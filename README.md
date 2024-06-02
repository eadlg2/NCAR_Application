# Foo Parameterization

This is a Python package for calculating the Foo et al. parameterization.

# Installation

This project is configured to be installed using `pip`.

To install the package into a Python environment, run the following command from the root directory:

```
pip install .
```

# Tests

The repository contains tests for ensuring the code is working. These may be ran using [PyTest](https://docs.pytest.org/en/8.2.x/). PyTest can be installed by running:

```
pip install pytest
```

After PyTest is intalled, the tests can be ran through the following commands from the root directory:

```
cd tests
pytest
```

# Direct Use

The package may also be directly used after cloning. From within the `src/foo_parameterization` directory, calculations can be made interactively from the command line using the following command:

```
python foo.py
```