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
    │   │   ├── connect_mlflow.py
    │   │   ├── exploration.ipynb
    │   │   ├── mlflow.db
    │   │   ├── mlruns
    │   │   │   ├── 0
    │   │   │   │   └── meta.yaml
    │   │   │   └── 377716236188296258
    │   │   │       ├── 943e7fadc314445b92c31df5cb10f532
    │   │   │       │   ├── artifacts
    │   │   │       │   ├── meta.yaml
    │   │   │       │   ├── metrics
    │   │   │       │   ├── params
    │   │   │       │   │   └── test_param
    │   │   │       │   └── tags
    │   │   │       │       ├── mlflow.runName
    │   │   │       │       ├── mlflow.source.git.commit
    │   │   │       │       ├── mlflow.source.name
    │   │   │       │       ├── mlflow.source.type
    │   │   │       │       └── mlflow.user
    │   │   │       └── meta.yaml
    │   │   └── train_model.py
    │   ├── model
    │   ├── requirements.txt
    │   └── tests
    ├── docs
    │   ├── index.md
    │   └── user_guide
    │       └── getting_started.md
    ├── frontend
    │   └── requirements.txt
    ├── main.py
    ├── mkdocs.yml
    ├── mlruns
    │   ├── 0
    │   │   └── meta.yaml
    │   └── 586956296079912339
    │       ├── 9e24cda01c51402ea7d7cab72b3b630b
    │       │   ├── artifacts
    │       │   ├── meta.yaml
    │       │   ├── metrics
    │       │   ├── params
    │       │   │   └── test_param
    │       │   └── tags
    │       │       ├── mlflow.runName
    │       │       ├── mlflow.source.git.commit
    │       │       ├── mlflow.source.name
    │       │       ├── mlflow.source.type
    │       │       └── mlflow.user
    │       └── meta.yaml
    ├── pyproject.toml
    └── uv.lock
