Development
===========
Developers of softworks can clone the repository from the `softworks Github repo <https://github.com/skyworksinc/Softworks>`.

Development Setup
-----------------
#. Setup development environment using the dev.yml file in envs/
#. Open a project using the sp command with the -p option to specify the development
   environment.
#. | For SKILL code development, the SKILL IDE can be opened from within Virtuoso.
   | For general development it is recommended that Softworks be attached to the User's IDS PyCharm project.

Note that Updates to the SKILL code can be reloaded directly from the SKILL IDE.  However updates to the
to any of the data.reg will require the Softworks Conda package to be rebuilt and the
development environment updated with the new version before the updates will take affect.

Conda Package
-------------
Softworks is built into a conda package for distribution.  The conda package uses IDS-skill
to setup the Virtuoso environment.  Please see http://idshost/IDS-skill/index.html for further details.

Release Methodology
-------------------
Softworks uses the IDS common release methodology.

Details: http://idshost/Development.html

.. toctree::
   :caption: Contents:
   :hidden:

   view_type_packages