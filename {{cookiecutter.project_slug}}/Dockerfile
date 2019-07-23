FROM python:3.7.3-slim-stretch AS base

RUN pip install -U pip

# Build Stage
FROM base AS build

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        gcc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /wheels
COPY requirements.txt .

RUN pip wheel -r requirements.txt

# Execution Stage
FROM base

ENV PYTHONUNBUFFERED=1

COPY --from=build /wheels /wheels

RUN pip install -r /wheels/requirements.txt -f /wheels && \
    rm -rf /wheels && \
    rm -rf /root/.cache/pip/*

WORKDIR /app

COPY {{ cookiecutter.package_name }} {{ cookiecutter.package_name }}

ENTRYPOINT ["python"]
CMD ["-m", "{{ cookiecutter.package_name }}"]
