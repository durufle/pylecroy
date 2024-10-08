# pylecroy: python package for lecroy

This package use the [ActiveDSO](https://teledynelecroy.com/support/softwaredownload/activedso.aspx) active X control version 2.36 from lecroy. 

This version can be used only on Windows station.

## Installation

Installation from the Pypi repository:

```bash
pip install ragnarok_pylecroy
```

## development

clone the repository in your workspace:

```bash
cd ./workspace
~/workspace $ git clone https://github.com/durufle/pylecroy.git
```

select package folder, create a virtual environment and select it:

```bash
~/workspace $ cd pyrs
~/workspace/pyrs $ python -m venv venv
~/workspace/pyrs $ source ./venv/bin/activate
# install dependency package
(venv) ~/workspace/pyrs $ pip install -r requirements.txt
(venv) ~/workspace/pyrs $ pip install -r development.txt
```
Use you preferred IDE to develop (PyCharm,...)

To build a wheel package:

```bash
(venv) ~/workspace/pylecroy $ python -m build
```

To execute pylint locally you can do the following:

```bash
(venv) ~/workspace/pyrs $ pylint $(git ls-files '*.py')
```
This will execute pylint for all python files in the repository.

