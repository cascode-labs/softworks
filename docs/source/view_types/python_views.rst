Python Views
============

`Python <https://www.python.org/>`_ views support the development of Python
code to automate the design and verification of circuits.  This can range 
from simple run scripts for automating a portion of the design flow to full
analog and RF generators.  

Support for `Jupyter <https://jupyter.org/>`_
notebooks is also included to support protoyping and run scripts.
Markdown is included to easily prepare documentation.

+-------------+-----------------+-------------+------------------------------+
| View Type   | Extensions      | Editors     | Description                  |
+=============+=================+=============+==============================+
| module      | \*.py (\*.pyc)  | VS Code,    | A Python module              |
|             |                 | gedit       |                              |
+-------------+-----------------+-------------+------------------------------+
| notebook    | \*.ipynb        | VS Code,    | A Python Jupyter notebook    |
|             |                 | gedit       |                              |
+-------------+-----------------+-------------+------------------------------+
| markdown    | \*.md           | VS Code,    | A markdown document. PyCharm |
|             |                 | gedit       | supports both editing and    |
|             |                 |             | rendering.                   |
+-------------+-----------------+-------------+------------------------------+
| yaml        | \*.yml          | VS Code,    | A yaml data file             |
|             |                 | gedit       |                              |
+-------------+-----------------+-------------+------------------------------+

VS Code IDE
-----------
`Visual Studio Code (VS Code) <https://code.visualstudio.com/>`_  is the default editor for Python
views.  It supports all the included Python view types.  Many of the views require extensions to be installed.  Before opening VS Code, it can be started from the
Softworks menu in the library manager to open the code workspace of the current project.

Gedit Text Editor
-----------------
`Gedit <https://help.gnome.org/users/gedit/stable/>`_ is included as another
option for editing Python views.  It is just a relatively simple text editor.
It is not as powerful as PyCharm but opens much faster than
PyCharm and doesn't need to be started separately before opening views.
