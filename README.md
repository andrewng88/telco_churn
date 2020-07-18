# Telco Churn Prediction 
## Classification and Supervised ML
- [Demo](#demo)
- [Overview](#overview)
- [Motivation](#motivation)
- [Technical Aspect](#technical-aspect)
- [Installation](#installation)
- [Deployment on Heroku](#deployment-on-heroku)
- [Directory Structure](#directory-structure)
- [To Do](#to-do)
- [Technologies Used](#technologies-used)
- [Team](#team)
- [License](#license)
- [Credits](#credits)

# Demo
Please note that it's not down but it takes some time for the server to spin up.
Link : https://dockerchurn.herokuapp.com/
![Drag Racing](https://i.imgur.com/SoTmPWs.png)

# Overview
This is a simple binary classification Streamlit app trained using Scikit-Learn's Logistic Regression. The trained model takes a list features such as customer profile , subscriptions that they subscribed to ( i.e Internet, StremingTV etc) and also payment profile and predict wheather the customer will churn or not.

# Motivation
- To build up my portfortlio as I'm unable to share what is done in my previous job due to  private and confidentiality.
- To practise my Python skills during lockdown especially in learning deployment from various cloud services and also the important pipeline/column transformer feature with Scikit Learn. Previously I deployed **another end to end [HDB Price Prediction project at AWS](https://bit.ly/3io2TYZ)**  and this time I tried Heroku as it's free and this app does not require much space and memory. 

# Technical Aspect
This project is divided into 2 major parts:

1. EDA and Modelling.

2. Building and hosting a Streamlit web app on Heroku . The user can either predict one row at a time OR perform batch prediction. You can download the CSV template from the web app, edit , re-upload and after prediction the output will be displayed at the browser OR you may download the CSV.

# Directory Structure
1. Jupyter Notebooks portion are located at **1_EDA** and **2_Modelling** .
Raw [CSV](https://github.com/IBM/telco-customer-churn-on-icp4d/blob/master/data/Telco-Customer-Churn.csv) by IBM.
Processed dataframe is churn_done.csv

2. Train Pickled models will have .pkl extension

3. Deployment files are located at deploy folder whereby app.py => web app , Dockerfile(instruction for Docker) and requirements.txt( libraries required ) 

```
├───Churn_Project
│   1_EDA.ipynb
│   2_Modelling.ipynb
├───data
│       churn.csv
│       churn_done.csv
│       logreg_model.pkl
│       rf_model.pkl
│       svc_model.pkl
├───deploy
│   │   app.py
│   │   Dockerfile
│   │   requirements.txt
│   └───data
│           churn.png
│           logreg_model.pkl
│           odds.csv
│           rf_model.pkl
│           svc_model.pkl
│           template.csv
```
# Installation

> STEP 1 ( Local )

Git clone this repo

Install streamlit.
!pip install streamlit

Install [Dockers for Windows 10 Home](https://docs.docker.com/docker-for-windows/wsl/). Yes, dockers can be installed in Home. I'm so happy that I do not need to allocate space for Linux partition on my lappy

CD to **deploy** directory to build the docker image
```sh
$ docker build -t yourappname:latest
```
( Optional but Recommended)
 Run image locally to ensure it's working before you deploy at the cloud. Streamlit uses 5801 but Heroku will help you assign. You can access via http://localhost:5801/ . 

 ```sh
$ docker run -d -p 5801:5801 yourappname
```
 Ctrl-C to end the session
 
 > STEP 2 ( Heroku )
 
# Deployment on Heroku
 
Create heroku account and install [heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
 ```sh
$ heroku container:login
```

Create app/url at heroku. If urlname is qwerty. Your app will be accessed via http://qwerty.herokuapp.com
 ```sh
$ heroku create urlname
```

Push docker image to Heroku cloud
 ```sh
$ heroku container:push web --app urlname
```

Execute the below command to create the container onto Heroku
 ```sh
$ heroku container:release web --app urlname
```
Hurrah, you can access it at http://qwerty.herokuapp.com

More info on [Dockers @ heroku](https://devcenter.heroku.com/articles/container-registry-and-runtime)

# To Do
1. Use [PyCaret](https://pycaret.org/) to Gridsearch through all the algo or perhaps a Voting Classifier to improve the performance
2. Deploy using Amazon Elastic Container Service (ECS) and Fargate ( Serverless)

# Technologies used
***
![Tech Used](https://i.imgur.com/SntSjI4.png)<br>
And of course [Dillinger](https://dillinger.io/) for web based WYSIWYG markdown editing.

# Team
| ![Tech Used](https://i.imgur.com/f93NtGU.png)  |
|---|
| [Andrew Ng ](https://www.linkedin.com/in/sc-ng-andrew/)  |

# License
***
MIT

# Credits
***
Really love [streamlit](https://www.streamlit.io/)
