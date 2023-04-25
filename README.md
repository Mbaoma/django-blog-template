# django-blog-template
This blog is built following [Corey Schafer's](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) Django series. 

## Features
- users can CREATE blogposts
- users who create blogposts can EDIT the posts
- users who create blogposts can DELETE their posts
- new users can SIGN IN
- existing users can LOGIN and LOGOUT 
- existing users can CHANGE their password
- users can OVERWRITE their existing passwords using the 'forgot password' feature

## Goal 
- To setup a CI/CD pipeline that runs the application through a series of unit tests and then deploys the application (blog) to Azure App Services.

## Setting Up
- Create a virtual environment.
```bash
python -m venv venv
```

-  Install requirements
```
pip install -r requirements.txt
```

- Run the app
```bash
cd tutorial
python manage.py runserver
```

<img width="1246" alt="image" src="https://user-images.githubusercontent.com/49791498/233818747-0aba2856-3e98-4f33-9f70-f1c7c7aff164.png">
*localhost*

- To  run tests,
```bash
python manage.py test ./blog 
python manage.py test ./account
```

- To setup a password that enables less secure apps (Django), send mails to your Gmail (for reset password/ forgot password functionality), first follow [this](https://support.google.com/accounts/answer/185833?hl=en) guide.

- To Dockerize the app
```bash
$ docker login
$ docker build -t  dockerhub-username/docker-image-name .
$ docker push dockerhub-username/docker-image-name
```

- Run the dockerized app
```bash
docker compose up
```