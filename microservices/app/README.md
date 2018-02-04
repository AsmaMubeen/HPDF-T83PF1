# Description of Python-Flask API

* This API returns entity type and entity value present in the text, when a post request is made to it, in the form-data format, 
  with key = input and value = "<--Text entered by the user-->"
* This API uses a wit app which is trained to recognize entities such as:
  
entity        | Example of values            |  Example of entered texts
------------- | -------------               |  --------------
thing         | pen                         |  show images of pen
message       | come home early  |    tell mom that come home early
song          | the faded        |  show the faded lyrics
volume        |  250 ml          |   How much is 250 ml in litres
number         | 456              |   456


* location : Recognizes locations
* datetime : Recognizes time and date ; Eg: 6 am
