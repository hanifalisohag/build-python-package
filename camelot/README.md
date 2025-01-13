# Camelot Project

## Overview

This project provides a Python package named `camelot` which is a playful experiment demonstrating Python packaging and execution. This package can be built into a wheel and used in various typical Python environments.

## Directory Structure

The project follows a simple directory structure:

### Project Structure
```
camelot
├───src
│    ├───camelot.py
│    └─── __init__.py
├───LICENSE.txt
├───pyproject.toml
└───Readme.md
```

## `pyproject.toml`

The `pyproject.toml` file includes essential metadata:

```toml
[project]
name = "camelot"
version = "1.0.0"
scripts = { "camelot-run" = "camelot:camelot" }
description = "Python project build as a module"
license = { file = "LICENSE.txt" }

[[project.authors]]
name = "Md Hanif Ali Sohag"
email = "hanifalisohag@gmail.com"

[build-system]
requires = ['setuptools>=42','wheel']
build-backend = 'setuptools.build_meta'
```

and `src/camelot.py`

```python
def camelot():
    print("It's only a model...")

if __name__ == '__main__':
    camelot()
```

Now we can run (output redacted):
```
$ pip wheel .
```
```
Processing c:\build_tutorial\build-python-package\another\camelot
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: camelot
  Building wheel for camelot (pyproject.toml) ... done
  Created wheel for camelot: filename=camelot-1.0.0-py3-none-any.whl size=1864 sha256=2e0fc4300c118e07e0ed71e1239e02b1c4f26727d51103d74f3d6f93525f9cdf
  Stored in directory: C:\Temp\pip-ephem-wheel-cache-7ljrh6_z\wheels\04\ce\80\99e702da6438a21a256232ce8f95ced8a4d13c5f8e9362c1bd
Successfully built camelot
```

Which we can test by making a local venv, activating it, and installing that wheel file into it:
```
$ python -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install camelot-1.0.0-py3-none-any.whl 
```
```
Processing ./camelot-1.0.0-py3-none-any.whl
Installing collected packages: camelot
Successfully installed camelot-1.0.0
```
and try the wrapper:

```
(.venv) $ camelot-run 
It's only a model...
```

(The wrapper `import`s the code, so that __name__ will be `'camelot'`, and not `'__main__'`. However, it then explicitly calls the camelot function itself - that’s what the `:camelot` part is for in `pyproject.toml`. Use `.`s normally for the package/module “path”, and `:` optionally to mark something inside the module to call. No arguments are passed; you’ll have to access and parse `sys.args` yourself if you care about command-line arguments.)


This of course also allows library use:
```
(.venv) $ python
Python 3.8.10 (default, May 26 2023, 14:05:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import camelot
>>> camelot.camelot()
It's only a model...
```
and running as a module:

```
(.venv) $ python -m camelot
It's only a model...
```
and running as a script (if you can find it):

```
(.venv) $ python .venv/lib/python3.8/site-packages/camelot.py 
It's only a model...
```

### Build
```
py -m pip install --upgrade build
py -m build
```


### References (Check for Uploading to real PyPI)
- [Building a package](https://discuss.python.org/t/how-to-release-python-code-on-github/38559/6)
