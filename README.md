# curso-python-practico


Instalación con virtualenv

```bash
virtualenv --python=python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

instalación con pipenv

```bash
pip install pipenv
pipenv install
pipenv shell
jupyter notebook
```

```bash
python -m unittest tests/test_example01.py
python -m unittest tests/test_example02.py
py.test tests/test_example02_1.py 
tox
```
