# Pre-requisites

- Python 3
- Pip

# Running the tests

## From VSCode with Python extension
either:
- right-click on test-file & select 'Run All Tests'
- shift-[ctrl/cmd]-p and select 'Python: Run All tests'
- 'Run Tests' lightning-bolt button in bottom bar
    - To see output, click it again & select 'View Test Output'

## From command-line

Mac:
```
pip3 install -U pytest
python3 -m pytest tests/test.py
```

Other:
```
pip install -U pytest
python -m pytest tests/test.py
```