# flask-blog-test
simple blog api (python 3.8 + flask)
## Setup

```bash
$ python -m venv .venv
$ & .\.venv\Scripts\Activate.ps1
$ pip install -U -r requirements.dev.txt
```

## Run dev

```bash
$ python server.py
```

Windows PowerShell

```
> & .venv\Scripts\Activate.ps1
> $env:FLASK_ENV = "development"
> $env:FLASK_APP = "app_blog"
> flask run
```

or Windows CMD

```shell
> .venv\Scripts\activate.bat
> set FLASK_ENV=development
> set FLASK_APP=app_blog
> flask run
```
