# Pre-requisites

- Python 3
- Pip for Python 3
- pytest

Check installation with 

```
python --version && pip --version
```

If python or pip versions are for Python 2, check if Python 3 versions are installed as `python3` / `pip3`:

```
python3 --version && pip3 --version
```

To install pytest:

```
pip install -U pytest
```

or, using `pip3`:

```
pip3 install -U pytest
```


# Running the tests

## From command-line

```
python -m pytest tests/
```

or, using `python3`:

```
python3 -m pytest tests/
```


## From VSCode

After installing the Python extension from Microsoft,

- Open the 'Testing' panel in the left bar
- Choose the test(s) to run

If this doesn't work, you may need to configure the tests:
- shift-[ctrl/cmd]-p
- type/select 'Python: Configure tests'
- select `pytest`


