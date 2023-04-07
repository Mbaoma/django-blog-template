# django-blog-template
This blog is built following [Corey Schafer's](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) Django series. 

The blog will have the following features:
- users can CREATE blogposts
- users who create blogposts can EDIT the posts
- users wjp create blogposts can DELETE their posts
- new users can SIGN IN
- existing users can LOGIN and  LOGOUT

I will 
- setup a CI/CD pipeline (using GitHub Actions) that runs the application through a series of unit tests and then deploys the application to AWS Amplify.
- populate the blog with data using Django's [Factory Boy](https://factoryboy.readthedocs.io/en/stable/orms.html) library
