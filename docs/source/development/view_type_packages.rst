View Type Modules
==================
Each view type package supports a view type or set of related view types in Cadence Virtuoso.
Each folder under src/ is a view type package and must include the following.

* **SKILL++ Modules**: Define the code for creating a new view and opening an existing view.
* **data.reg File**: Defines the view types in the Cadence data registry.
* **File Templates**: A file for each veiw type which is copied when creating a new cell view
* **Initialization Script**: An init.il or init.ils script
* **Documentation**
* **Conda Recipe**

SKILL++ Modules
----------------
The code for creating a new view and opening an existing view is defined in one or more SKILL++ packages.
A package general includes each of the following elements.  Each of the functions listed here must be a public function
of the package.

viewSetup
^^^^^^^^^
A package variable named viewSetup.  This is a list containing an entry for each view type defined in the view
type package. Each view's entry is a list containing 4 elements: (viewType appName dataTrigger parentType)

* **viewType**: A string which must match the dfII_ViewType of the Dataformat entry in the data.reg file
* **appName**: A string which must match the name of the associated tool entry in data.reg
* **dataTrigger**: The name of the callback function as a string.  It is called both when a new cell view of this type
  is created and when an existing view of this type is opened.
* **parentType**: A string which defines the parent type for a child view type.  Child view types allow addition editor
  applications to be defined for a view type.  All the entries of a child view type must be unique from the
  parent view type and all the other children.  Each view type must have a single parent with parentType set to
  "nil".  Then each child type entry should come after it, indented on a new line with the dataTrigger set
  to "nil" and the parentType set to the viewType of the parent.

init Function
^^^^^^^^^^^^^
A public function which registers each view.  In most cases this can register the views defined in viewSetup using the
following standard function definition:

.. code-block::

  ; Register All Python Custom Cellviews
  procedure(init() let(((out t))
    Softworks->initDeRegApp(viewSetup)
  ))

uninit Function
^^^^^^^^^^^^^^^
A public function which unregisters each view.  In most cases this can unregister the views defined in viewSetup using the
following standard function definition:

.. code-block::

  ; uninitialize all Python views so they can be redefined
  procedure(uninit() let(((out t))
    Softworks->uninitDeRegApp(viewSetup)
  ))

DataTrigger Function
^^^^^^^^^^^^^^^^^^^^
A public function which is called both when a new cell view of this type is created and when an existing view of
this type is opened.  This must be accessible as a global skill symbol when it is registered.  Hence it must be exported
as a global function.

data.reg File
-------------
A cadence data registry file which defines the view type must be included in each view type
package.  The data.reg is added to the conda environment's data.reg as part of the Softworks Conda recipe.

The Dataformat parameters:

* Pattern: Defines the filename of the view's master file.  It can be in terms of a file extension by using the
  \*.ext format or can be an absolute name such as table.xlsx
* Preferred_Editor: The default editor to be used to open the views of this type
* Default_Editor: Same as Preferred_Editor.  This should both have the same entry.
* dfII_ViewType: View Type name
* Co_Managed: Other files in the view's folder that are managed along with the master file.

A separate Tool entry must be made for each editor to be used by the view type.  These tool entries
must be unique for each view type.  The naming convention for tool entries is "editorName_viewType"

Example View Definition:

.. code-block::

  DataFormat module_df {
	Pattern = *.py;
	Preferred_Editor = pyCharm_module;
	Default_Editor = pyCharm_module;
	dfII_ViewType = module;
	Co_Managed = *.py master.tag data.dm *.ipynb *.pyc;
  }
  Tool pyCharm_module {  }
  Tool gedit_module {  }

File Templates
--------------
Each view type can have one or more templates that can be used when creating a new view.
These should be directly included in the associated view type packages.

Initialization Script
---------------------
Initialization of each package should be added to the common SKILL initialization script in the
repository root.  It is named "Softworks.init.ils".

Documentation
-------------
Each view type package should have its own page documenting the views and tools included in that package.  This
should be added as a restructured text document to the docs/source/ folder.  This should include a table outlining
the views included in the package and other details about the tools added to be able to open those views.

The documentation must then be included in the index.rst toctree so it is accessible from the homepage.

Conda Recipe
------------
Each view type package needs to have its data.reg included in the environment's data.reg.
This is accomplished by adding a new entry in the build.sh script of Softwork's Conda
recipe.

Example Entry for the Python view type package in build.sh:

.. code-block::

  # data.reg
  echo "SOFTINCLUDE ${PREFIX}/lib/skill/Softworks/src/python/SdmPy.data.reg;" >> \
  "${PREFIX}/lib/skill/IDS.data.reg"
