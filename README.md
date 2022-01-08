# Pre-requisites

- `python3`
- `pip3`

Check installation with 

```
python3 --version && pip3 --version
```

# Set up virtual environment and install dependencies

1. Create a new virtual environment called '.env':

```
python3 -m venv .env
```

2. Activate it:

```
source .env/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

If you need to de-activate the virtual environment, the command is `deactivate`.

# Running tests

## From command-line

```
pytest
```


## From VSCode

After installing the Python extension from Microsoft,

1. Tell VSCode to use the virtual environment
   - shift-[ctrl/cmd]-p
   - type/select 'Python: Select Interpreter'
   - select the one at `./.env/bin/python3`
3. Open the 'Testing' panel in the left bar
4. Choose the test(s) to run

If this doesn't work, you may need to configure the tests:
- shift-[ctrl/cmd]-p
- type/select 'Python: Configure tests'
- select `pytest`


