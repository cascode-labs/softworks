# Softworks

Enables software-based circuit design flows in Cadence Virtuoso.  It also enables documentation views.

## Overview

Softworks intimately couples generator code or configuration with template schematic and symbol views of a circuit design.
It allows code and software notebooks to be included in the Cadence Virtuoso database.  It supports both Python using
the PyCharm IDE and SKILL using Cadence's built in SKILL IDE for editing.  It is based on the idea that a library can
simultaneously be a Cadence Library and a Python Package.  It also supports Markdown, pptx, xls, and pdf views to
streamline documentation of IP libraries to improve team collaboration.

## Custom Cell Views


| View Type   | Extensions    | Editors          | Description                  |
| ----------- | ------------- | ---------------- | ---------------------------- |
| pdf         | *.pdf         | xpdf             | A pdf Document              |
| ppt         | *.pptx        | open office      | A power point presentation  |
| Excel       | *.xlsx *.xlsm | open office      | A spreadsheet               |
| html        | *.html        | firefox          | A web page                  |
| module      | *.py *.pyc    | VS Code,         | A Python module             |
| notebook    | *.ipynb       | VS Code, gedit   | A Python Jupyter notebook   |
| markdown    | *.md          | VS Code, gedit   | A markdown document. VS code enables editing and rendering |
| yaml        | *.yml         | VS Code, gedit   | A yaml data file            |
| skill       | *.il          | Skill IDE, gedit | A SKILL code file           |
| skillpp     | *.ils         | Skill IDE, gedit | A SKILL++ code file         |


Creating a New View
-------------------

A new blank document view can be created by using the standard "File -> New -> Cell View..." selection.
Then some view types will create a new cellview directly based on a template file while the
documentation views will open a GUI.  This GUI has the option to either create the new cell view from a template or
import an existing file to the cell view.


 Note: Need to add a picture of the import gui
 57  
README.rst
