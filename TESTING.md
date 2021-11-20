<h1 align="center">Adventure Awaits<a name="#top"></a></h1>


## Table of Contents


- [Validators](#validator)

  - [HTML5 validator](#html-validator)
  - [CSS3 validator](#css3-validator)
  - [JS validator](#js-validator)
  - [Python validator](#py-validator)


- [Testing](#testing)

  - [Functionality Testing](#test-functionality)
  - [Responsiveness](#responsiveness)
  - [Browser compatibility](#browser-compatibility)
  - [Performance Testing](#performance-testing)


  - [User Stories](#user-stories)



<a name="validators"></a>

### Validators


<a name="html-validator"></a>

#### HTML5 validator
Vaidate by URI [HTML5 Validator](https://validator.w3.org/#validate_by_uri)
Test result : No errors beyond this which occurs in the base.html thus on all pages.

<img src="readme/testing/html_error.png" height="300px"/>



<a name="css3-validator"></a>

#### CSS3 validator
Validate by direct input [CSS Validator](https://jigsaw.w3.org/css-validator/)
Test result : No errors


<a name="js-validator"></a>

#### JS validator
Validate by direct input [JavaScript Validator](https://jshint.com/)
- Test result : No Errors


<a name="py-validator"></a>

#### Python validator
Validate by direct input [Python Validator](http://pep8online.com/)
Test result : No Error


<a name="testing"></a>

## Testing


<a name="test-functionality"></a>

### Functionality Testing

- Navigation bar
  - When the navbar links are clicked, they take the user to the revelent page.
  - Clicking on the logo takes the user to the home page.

- Subscribe link
  - Located at the bottom of each page and link works.

- Links
  - All internal and external links are tested to make sure that all pages are connected and opened.


<a name="responsiveness"></a>

### Responsiveness
- Galaxy S5 - Good
- iPhone 5/6/7/8 - Good
- iPad - Good
- iPad Pro - Good
- Desktop 1024px - Good
- Desktop >1200px - Good


<a name="browser-compatibility"></a>

### Browser compatibility
- Chrome: Responsiveness, Appearance and Functionality- Good
- Safari: Responsiveness and Appearance and Functionality- Good


<a name="performance-testing"></a>

### Performance Testing

- Test in Dev Tools Lighthouse.

   - Run a report
     - In Chrome, go to the URL you want to check.
     - Open DevTools.
     - Click on the Lighthouse tab.
     - Choose desktop or mobile, leave all categories enabled.
     - Click Generate report.

- A Lighthouse report in Chrome DevTools

    - Home page Desktop and Mobile
      <img src="readme/testing/home.jpg" height="300px"/>

    - All clothing page Desktop and Mobile
      <img src="readme/testing/all_clothing.jpg" height="300px"/>

    - Products(all) page Desktop and Mobile
      <img src="readme/testing/all_products.jpg" height="300px"/>

    - All equipment page Desktop and Mobile
      <img src="readme/testing/all_equipment.jpg" height="300px"/>

    - Contact page Desktop and Mobile
      <img src="readme/testing/contact.jpg" height="300px"/>

    - Bag page Desktop and Mobile
      <img src="readme/testing/bag.jpg" height="300px"/>

    - Checkout success Desktop and Mobile
      <img src="readme/testing/checkout-success.jpg" height="300px"/>

    - Register page Desktop and Mobile
      <img src="readme/testing/register.jpg" height="300px"/>

    - Login page Desktop and Mobile
      <img src="readme/testing/login.jpg" height="300px"/>

<a name="user-stories"></a> 

### Testing User Stories

- User

1. As a user I'd like to easily navigate around the site.
2. As a user I'd like to view a list of products.
3. As a user I'd like to search for individual products.
4. As a user I'd like to sort the products by categories.
<img src="readme/testing/navbar.png" height="300px"/>

5. As a user I'd like to view individual products.
<img src="readme/testing/individual_product.png" height="300px"/>

6. As a user I'd like to easily register.

<img src="readme/testing/register.png" height="300px"/>

7. As a registered user I'd like to easily login and logout.
<img src="readme/testing/login.png" height="300px"/>
<img src="readme/testing/logout.png" height="300px"/>

8. As a registered user I'd like to have a profile with a previous order history.

<img src="readme/testing/profile.png" height="300px"/>

9. As a user I want to select the quantity of the products when purchasing.
<img src="readme/testing/quantity.png" height="300px"/>

10. As a user I want a confirmation message that the purchase was successful.
<img src="readme/testing/order_success.png" height="300px"/>

11. As a user I want to view the products in the shopping bag before purchasing.
<img src="readme/testing/shopping_bag.png" height="300px"/>


- Site Owner

12. As the owner of the site I'd like to add new products.

<img src="readme/testing/add_product.png" height="300px"/>

13. As the owner of the site I'd like to edit/update already existing categories and products.
14. As the owner of the site I'd like to delete already existing categories and products.
<img src="readme/testing/edit_delete.png" height="300px"/>


- Back To [Readme](README.md)