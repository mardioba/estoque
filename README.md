# Estoque

## Como rodar o projeto?

* Clone esse repositorio.
* Crie uma virtualenv com Python 3.
* Ative a virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/mardioba/estoque.git
cd estoque
python3 -m -venv .venv
source .venv/bin/active
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

## Links

https://github.com/HBNetwork/python-decouple

https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html

