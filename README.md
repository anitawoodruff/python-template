# Pre-requisites

- Python 3
- Pip for Python 3
- [pytest](https://docs.pytest.org/en/6.2.x/getting-started.html)

Check installation with 

```
python3 --version && pip --version && pytest --version
```

To install pytest:

```
pip install -U pytest
```


# Running the tests

## From command-line

```
pytest
```


## From VSCode

After installing the Python extension from Microsoft,

- Open the 'Testing' panel in the left bar
- Choose the test(s) to run

If this doesn't work, you may need to configure the tests:
- shift-[ctrl/cmd]-p
- type/select 'Python: Configure tests'
- select `pytest`


