# DevSearch

Created a application which can be used by the Developers to upload their profiles and show their skills and projects they worked on. There are two main parts of the application.

```
  1). Developers can Upload their profiles with the projects and skills.
  2). Employers can watch their profiles and projects they worked on and can communicate with them with messages.
```

## Download Python and pgAdmin 4

  &emsp; 1). Download and setup Python from <a href="https://www.python.org/downloads/" target="_blank">here</a>.<br/>
  &emsp; 2). Download pgAdmin 4 which used to setup Postgresql DB from <a href="https://www.pgadmin.org/download/" target="_blank">here</a>.<br/>
  &emsp; 3). Download Postgresql from <a href="https://www.postgresql.org/download/" target="_blank">here</a>.
  
## Setup AWS Account with RDS and S3 bucket

### Setup AWS Account

  &emsp; 1). You need to setup AWS Account to upload developer profile images and project title images to AWS S3 bucket and to connect DB with AWS RDS. Check tutorial to setup AWS root account from <a href="https://www.youtube.com/watch?v=FRQ9fE4fd5g" target="_blank">here</a>.</br>
  &emsp; 2). Setup IAM User with the help of <a href="https://www.youtube.com/watch?v=wRzzBb18qUw" target="_blank">this </a>tutorial.</br>
  &emsp; 3). When Setting up IAM user permission attach policy named ```AmazonS3FullAccess``` as well.

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
    - Create or Select Security group which has inbound rules Type HTTP and source from 0.0.0.0/0
    - Select Additional Configuration according to your usage of DB.
```

### Setup S3 bucket on AWS

  &emsp; Search S3 and create S3 bucket. <br/>
  &emsp; Follow the steps and uncheck Block all public access.<br/>
  &emsp; Create S3 bucket. <br/>
  &emsp; After Successfully creating S3 bucket, go to permissions -> Edit Bucket policy.
  
  ```
    Add Following bucket policy and Save Changes.
    
    {
      "Version": "2012-10-17",
      "Id": "devsearch-project-policy",
      "Statement": [
        {
            "Sid": "devsearch-project-statement-id",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::devsearch-project-bucket/*"
        }
      ]
    }
    
  ```
  
## Setup PostgreSQL server

  &emsp; 1). Open pgAdmin 4 and Register new Server into Servers group.
  &emsp; 2). Give name to the Server and go to Connection.
  ```
      Information in Connection.
      
      - Host name/address -> Go to RDS and Copy the Endpoint of Database that we created.
      - Username          -> (AWS Database username)
      - password          -> (AWS Database password)
  ```
  &emsp; 3). Create a Database in Server with the name of your choice.
  
## Clone the Repo and Setup Environment Variables

  &emsp; 1). Open Terminal and Install virtual environment with ```pip install virtualenv``` or ``` pip3 install virtualenv``` or ```python3 -n pip install virtualenv```.<br/>
  &emsp; 2). Clone the Repo.<br/>
  &emsp; 3). cd to the root directory of the repo.
  &emsp; 4). Start Virtual environment with ```virtualenv venv``` and then ```source venv/bin/activate```.
  &emsp; 5). After that cd to the Folder DevSearch with the command ```cd DevSearch/DevSearch```.
  
### Setup Environment Variables

  &emsp; Create file ```.env```
  &emsp; Go to .env file and write below variables.
  
  ```
     SECRET_KEY=(any string you like to enter)
     EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
     EMAIL_HOST=smtp.gmail.com
     EMAIL_PORT=465
     EMAIL_USER=(your email address)
     EMAIL_PASSWORD=(your email password)
     DB_NAME=(name of your database in pgAdmin 4 Server)
     DB_USER=(username on AWS Database)
     DB_PASSWORD=(AWS Database Password)
     DB_HOST=(AWS Database Endpoint)
     DB_PORT=5432
     AWS_ACCESS_KEY_ID=(Your AWS IAM user Access key)
     AWS_SECRET_ACCESS_KEY=(Your AWS IAM user secret key)
     AWS_STORAGE_BUCKET_NAME=(Name of the S3 bucket)
     AWS_S3_REGION_NAME=(Name of your S3 bucket region)
  ```

## Instruction to Run Local Application

Go to the Root Folder of the Project where ```manage.py``` and ```requirements.txt``` files are located.
<ul><li>Run following Commands to run your application locally.</li></ul>
```
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
```

This will run your application on this URL: http://127.0.0.1:8000/
