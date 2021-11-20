<h1 align="center">Adventure Awaits<a name="#top"></a></h1>


## Table of Contents

- [Introduction](#introduction)

- [User Experience](#ux)

  - [Wireframe](#wireframe)

- [User Stories](#user-stories)

- [Features](#features)

- [Technologies Used](#technologies)

- [Testing](testing)

- [Deployment](deployment)

- [Known Bugs](#known-bugs)

- [Credits](#credits)

<a name="introduction"></a>

## Introduction

Adventure Awaits is a camping and hiking wear online store.
The website is designed for the business purpose of selling clothing and equipment suited for camping and hiking trips.
This is my fullstack milestone project at code institute. The goal of this project is to build a website that uses HTML, CSS, JS, Python, Django, Stripe and a relational database.
This project is deployed on Heroku and styled using bootstrap and css.
To test the functionality of the payment section of this project use the card number 4242 4242 4242 4242 or 4000 0027 6000 3184 with any CVC and expiry date.


[Click here to view the deployed project.](https://milestone4-project-daniella-m.herokuapp.com/)

<a name="ux"></a>

## User Experience (UX)

<a name="wireframe"></a>

### Wireframe
[wireframes](https://github.com/DaniellaMinyo/Milestone4/tree/main/readme/wireframes)


<a name="user-stories"></a>

## User Stories

There are 3 types of users:

1.	Admin/Superuser who can add, modify and delete products and categories.
2.	Users who have not registered but can browse and even purchase on site.
3.	Users who have registered and thus have a profile page.



Navigation and Viewing

1. As a user I'd like to easily navigate around the site.
2. As a user I'd like to view a list of products.
3. As a user I'd like to view individual products.

Management and Admin

4. As the owner of the site I'd like to add new categories and products.
5. As the owner of the site I'd like to edit/update already existing categories and products.
6. As the owner of the site I'd like to delete already existing categories and products.

Searching and Sorting

7. As a user I'd like to search for individual products.
8. As a user I'd like to sort the products by categories.

Registration and User accounts

9. As a user I'd like to easily register.
10. As a registered user I'd like to easily login and logout.
11. As a registered user I'd like to have a profile with a previous order history.

Checkout (and purchasing)

12. As a user I want to select the quantity of the products when purchasing.
13. As a user I want a confirmation message that the purchase was successful.
14. As a user I want to view the products in the shopping bag before purchasing.



<a name="features"></a>

## Features

### Existing Features

#### Features that exist across all the web pages

-  The navigatin menu features a search bar, contact link, an account dropdown menu (with (product management if admin), my profile and logout links if the user is logged in else register and sign in links), basket link, home, and product links.
- A subscibe link at the bottom of the page that takes the user to a subsciption form.
- A free delivery banner under the navbar.


#### Specific to the pages

**Home Page**

 - Some text and a shop now button which takes the user to the all products page.


**Subscribe Page**

- Contains a subscription form that requires a name and email. Upon form submission the name and email will be saved to the database.


**Products Page**

- Contains all the products/the products from the searched for category.
- A sort by dropdown menu.
- Has a to-top button.


**Contact Page**

- Contains a contact form with a name, email, subject and message fields. Upon submission the data will be saved to the database.


**Product Management Page**

-  A form where products can be added by the admin.


**My Profile Page**

-  A form with saved delivery information which can be updated.
- An order history.


**Registration Page**

- A registration form.


**Login and Logout Page**

 - The login page has a login form after filling it out and clicking the login button the user will be redirected to the home page.
  - The logout page has a logout button after clicking button the user will be redirected to the home page.


**Basket Page**

- When basket is empty a prompt and button that takes the user to the prompts page.
- When there is something in the bag, it contains the items to be purchased, the bag total, delivery charge and buttons to keep shopping or go to checkout.


**Checkout Page**

- Contains details, delivery (delivery information can be saved) and payment details form.
- An order summary with your grand total.
- An adjust bag and complete order button.


**Checkout Success Page**

- A confirmation email will be sent to the given email address.
- A confirmation page will appear with all your order information.
- A button that redirects the user to the all products page.


<a name="technologies"></a>

## Technologies Used

-   [GitHub](https://github.com/)
-   [Gitpod](https://www.gitpod.io/)
-   [Heroku](https://www.heroku.com/)
-   [HTML5](https://www.w3schools.com/html/)
-   [CSS3](https://www.w3schools.com/css/)
-   [Bootstrap](https://getbootstrap.com/)
-   [JS](https://www.w3schools.com/js/DEFAULT.asp)
-   [jQuery](https://jquery.com/)
-   [Python](https://www.python.org/)
-   [Django](https://www.djangoproject.com/)
-   [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
-   [PostgresSQL](https://www.heroku.com/postgres)
-   [Psycopg2](https://pypi.org/project/psycopg2/)
-   [Gunicorn](https://gunicorn.org/)
-   [SQLite](https://docs.djangoproject.com/en/3.1/ref/databases/#sqlite-notes)
-   [Stripe](https://stripe.com/ie)
-   [AWS S3 Bucket](https://aws.amazon.com/s3/)
-   [FontAwesome](https://fontawesome.com/)


<a name="testing"></a>

## Testing
[find here](https://github.com/DaniellaMinyo/Milestone4/blob/main/TESTING.md)


<a name="deployment"></a>

## Deployment

### Local Deployment

- To create this project the [Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used to create a new repository. Then in my new repository on GitHub, I clicked the Gitpod button which built my workspace.

To clone:
  - When your workspace is built:
    Install:
    pip3
    Python3
  - Create an account with Stripe.
  - Using an email provider, sign in and navigate to the account security page page. Create a two-step authentication. Using the same email values, set up your email username and password below:
	- Click on the "clone or download button" at the top of this repo.
	- Clone the project using HTTPS or an SSH key:
    - HTTPS: click on the checklist icon
    - SSH key: first click on 'Use SSH' then click on the same icon as above
  - Return to your workspace and open a new Terminal window.
  - Change the current working directory to the location where you want the cloned directory.
  - Enter: git clone https://github.com/DaniellaMinyo/Milestone4.git
  - Install the required dependencies with: pip3 install -r requirements.txt
  - Create an ```env.py ```file and add the following, complete with your own values:
    ```
    import os
    os.environ['DATABASE_URL'] = '<your Heroku Postgres database url>'
    os.environ['EMAIL_HOST_PASS'] = '<your value>'
    os.environ['EMAIL_HOST_USER'] = '<your value>'
    os.environ['SECRET_KEY'] = '<your value>'
    os.environ['STRIPE_PUBLIC_KEY'] = '<your value>'
    os.environ['STRIPE_SECRET_KEY'] = '<your value>'
    os.environ['STRIPE_WH_SECRET'] = '<your value>'
    os.environ['DEVELOPMENT'] = 'True'
    ```
  - Add your ```env.py``` file to .gitignore.
  - Set up the Django SQLite3 tables:
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
  - Create a superuser for your project:
    ```
    python3 manage.py createsuperuser
    ```
  - Run cloned repo:
    ```
    python3 manage.py runserver
    ```

### Heroku Deployment
To deploy and host on [Heroku](https://www.heroku.com/).
- Go to [Heroku](https://www.heroku.com/) and login.
- Click on the 'New' button and select 'Create new app'.
- Enter the app name and select a region.
- Click 'Resources' than 'Add-ons' than click 'Heroku Postgres' and Select Hobby Dev plan to use the Postgres database for deployment.
- Freeze the requirements.txt file : pip3 freeze --local > requirements.txt
- In your env.py file:
  ``` 
  os.environ['DATABASE_URL'] = '<your Heroku Postgres database url>'
  ```
- Set up the Postgres database:
  ```
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```
- Import product data:
  ```
  python3 manage.py loaddata categories
  python3 manage.py loaddata products
  ```
- Create a new superuser for deploying on Heroku:
  ```
  python3 manage.py createsuperuser
  ``` 
- Create a Procfile:
  ```
  web: gunicorn xtreme_fitness.wsgi:application
  ```
- In your terminal:
  ```
  heroku login 
  heroku config:set DISABLE_COLLECTSTATIC=1 --app Milestone4
  ```
- In settings.py.
  ```
  ALLOWED_HOSTS = ['Milestone4.herokuapp.com', 'localhost']
  ```
- Add and commit your changes:
  ```
  git add .
  git commit -m "commit message"
  git push (gitHub push)
  git push heroku master
  ```
- Click the Deploy tab (on heroku) and set deployment method to connect to GitHub and search for your repo and click to connect. Enable Automatic Deploys.
- In 'Settings', click on the 'Reveal Config Variables' and add:

| **Key** | **Value** |
--- | ---
 DATABASE_URL | Heroku Postgres database url
 EMAIL_HOST_PASS | password for your email account
 EMAIL_HOST_USER | email address
 SECRET_KEY | secret key for Django project, use [Secret Key Genarator](https://miniwebtool.com/django-secret-key-generator/))
 STRIPE_PUBLIC_KEY | from Stripe account
 STRIPE_SECRET_KEY | from your Stripe account
 STRIPE_WH_SECRET | from your Stripe account


### AWS Bucket

For this project to be successfuly deployed on heroku you need to use a service like AWS S3 for the storage of static files.

1. Create an account on [AWS S3 Bucket](https://aws.amazon.com/s3/). 
2. Go to [AWS S3 Bucket](https://aws.amazon.com/s3/) and sign-in. 
3. In the AWS Managnemt Console search for S3.
4. Create a bucket with your heroku app name, choose the region closest to you and uncheck block all public access. Click Create bucket.
5. Click on the properties tab in bucket. 
6. Find the static website hosting option and click on edit.
7. Turn on Static Website Hosting. Add index.html to the index document field and error.html to the error document field. Save the changes. 
8. Click on permissions tab and find the CORS option and click Edit.
9. Click on Bucket Policy, select policy generator and create a security policy.
 - Policy type : S3 Bucket Policy
 - Principal:  *
 - Action: Get Object
 - Amazon Resorce Name(ARN): <ARN name > (find it in the bucket policy tab).
 - Add statement than click Generate Policy.
 - Copy the policy into Bucket policy editor.
 - Add ( /* ) to the end of Resource key.
10. Find the Access Control List option and click edit.
 - On Everyone check list object permission and save.

11. In the Services menu, find IAM.
 - Click on Groups and create a new group.
 - Click on Policy, than on Create Policy, choose the Json tab and click on import manage policy. 
 - Find the S3, choose AmazonS3FullAccess and import.
 - Click on Review policy, give it a name and description and create policy.
 - Go to Groups, click your group and click the attach policy button. Find the policy you created, select it  and click attach policy.
 - Click on users then add users.
 - Create a user and access type: Programatic Access.
 - In add user to group section, check your group name, click next and click on Create User. 
 - Download zip file containing ID and KEY.
12. In Gitpod in the settings.py, change the AWS_STORAGE_BUCKET_NAME to bucket name, the AWS_S3_REGION_NAME to your region.
13. On Heroku go to Settings, click Config Vars, add your AWS keys to the config variables, add USE_AWS and set to true. Remove DISABLE_COLLECTSTATIC.

| **Key** | **Value** |
--- | ---
 AWS_ACCESS_KEY_ID | AWS bucket ID
 AWS_SECRET_ACCESS_KEY | AWS secret key
 DATABASE_URL | Heroku Postgres database url
 EMAIL_HOST_PASS | password for your email account
 EMAIL_HOST_USER | email address
 SECRET_KEY | secret key used for your Django project 
 STRIPE_PUBLIC_KEY | from your Stripe account
 STRIPE_SECRET_KEY | from through your Stripe account
 STRIPE_WH_SECRET | from through your Stripe account
 USE_AWS | True


<a name="known-bugs"></a>

## Known Bugs


<a name="credits"></a> 

## Credits

### Code

- This project was very heavily influenced by the [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) mini-project from the code institute course.
- [Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/) was used for the responsive design.

### Content

- I was inspired by:
  - [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1)
  - [Cabelas](https://www.cabelas.com/shop/en#/)

- Product Content (name and info)
  - [Cabelas](https://www.cabelas.com/shop/en#/)

### Media

- Images and icons from
  - [cabelas](https://www.cabelas.com/shop/en#/)
  - [font awesome](https://fontawesome.com/)

### Acknowledgements

- To [Code Institute](https://codeinstitute.net/).
