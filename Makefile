.PHONY:	all container push

TAG = 0.0.1
REGISTRY = 080385600816.dkr.ecr.us-east-1.amazonaws.com
IMAGE = iris_sup_docker
LOGIN:=$(shell aws ecr get-login --no-include-email)

all: container \
     push \


container:
	docker build -t $(IMAGE):$(TAG) . --no-cache

push: container
	exec ${LOGIN}
	docker tag $(IMAGE):$(TAG) ${REGISTRY}/$(IMAGE):$(TAG)
	docker push ${REGISTRY}/$(IMAGE):$(TAG)

