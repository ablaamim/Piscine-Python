### Define Package Structure:

> A Python package typically has a specific directory structure :

```
ft_package/
|-- ft_package/
|   |-- __init__.py
|   |-- module.py
|-- setup.py
|-- README.md
```

### Install dependencies :

```bash
pip install --upgrade setuptools wheel
```

### Inside ft_package/module.py, write the code for package. For example :

```
from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    description='my package',
    author='ablaammim',
    author_email='ablaamim@student.1337.ma',
    url='https://github.com/ablaamim/Piscine-Python/tree/master/Module-00-starting/ex09/ft_package',
    packages=find_packages(),
    install_requires=[],
)
```

* name: The name of your package.
* version: The version number of your package.
* description: A short description of your package.
* author: The author's name.
* author_email: The author's email address.
* url: The URL of your package's home page.
* packages: The packages to include in your distribution.
* install_requires: List of dependencies required for your package.

### Build the package :

> Run the following command to build the distribution files (source distribution and wheel) :

```bash
python3 setup.py sdist bdist_wheel
```

### Install the package :

> Install the package using one of the following command:


```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

### Verify installation :

```bash
pip show -v ft_package
```

### Test the package :

> Run the test_script.py :

```python
# test_script.py

from ft_package.module import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
```