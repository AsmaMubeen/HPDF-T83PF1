# HPDF-T83PF1

This repository contains Python-Flask backend, ReactJS and ReactNative frontend code for web, mobile apps which extract entities which are sub strings of a text, using https://wit.ai 

Refer to [README-ReactNative.md](README-ReactNative.md) for instructions on using ReactNative code and mobile app APK link

Refer to [README-ReactJS.md](README-ReactJS.md) for instructions on using ReactJS code

## Requirements
* Hasura CLI
* Python 3.x

## Clone and Deploy

* Download and install Hasura CLI.
* Run the below commands in git bash 

```
$ hasura quickstart asma_mubeen/python-wit-integration
$ cd python-wit-integration
# Deploy
$ git add . && git commit -m "Deployment commit"
$ git push hasura master

```

* Now you can see the microservices list and their URLs by running the command below

```
$ hasura ms list

```
* The microservice app is python-flask API.
* The microservice www is ReactJS web app.

## Modify

* Change the access token of wit app in python-flask API.  ( Refer to [Python-Flask README.md](microservices/app/README.md) for details)
* Replace cluster name in backend API URL in ReactJS and React Native code. ( Refer to [README-ReactJS.md](README-ReactJS.md) and [README-ReactNative.md](README-ReactNative.md) for details)
* Push the changes to the cluster.
