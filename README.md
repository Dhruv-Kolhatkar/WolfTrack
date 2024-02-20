<h1><b>WolfTrack </b></h1>

---

---

&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; <img width = "380" height = "450" src = "static/images/wolftrack3.0.png"> </img>

---

# ❓ Why WolfTrack3.0 ❓

Do you find yourself applying to too many companies and losing track of your time?

Do you want to hear from your coworkers or experts?

WolfTrack 3.0 aids in the planning and organization of job applications in a chronological manner so that you can conveniently track job applications, receive professional advice, and land your dream job. We keep track of job applications, job descriptions, locations, wages, dates, and notes, among other things.

&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; <img width="380" height="450" alt="confused_applicant" src="https://user-images.githubusercontent.com/66715000/144729660-8b6136c1-1034-41e5-a22e-cb10e2b3d36f.png">

**So, let's go get that job! 😎**

---

## 🥊 Punch Line

https://user-images.githubusercontent.com/66715000/144538638-acc75fa1-db5b-49a1-a5d0-9b3bbc79cf89.mp4

---

## 📚 Technology Stack

&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; <code><a href="https://developer.mozilla.org/en-US/docs/Glossary/HTML5" target="_blank"><img src = "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="50"/></a></code>
<code><a href="https://flask.palletsprojects.com/en/1.1.x/" target="_blank"><img height="50" src="https://freetutsdownload.net/wp-content/uploads/2021/07/Learn-Flask-A-web-Development-Framework-of-Python.jpg"></a></code>
<code><a href="https://developer.mozilla.org/en-US/docs/Glossary/HTML5" target="_blank"><img height="50" src="https://cdn.pixabay.com/photo/2017/08/05/11/16/logo-2582748_1280.png"></a></code>
<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank"><img height="50" src="https://cdn.pixabay.com/photo/2017/08/05/11/16/logo-2582747_1280.png"></a></code>
<code><a href="https://www.javascript.com/" target="_blank"><img height="50" src="https://cdn.freelogovectors.net/wp-content/uploads/2020/11/javascript_logo-768x873.png"></a></code>
<code><a href="https://getbootstrap.com/" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/getbootstrap/getbootstrap-ar21.svg"></a></code>
<code><a href="https://www.mysql.com/" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/mysql/mysql-ar21.svg"></a></code>
<code><a href="https://aws.amazon.com/" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/amazon_aws/amazon_aws-ar21.svg"></a></code>

<p align="center"> Python |  Flask |  HTML | CSS | JavaScript | BootStrap | MySQL | AWS </p>

## 🎛️ Version Control Tools

 <p align="center">
<img src="https://i.giphy.com/media/KzJkzjggfGN5Py6nkT/200.webp" width="150"><img src="https://i.giphy.com/media/IdyAQJVN2kVPNUrojM/200.webp" width="150"> <img src="https://media.giphy.com/media/UWt0rhp21JgLwoeFQP/giphy.gif" width ="150"/> <img src="https://media.giphy.com/media/kH6CqYiquZawmU1HI6/giphy.gif" width ="150"/> 
</p>

## 🧰 Tools

&emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;![ezgif com-optimize](https://user-images.githubusercontent.com/32817064/140445992-15af5890-6aa5-48e5-b663-7e6bd1272d26.gif)

### Third-Party Tools

- [AWS Relational Database Service-RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
  - The AWS Database is used as a primary DB by the location. The application interacts with the DB and no additional steps are required from the users. For any contributors or future developers, please mail to wolftrackse@gmail.com to get your AWS IAM user account details to connect to AWS RDS.
- [Microsft Power BI](https://docs.microsoft.com/en-us/power-bi/)
- [Highcharts](https://www.highcharts.com/)

---

## 💻 Getting Started & Installation:

- ### Prerequisite:

  - Download [Python3.x](https://www.python.org/downloads/).

- ### Installation:

  E.g If you downloaded `Python 3.8.7` above, then

  **Steps to setup virtual environment**

  - Create a virtual environment:

    `python3.8 -m venv test_env`

  - Activate the virtual environment:

    `source test_env/bin/activate`

  - Build the virtual environment:(must be present in [project root directory]

    `pip install -r requirements.txt`

- ### Run Instructions

  **To run/test the site locally:**

  - Clone 

  - Navigate to [project directory]

  - Run `python main.py` or `python3 main.py` <br> <br>
    If there is a certificate error coming up for nltk stopwords download: <br>

    - search for "Install Certificates.command" in finder and open it. Its a script that will install required Certificates. <br>
    - Run the above command again.

  - Site will be hosted at:
    `http://127.0.0.1:5000/`

- ### Application Deployed on a sandbox server
  - You can access the application on the url
    `https://harshb.pythonanywhere.com/login`

## 🚢 Run locally using Docker

Our application is docker-compatible configured and you have to follow below steps to run the docker on local:<br>
Note : Make sure you have a docker desktop or docker client installed on your system

- [Docker Desktop Installation Guide](https://docs.docker.com/get-docker/)

1. Clone the repository

```
git clone https://github.com/nehajaideep/WolfTrack3.0.git
```

2. Go the the repository

```
cd WolfTrack3.0
```

3. Run the docker build command

```
docker build --tag wolftrackv3:1.0 .
```

4. Run the built docker image on local Container

```
docker run -dp 5000:5000 wolftrackv3:1.0
```

5. Test the backend application using below api

```
GET localhost:5000/login
Response :- "Login Page will appear"
```

6. Tag the Deployable image

```
docker tag wolftrackv2:1.4 akhil/wolftrackv3:1.0
```

7. Push the Deployable tagged image to the DockerHub Cloud Image Repository

```
docker push akhil/wolftrackv3:1.0
```

8. Below DockerHub Repository where the readily deployable Image is available
   <img width="1389" alt="Screenshot 2021-11-04 at 9 38 50 PM" src="https://user-images.githubusercontent.com/32817064/140444016-f26825a8-6fb6-4345-ab6a-54986163ede5.png">

---



---



## 🛤️ Roadmap

### Phase 1 WolfTrack:

- [x] Create database ER diagram
- [x] Create SQL DML and DDL queries
- [x] Create Dashboard Page
- [x] Create Login Page
- [x] Create Signup Page
- [x] Setup Flask
- [x] Add Unit testing
- [x] Add Error Handling mechanisms
- [x] Mock of Job Application Map using Power BI

### Phase 2 WolfTrack 2.0:

- [x] Resume Parser and Analyzer
- [x] Email Notifcation after adding new job profile to list
- [x] Upload and maintaining resume versions
- [x] Send remainder mails for deadlines
- [x] Share your profile with others
- [x] Creation of Docker image
- [x] Readily deployable image in docker registry

### 🏁 Phase 3 WolfTrack 3.0:

- [x] Two Type Login Application - Admin and User.<br>
- [x] Resume Review, Comment, Download and Like by Admin.  
- [x] Comments given by Admin are sent as email to the user. <br>
- [x] Cronjob for pending application deadlines as email notification. <br>
- [x] Implemented web scraping to find relevant jobs according to user's profile and recommend him <br>
- [x] Daily Goal Check to keep track of number of jobs applied and to apply <br>
- [x] Customizable Daily Target Field <br>
- [x] Parse Resume Document with other extensions <br>
- [x] Recommend jobs by matching the resume with open jobs <br>

### 🔭 Phase 4 WolfTrack 4.0 (Future Scope):

- [x] Configure Cron-Job for reminder as SMS notification
- [x] Model improvement of resume analyzer
- [x] Customization of job recommendations
- [x] Direct application links to jobs in the recommendation list
- [x] Online chat with expert
- [x] Resume template editor

---

---
