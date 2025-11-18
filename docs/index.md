# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    ├── README.md
    ├── backend
    │   ├── app
    │   ├── ml
    │   │   ├── mlflow.db
    │   │   ├── mlruns
    │   │   └── train_model.py
    │   ├── model
    │   │   ├── model.pkl
    │   ├── requirements.txt
    │   └── tests
    │   │   ├── test_api.py
    │   │   └──test_train.py
    ├── docs
    │   ├── index.md
    │   └── user_guide
    │       └── getting_started.md
    ├── frontend
    │   ├── app.py
    │   └── requirements.txt
    ├── main.py
    ├── mkdocs.yml
    ├── pyproject.toml
    └── uv.lock
