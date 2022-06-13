
# Awards Application

## Author
# Isaac Kiptoo Kilimo.



## Description
This is a web application written in Django. It is a clone of AWWARDS application where users can view different posts,rate,and search other posts. The administrator is in charge of populating the database.

## User Story
1. View different posts that interest them.
2. Click a single image to expand it and view the details of that image.
3. Search for different projects.
4. Rating projects from different users.



## Behaviour Driven Development (BDD)
1. Register

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| A new user must sign up to be able to post and view other people posts and images will be displayed on user timeline  | 


1. Login

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| upon signing up successfully the user will be able to be redirected to home page where he/she be able to post and view other people posts and images | 

1. update profile

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| upon signing up successfully the user will be able to be redirected to home page where he/she be able to post and view other people posts and images,the user can also update his profile | 

1. logout

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| upon signing up ang logging in successfully the user will be able to post and view other people posts and images will be displayed on user timeline  and he can be able to logout after navigating to the dropdown | 

2. Search by post title 

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Enter a search name on the search form   | searchTerm| names that belong to that category are displayed  | 


3. Admin View

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on Admin on navigation bar | Username, Password| User is redirected to the admin page where they can manage the database  |  

4. View post

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on the copy icon on the image modal that appears after clicking on the image | copy link| The image link is copied to clipboard  |  


## Setup/Installation Requirements
1. clone repository
     
2.  Type code based on the text editor you have and work on it.   

### Database
1. Set up Database,and put your username and password in the code

2. Make migrations
    python3.8 manage.py makemigrations picture

3. Migrate
   python3.8 manage.py migrate 
    
### Running the Application
1. Run main apllication
   * python3 manage.py runserver

2. Run tests    
   * python3.6 manage.py test imagery

###
1. Creating Admin Locally
    python manage.py createsuperuser. Then set username, email & password

2. Creating Django Admin   
     heroku run python manage.py createsuperuser. Then set username, email & password

## Technologies Used
* Python3.8
* Django 4.0
* javaScript
* Bootstrap
* PostgreSQL

## License -Copyright 

MIT License

Copyright © license 2022 ,Isaac kiptoo kilimo, student Moringa school.

## Authors Info/contacts

Github Profile - [Isaac kiptoo kilimo](https://github.com/Isaac-kiptoo-kilimo)

Email Address-[Isaac kiptoo kilimo] (isaac.kiptoo.kilimo@student.moringaschool.com)

Copyright © 2022

# project layout

### Homepage
![gallaryup](./static/images/instapage.png)

### Admin 
![gallaryup](./static/images/loginpage.png)
