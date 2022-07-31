Overview
=========

Enables software-based circuit design flows in Cadence Virtuoso.  It also enables documentation views.

Softworks intimately couples analog generator code with template schematic and symbol views of a circuit design.
It allows code and software notebooks to be included in the Cadence Virtuoso database.  It supports both Python using
the PyCharm IDE and SKILL using Cadence's built in SKILL IDE for editing.  It is based on the idea that a library can
simultaneously be a Cadence Library and a Python Package.  It also supports Markdown, pptx, xls, and pdf views to
streamline documentation of IP libraries to improve team collaboration.

Custom Cell Views
-----------------

+-------------+-----------------+-------------+------------------------------+
| View Type   | Extensions      | Editors     | Description                  |
+=============+=================+=============+==============================+
| pdf         | \*.pdf          | xpdf        | A pdf Document               |
+-------------+-----------------+-------------+------------------------------+
| ppt         | \*.pptx         | open office | A power point presentation   |
+-------------+-----------------+-------------+------------------------------+
| Excel       | \*.xlsx \*.xlsm | open office | A spreadsheet                |
+-------------+-----------------+-------------+------------------------------+
| html        | \*.html         | firefox     | A web page                   |
+-------------+-----------------+-------------+------------------------------+
| module      | \*.py (\*.pyc)  | PyCharm,    | A Python module              |
|             |                 | gedit       |                              |
+-------------+-----------------+-------------+------------------------------+
| notebook    | \*.ipynb        | PyCharm,    | A Python Jupyter notebook    |
|             |                 | gedit       |                              |
+-------------+-----------------+-------------+------------------------------+
| markdown    | \*.md           | PyCharm,    | A markdown document. PyCharm |
|             |                 | gedit       | supports both editing and    |
|             |                 |             | rendering.                   |
+-------------+-----------------+-------------+------------------------------+
| yaml        | \*.yml          | PyCharm,    | A yaml data file             |
|             |                 | gedit       |                              |
+-------------+-----------------+-------------+------------------------------+
| skill       | \*.il           | Skill IDE,  | A SKILL code file            |
|             |                 | gedit       |                              |
+-------------+-----------------+-------------+------------------------------+
| skillpp     | \*.ils          | Skill IDE,  | A SKILL++ code file          |
|             |                 | gedit       |                              |
+-------------+-----------------+-------------+------------------------------+

Creating a New View
-------------------

A new blank document view can be created by using the standard "File -> New -> Cell View..." selection.
Then some view types will create a new cellview directly based on a template file while the
documentation views will open a GUI.  This GUI has the option to either create the new cell view from a template or
import an existing file to the cell view.

..
  Note: Need to add a picture of the import gui when it is ready

.. toctree::
   :caption: Contents:
   :hidden:

   documentation_views
   python_views
   skill_views
   release_notes
