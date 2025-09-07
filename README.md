[![PEP-08](https://img.shields.io/badge/code%20style-PEP08-green.svg)](https://www.python.org/dev/peps/pep-0008/)


you are reading VERSION = v0.0.3-develop


# thonny-gitonic 

[thonny](https://thonny.org) plugin for [gitonic](https://github.com/kr-g/gitonic)

open `gitonic` in thonny by pressing Control+Shift+g, or via tools menu

press `ESC` key to minimize gitonic window.


# what's new ?

Check
[`CHANGELOG`](https://github.com/kr-g/thonny-gitonic/blob/main/CHANGELOG.md)
for latest ongoing, or upcoming news.


# limitations

Check 
[`BACKLOG`](https://github.com/kr-g/thonny-gitonic/blob/main/BACKLOG.md)
for open development tasks and limitations.


# platform

tested on python3, and linux


# installation

    python3 -m pip install thonny-gitonic


# configuration

## custom installation path

in file `~/.gitonic/thonnycontrib.cfg` 

    [DEFAULT]
    # will run gitonic from local installation 
    path = .

    [DEFAULT]
    # will run gitonic from specific .venv installation 
    path = ~/gitonic/.venv/bin



# license

thonny-gitonic is released under the following
[`LICENSE`](https://github.com/kr-g/thonny-gitonic/blob/main/LICENSE.md)
