<h1 align="center">Adventure Awaits<a name="#top"></a></h1>

## Table of Contents

- [Introduction](#introduction)

- [User Experience](#ux)

  - [Wireframe](#wireframe)

- [User Stories](#user-stories)

- [Database Structure](#database-structure)

  - [Products App](#products-app)
  - [Profiles App](#profiles-app)
  - [Contact App](#contact-app)

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