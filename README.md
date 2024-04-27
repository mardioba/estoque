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

[python-decouple](https://github.com/HBNetwork/python-decouple)

[Como usar o desacoplamento Python](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html)

[tutoriais django basico por RG3915](https://github.com/rg3915/tutoriais)

[Include Bootstrap’s CSS and JS - Template Base.html](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

[django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks)