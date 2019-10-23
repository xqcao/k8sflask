install Kubernetes

https://matthewpalmer.net/kubernetes-app-developer/articles/guide-install-kubernetes-mac.html

#1.build Image.

    1. docker build -t hello-flask-img .

#2. open hub.docker.com, and create one repository, will generate name like="adamcao/hello-flask-img"

#3. push to hub.docker.com

_1._ docker tag hello-flask-img adamcao/hello-flask-img
_2._ docker push adamcao/hello-flask-img
_3._ https://cloud.docker.com/u/adamcao/repository/docker/adamcao/hello-flask-img

#4. run cluster:

_1._ minikube start // in 2 mins

#5. deploy it to cluster

_1._ kubectl apply -f mydeployment.yml
_2._ or minikube dashboard
_3._ and from dashboard click "create" and load yaml file

#6. run
_1._ minikube dashboard

#7. after 1 or 2 mins,
_1. _ open page on browser
