FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential && apt-get clean

COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --no-dev

COPY backend ./backend

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
