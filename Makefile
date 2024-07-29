#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`

#* Docker variables
IMAGE := chatbot-demo
VERSION := latest

#* Docker
# Example: make docker-build VERSION=latest
# Example: make docker-build IMAGE=some_name VERSION=0.1.0
.PHONY: docker-build
docker-build:
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build \
		-t $(IMAGE):$(VERSION) .

# Example: make docker-remove VERSION=latest
# Example: make docker-remove IMAGE=some_name VERSION=0.1.0
.PHONY: docker-remove
docker-remove:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi -f $(IMAGE):$(VERSION)

.PHONY: serve
serve:
	gunicorn chatbot_demo.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080

.PHONY: docker-serve
docker-serve: docker-build
	docker run -p 8080:8080 --env-file=.env $(IMAGE):$(VERSION) make serve
