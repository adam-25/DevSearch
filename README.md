# DevSearch

> Created a web application which can be used by the Developers to upload their profiles and show their skills and projects they worked on. There are two main parts of the application.

```
  1. Developers can Upload their profiles with the projects and skills.
  2. Employers can watch their profiles and projects they worked on and can communicate with them through messages.
```

## Download Python and pgAdmin 4

<ol>
  <li>Download and setup Python from <a href="https://www.python.org/downloads/" target="_blank">here</a>. </li>
  <li>Download pgAdmin 4 which used to setup Postgresql DB from <a href="https://www.pgadmin.org/download/" target="_blank">here</a>. </li>
  <li>Download Postgresql from <a href="https://www.postgresql.org/download/" target="_blank">here</a>. </li>
</ol>
  
## Setup AWS Account with RDS an S3 bucket

### Setup AWS Account

<ul>
  <li>You need to setup AWS Account to upload developer profile images and project title images to AWS S3 bucket and to connect DB with AWS RDS. Check tutorial to setup AWS root account from <a href="https://www.youtube.com/watch?v=FRQ9fE4fd5g" target="_blank">here</a>.</li>
  <li>Setup IAM User with the help of <a href="https://www.youtube.com/watch?v=wRzzBb18qUw" target="_blank">this </a>tutorial.</li>
  <li><b>When Setting up IAM user permission attach policy named "AmazonS3FullAccess" as well.</b></li>
</ul>

### Setup RDS Database on AWS

```
  Search RDS and Create Database.
  
  Steps to Setup Database.
  
    - Choose a database creation method -> Standard create
    - Engine options                    -> PostgreSQL
    - Templates                         -> Free tier
    - Master username                   -> (username you want to set)
    - password                          -> (password you want to set)
    - Instance                          -> db.t3.micro
    - Public access                     -> Yes
    - Create or Select Security group which has inbound rules Type HTTP, HTTPS and source from 0.0.0.0/0
    - Select Additional Configuration according to your usage of DB.
```

### Setup S3 bucket on AWS

<ul>
  <li>Search S3 and create it on AWS.</li>
  <li>Follow the steps and uncheck Block all public access.</li>
  <li>Create S3 bucket.</li>
  <li>After Successfully creating S3 bucket, go to permissions -> Edit Bucket policy.</li>
  <li>After that add Images folder into static folder to AWS S3 bucket to get better experience.</li>
</ul>
  
  ```
    Add following bucket policy and Save Changes.
    
    {
      "Version": "2012-10-17",
      "Id": "devsearch-project-policy",
      "Statement": [
        {
            "Sid": "devsearch-project-statement-id",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::${name_of_your_bucket}/*"
        }
      ]
    }
    
  ```
  
## Setup PostgreSQL server

<ol>
 <li>Open pgAdmin 4 and Register new Server into Servers group. </li>
 <li>Give name to the Server and go to Connection. </li>

#### Information in Connection.
| Label | Value |
| --- | --- |
| Host name/address | Go to RDS Database that we created and copy the EndPoint and Paste it here. |
| Username | (AWS Database username) |
| password | (AWS Database password) |

  
  <li>Create a Database in Server with the name of your choice. </li>
</ol>

## Clone the Repo and Setup Environment Variables

<ol>
  <li>Open Terminal and Install virtual environment with "pip install virtualenv" or "pip3 install virtualenv" or "python3 -n pip install virtualenv".</li>
  <li>Clone the Repo.</li>
  <li>cd to the root directory of the repo.</li>
  <li>Start Virtual environment with "virtualenv venv" and then activate it with command "source venv/bin/activate".</li>
  <li>After that cd to the Folder DevSearch with the command "cd DevSearch/DevSearch".</li>

</ol>

### Setup Environment Variables

<ol>
  <li>Create file ".env" </li>
  <li>Go to .env file and write below variables. </li>
</ol>

| Variable Name | Value |
| --- | --- |
| SECRET_KEY | (any string you like to enter) |
| EMAIL_BACKEND | django.core.mail.backends.smtp.EmailBackend |
| EMAIL_HOST | smtp.gmail.com |
| EMAIL_PORT | 465 |
| EMAIL_USER | (your email address) |
| EMAIL_PASSWORD | (your email password) |
| DB_NAME | (name of your database in pgAdmin 4 Server) |
| DB_USER | (username on AWS Database) |
| DB_PASSWORD | (AWS Database Password) |
| DB_HOST | (AWS Database Endpoint) |
| DB_PORT | 5432 |
| AWS_ACCESS_KEY_ID | (Your AWS IAM user Access key) |
| AWS_SECRET_ACCESS_KEY | (Your AWS IAM user secret key) |
| AWS_STORAGE_BUCKET_NAME | (Name of the S3 bucket) |
| AWS_S3_REGION_NAME | (Name of your S3 bucket region) |

## Instruction to run local Application

&emsp;  1. Go to the Root Folder of the Project where ```manage.py``` and ```requirements.txt``` files are located.<br/>
&emsp;  2. Run following Commands to run your application locally.

```bash
  pip install -r requirements.txt  # This command will install all the required packages for project.
  
  python manage.py makemigrations  # This command will package all models into individual migration files.
  
  python manage.py migrate         # This command will apply all migration files to DB.
  
  python manage.py runserver       # This will start developement server locally.
```

**This will run your application on this URL: http://127.0.0.1:8000/**
