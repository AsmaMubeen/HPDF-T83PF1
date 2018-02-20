# Description for ReactJS code

* Source code for ReactJS web app -> https://github.com/AsmaMubeen/HPDF-T83PF1/tree/master/microservices/www
* Our app is live at https://www.fridge28.hasura-app.io/

* Run the below command to open your shiny new deployed react app.
``` shell
$ hasura microservice open www
```

## Modification

* Replace "fridge28" with your cluster name in the backend API URL (https://app.fridge28.hasura-app.io/) in microservices/www/app/src/App.js
    * `var url =  'https://app.<YourClusterName>.hasura-app.io/'`


## Local development

To test and make changes to this app locally, follow the below instructions.
* Open Terminal and `cd` into the project folder
* Run `npm install` to install all the project dependencies
* Run `npm start` and `npm build` in the terminal to build and run it.
* Make changes to the app, and see the changes in the browser



## Screenshot of ReactJS web app

<img src="README-Assests/Screenshot (333).png" width = "800">
