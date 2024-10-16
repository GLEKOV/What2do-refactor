what2do refactoring using FastAPI tutorial
https://www.youtube.com/watch?v=XWJWJfTWjSs

Project Structure

(root)
|
|__.gitignore
|__poetry.lock
|__pyproject.toml
|__README.md
|
|__(app)
|  |__main.py
|  |__.env
|  |__.env.templates
|  |
|  |__(api)
|  |  |____init__.py
|  |
|  |__(core)
|     |____init__.py
|     |__config.py
|     |
|     |__(models)
|        |____init__.py
|        |__db_helper.py



File explanations:

pyproject.toml - dependencies

.env.templates - default values for .env for Settings class

app/api/__init__.py - basic router

app/core/config.py - data classes and Settings class

app/core/models/db_helper.py - db engine factory and sessionmaker




