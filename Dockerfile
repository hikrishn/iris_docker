FROM quay.io/coreos/hyperkube:v1.9.6_coreos.2


MAINTAINER krish-io

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

#ADD src/config/application.properties /src/config/application.properties
COPY ./src /src
#COPY ./lib/* /src/
#ENV PYTHON_VERSION 2.7
#RUN pip3 install typing
RUN pip3 install boto3
RUN pip3 install bottle
RUN pip3 install pyyaml
#RUN pip3 install logging
RUN pip3 install waitress
RUN pip3 install urllib3
RUN pip3 install python-dateutil

#Dependencies for my iris application
RUN pip3 install scikit-learn



RUN useradd -ms /bin/bash iris-docker
USER iris-docker

ENTRYPOINT ["python", "/src/sup_class.py", "-p 8080"]
EXPOSE 8080

#docker build -
# docker build -t iris_sup_docker . --no-cache
# docker run -dp 8080:8080 iris_sup_docker
#curl -X POST 0.0.0.0:8080/iris/v1/predict -H 'Content-Type: application/json' -d '[8,9,7,1]'
#curl -X POST ec2-52-66-197-175.ap-south-1.compute.amazonaws.com:8080/iris/v1/predict -H 'Content-Type: application/json' -d '[8,9,7,1]'
#Run App local bottle server instead of inside a docker redhat container
#python ./src/sup_class.py


#google cloud
# gcloud auth login
# gcloud auth configure-docker
## docker tag SOURCE_IMAGE HOSTNAME/PROJECT-ID/TARGET-IMAGE:TAG
#docker tag iris_sup_docker gcr.io/krish-gcp-iris/iris_sup_docker:0.0.1
## docker push HOSTNAME/PROJECT-ID/IMAGE:TAG
#docker push gcr.io/krish-gcp-iris/iris_sup_docker:0.0.1
# curl -X POST  http://35.202.119.145:8080/iris/v1/predict -H 'Content-Type: application/json' -d '[8,9,7,1]'
