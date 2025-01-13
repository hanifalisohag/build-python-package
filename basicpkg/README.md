# `basicpkg`

The `basicpkg` is a simple testing example to understand the basics of developing your first Python package.


### Project Structure
```
basicpkg
├───dist
│   ├─── basicpkg-1.0.0-py3-none-any.whl
│   └─── basicpkg-1.0.0.tar.gz
├───src
│   └───basicpkg
│       ├───__init__.py
│       ├───divide
│       │   ├───by_three.py
│       │   └─── __init__.py
│       └───multiply
│           ├───by_three.py
│           └─── __init__.py
│
├───tests
│    ├───test_divide_by_three.py
│    ├───test_multiply_by_three.py
│    └─── __init__.py
├───LICENSE.txt
├───pyproject.toml
├───Readme.md
└───setup.cfg
```

### Tests
```
python -m unittest discover -s tests
```

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```
### Build
```
py -m pip install --upgrade build
py -m build
```

### Install
```
pip install dist\basicpkg-1.0.0-py3-none-any.whl
```
### Install from github
```
pip install git+https://github.com/hanifalisohag/build-python-package.git
```
### Test Code
```
from basicpkg.divide import by_three
from basicpkg.multiply.by_three import multiply_by_three

# Example usage
result_divide = by_three.divide_by_three(9)  # Should return 3
print(result_divide)
result_multiply = multiply_by_three(9)  # Should return 27
print(result_multiply)

''' 
Output
3.0
27
'''
```


### References (Check for Uploading to real PyPI)
- https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/"# build-python-package" 
