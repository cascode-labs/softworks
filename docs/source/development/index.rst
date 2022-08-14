Development
===========
Developers of softworks can clone the repository from the `softworks Github repo <https://github.com/cascode-labs/softworks>`.

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
Softworks is built into a conda package for distribution on `conda-forge <https://conda-forge.org/#page-top>`_.
The Conda recipe can be found in the softworks-feedstock

Release Methodology
-------------------

softworks should be released on Github.  When a new release is published on 
Github then a workflow will build and publish softworks to PyPi.  Then the 
release on PyPi will trigger an update to the conda package.

.. toctree::
   :hidden:

   view_type_packages