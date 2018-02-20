# Python-Flask API

* [Source code for python-flask API](https://github.com/AsmaMubeen/HPDF-T83PF1/tree/master/microservices/app)

* This API returns **entity type** and **entity value** present in the text, when a **post request** is made to it, in the **form-data** format, 
   with **key = input** and **value="<--Text entered by the user-->"**

**EXAMPLE REQUEST**


```
curl -X POST \
  https://app.fridge28.hasura-app.io \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: <token>' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F 'input=show beat it lyrics'

```
**Example Response**

```json
[{"entityType": "song", "entityValue": "beat it"}]

```

* This API uses a wit app which is trained to recognize entities such as:
  
  Entity        | Example of value            |  Example of entered text
  ------------- | -------------               |  --------------
  thing         | pen                         |  show images of pen
  message       | come home early  |    tell mom that come home early
  song          | the faded        |  show the faded lyrics
  volume        |  250 ml          |   How much is 250 ml in litres
  number         | 456              |   456


* location : Recognizes locations
* datetime : Recognizes time and date




## MODIFICATION

* You can make your version of wit app and train it with different entities
        
* Follow [Wit docs recipe to extract an entity that is a substring of the message](https://wit.ai/docs/recipes#extract-an-entity-that-is-a-substring-of-the-message)

* To link your wit app to this API, update access token from git bash using the command below. You can find your wit app's access token on the settings page of the app.
```
$ hasura secrets update wit.token.key <--your wit app's token-->

```

* Check if the secret is updated using the command below.
```
$ hasura secrets list

```



