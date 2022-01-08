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


## From VSCode with Python extension
either:
- right-click on test-file & select 'Run All Tests'
- shift-[ctrl/cmd]-p and select 'Python: Run All tests'
- 'Run Tests' lightning-bolt button in bottom bar
    - To see output, click it again & select 'View Test Output'

