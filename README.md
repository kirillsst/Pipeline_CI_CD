# Iris ML Pipeline
This project demonstrates a full ML pipeline for training, serving, and deploying a simple Iris classifier.
It includes:
- Model training with scikit-learn
- FastAPI backend for predictions
- Streamlit frontend
- Automated tests with pytest
- Documentation deployment with MkDocs
- Dockerization for backend and frontend
- CI/CD with GitHub Actions
- Deployment on Azure App Service

## Structure project 
````bash
├── backend/         # FastAPI backend & ML code
├── frontend/        # Streamlit app
├── docs/            # MkDocs documentation
├── ml/              # model training & experiments
├── .github/workflows/ # CI/CD pipelines
├── Dockerfile(s)    # Docker configuration in backend and frontend
├── docker-compose.yml
├── README.md
├── mkdocs.yml
└── ...
````
## Getting Started
# 1. Clone the repository
git clone https://github.com/kirillsst/Pipeline_CI_CD.git
cd Pipeline_CI_CD

# 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
uv sync

# 4. Manual run guide
mkdocs serve

## CI/CD
- On push to main:
    - Code style is checked with **Ruff**    
    - Tests are run
    - Docs are built and deployed to GitHub Pages
    - Docker images for backend & frontend are built and pushed to DockerHub

## Azure Deployment
- Backend and frontend deployed on Azure App Service
- Backend URL used in frontend: https://irispipelinekirillsst-ebhncxhycxe2g6gt.francecentral-01.azurewebsites.net
- Frontend URL: https://irispipelinefrontendkirillsst-fxgra2gxembsf0gy.francecentral-01.azurewebsites.net



