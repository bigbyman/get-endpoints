# Get Endpoints


### Installation

Clone repo, then run `pip install get-endpoints` while in the repo. [click](http://click.pocoo.org/5/) and [colorama](https://pypi.python.org/pypi/colorama) will be installed alongside.

---
`getend` assumes that it is invoked one level above your 'controller' directory.

getend [OPTIONS]
 ---
`--l` List all controllers
 
`--name TEXT` Print controller (may be more than one if name matches more than one filename)

`--grep TEXT`   Print all lines from all controllers containing TEXT (with nice colors and formatting)

---
`--name` and `--grep` can be combined. You can use it to e.g. print only POST mappings.
