# SLurp Ramen

![Am I Responsive Screenshot](static/images/screenshots/am-i-responsive.png)

## Table of Contents

* [**Planning Phase**](#planning)
  * [**Strategy**](#strategy)
      * [**Site Aims**](#site-aims)
      * [**Visitor Goals**](#visitor-goals)
  * [**Agile Methodologies**]
    * [**User Stories**](#user-stories)
  * [**Design**](#design)
  * [**Ecommerce Business Model**]
  * [**Wireframes**](#wireframes)
  * [**SEO Considerations**](#seo-considerations)

* [**Features**](#features)
  * [**Apps**](#apps)
  * [**Future Features**](#future-features)

* [**Testing**](#testing)
  * [**Bugs**](#bugs)
  * [**Automated Testing**](#automated-testing)
  * [**Manual Testing**](#manual-testing)
  * [**Code Validation**](#code-validation)
    * [**Jigsaw**](#jigsaw)
    * [**Flake8 Python**](#python Testing)
    * [**W3C HTML**](#w3c-html)
    * [**Lighthouse**](#lighthouse)

* [**Deployment**](#deployment)
  * [**Create a databse**](#create-a-database)


# Planning

## Strategy

### Site Aims

- Provide a user-friendly and effient online ordering system for customers to easily browse the menu, add food to a cart, and complete secure payments.
- Enable customers to book a table for dining in, ensuring availability and a smooth reservation experience. 
- Offer a simple and accessible way for customers to contact the restaurant, wheather for inquiries, reservations, or feedback.
- Ensure the website has distinct branding.
- Ensure the website is fully responsive and optimized for mobile users, allowing customers to access and interact with the site seamlessly on any device.
- To integrate Strip for secure and reliable payment processing of online orders.
- Implement SEO strategies to improve the sites visibility on search engines and attract local customers searching for ramen or Japanese food in Dublin.
- Provide an efficent backend system for restaurant owners to efficiently manage orders, reservations, communications, and customer and user data.

### Visitor Goals

- To easily browse options in the menu, add them to a cart, and place an order for delivery.
- To book a table for dining in.
- To get in touch with the restaurant for information relating to the website.
- To sign up for a newsletter to keep up to date with any changes relevant to the restaurant.
- To have feedback on the website when an action has been successul or unsuccessful.

## Agile Methodology

In this project, I adopted a streamlined agile approach using GitHubs issue tracking and project board features. Each task was defined as an issue, with clear acceptance criteria that outlined the expected outcomes for successful complettion. These criteris served as a guide to ensure each feature or fix met the requirements before being moved to the next stage.

The tasks were through various stages on the board, From "To Do" to "In Progress" and ultimately to "Completed" once the acceptance criteria were met.
This ensured a transparent, efficient worflow, with task being cheked and validated against the criteria before being marked as finished.

![Checkout Page Wireframe](static/images/screenshots/agile-method.png)

### User Stories

### User

- As a user I want to view a detailed menu so I can choose the items I want to order.
- As a user I want to add menu items to a shopping cart so I can keep track of my order.
- As a user I want to review my order so I can see the total price before proceeding.
- As a user I want to securely pay for my order online so my information is protected.
- As a user receive confirmation of my successful payment so I know my order has been processed.
- As a user I want to receive email confirmation of my order so I have proof of my purchase.
- As a user I want a user-friendly interface so I can easily navigate the website and order food.
- As a user I want to sign up for a newsletter so I can stay updated with promotions and information.
- As a user I want to create an account so I can place orders and view my past orders.
- As a user I want to log in to my account so I dont have to re-enter my information every time I order.
- As a user I want to log out of my account so I can secure my session.


### Admin

- As an admin I want to be able to add, edit, and remove menu items from admin panel so our information is up to date and correct.
- As an admin I wan to restrict access to certain management functions so only authorized users can perform these actions.

### Developer

- As a developer, I want to ensure that I use defensive programming so users cannot break the site.
- As a developer, i want to ensure users with correct credentials can access correct information.

## Design

#### Fonts

For this site I used the Noto Serif and Noto Sans Google fonts. When paired these two fonts create a balance between tradition and modernity. Noto Serif adds an authentic feel that reflects the rich history of Japanese ramen, while Noto Sans ensure readability and a clean, contemporary user experience.

#### Color

For this site I wanted I wanted to choose colors that use colors that create cohesive design. These colors are below.

-  #1C1C1C - Deep black to provide contact and depth, used for most text.
- #B71C1C - Rich red to adds bold accent to draw attention and create energy.
- #A3B763 - A muted green, creates a freshness and softens overall look.
- #FAF9F6 - Off white offers a clean neatural backdrop to increase readability.

![Color Palette](static/images/screenshots/color-palette.png)

## Wireframes

### Home Page

![Home Page Wireframe](static/images/screenshots/home-wireframe.png)

### Menu Page

![Menu Page Wireframe](static/images/screenshots/menu-wireframe.png)

### Menu Detail

![Menu Detail Page Wireframe](static/images/screenshots/menu-detail-wireframe.png)

### Booking Page

![Booking Page Wireframe](static/images/screenshots/booking-wireframe.png)

### Checkout 

![Checkout Page Wireframe](static/images/screenshots/checkout-wireframe.png)

## E-Commerce Business Model

Implementing an e-commerce platform for the restaurant provides a seamless, efficent way for customers to browse the menu, place orders for delivery, or reserve tables for dining in. By offering an online ordering system, the restaurant expands its reach, allowing customers to conveniently place orders anytime, without the need for direct interaction or phone calls. This not only increases sales potential but also provides valuable customer data that can be used for targeted marketing through our newsletter, and improving customer experience.
Additionally, integrating secure payment processing and booking systems enhances customer trust and satisfaction, making the restaurant more accessible and competitive in the digital age. The ecommerce website not only drives revenue but also establishes the restaurants presence in the local online market, attracting new customers while retaining loyal ones.

## Seo Considerations

To optimize my website for search engines, I strategically incorporated relevant keywords into the sites metadata and image attributes. In the head section of my HTML, I included a <meta name="keywords"> tag populated with the key phrases related to ramen in Dublin, such as "best ramen Dublin", "authentic Japanese Ramen", and "ramen Delivery Dublin". Additionally, I enhanced image accessibility and SEO  by descriptive alt attributes to <img> tags, ensuring that search engines can better understand the contact of my images. These alt texts include keywords such as "best ramen in Dublin", and "Ramen Delivery Dublin", which helps improve visibility in image searches while maintaining usability for visually impaired users. 

# Features

## Apps

### Home

The home app is for rendering the main landing page of the website. The page serves as a first impression and a central navigation point to explore the rest of the site.

### Menu

The menu app handles the display and management of menu items for the restaurant. The menu view retrieves all menu items from the database and categorizes them into sections such as Most Popular, Starters, Sides, Mains and Soft Drinks, ensuring a well organised presentation of the menu page.

For administrative users, the app provides additional functionality to manage the menu. The add_menu_item view allows superusers to add new dishes through a form, while the edit_menu_item view enables modifications to existing items. The delete_menu_item view allows for the removal of menu items when necessary. These admin-onlyviews ensure that the menu remains up to date, offering an easy way to make changes via the Django admin panel.

#### Menu App Database Schema

##### MenuItem Model

| Field Name      | Data Type         | Description                                 |
|-----------------|-------------------|---------------------------------------------|
| `id`            | Integer           | Primary key, auto-incremented               |
| `category`      | ManyToManyField   | Links to multiple `Category` objects        |
| `name`          | CharField         | Name of the menu item (max length 254)      |
| `description`   | TextField         | Detailed description of the menu item       |
| `price`         | DecimalField      | Price of the menu item (max 6 digits, 2 decimal places) |
| `image`         | ImageField        | Image representing the menu item (nullable) |
| `image_url`     | URLField          | URL of the image representing the menu item (nullable) |

##### Category Model

| Field Name      | Data Type         | Description                                 |
|-----------------|-------------------|---------------------------------------------|
| `id`            | Integer           | Primary key, auto-incremented               |
| `category`      | ManyToManyField   | Links to multiple `Category` objects        |
| `name`          | CharField         | Name of the menu item (max length 254)      |
| `description`   | TextField         | Detailed description of the menu item       |
| `price`         | DecimalField      | Price of the menu item (max 6 digits, 2 decimal places) |
| `image`         | ImageField        | Image representing the menu item (nullable) |
| `image_url`     | URLField          | URL of the image representing the menu item (nullable) |

### Bag

The bag app manages the users shopping cart by allowing items to added, updated, or removed. It uses Django sessions to store cart data, ensuring that selections persist across page reloads. The app includes views for viewing the cart, adding items with specified quantities, adjusting item quantities, and removing items. Additionally, it calculates, the total cost, item count, and delivery charges, making this information available via the bag. The data is passed as context, making it accessible throughout the site, ensuriung a consistent and dynamic user experience for the cart and checkout process.


### Checkout

The checkout app handles the stripe payment processing and order creation once a user proceeds with their purchase. It integrates with Stripe's webhook system to manage payment statuses and store orders in the database. The app listens for incoming Stripe webhooks, processes events like payment_itent.succeeded and payment_intent.payment failed, and then takes actions accordingly, such as creating an order, saving customer information, and sending confirmation emails. It ensures that orders are properly recorded and that customers recieve order confirmations after a successful payment.

#### Checkout App Database Schema

##### Order Model

| Field Name        | Data Type                       | Description                                                                   |
|-------------------|---------------------------------|-------------------------------------------------------------------------------|
| `order_number`    | `CharField` (max_length=32)     | Unique order number (automatically generated via UUID).                      |
| `user_account`    | `ForeignKey` (UserAccount)      | Foreign key to the `UserAccount` model representing the user who placed the order. |
| `full_name`       | `CharField` (max_length=50)     | Full name of the person making the order.                                     |
| `email`           | `EmailField` (max_length=254)   | Email address of the person making the order.                                |
| `phone_number`    | `CharField` (max_length=20)     | Phone number of the person making the order.                                  |
| `country`         | `CountryField`                  | The country of the customer (uses `django_countries`).                       |
| `postcode`        | `CharField` (max_length=20)     | Postcode of the customer (optional).                                         |
| `town_or_city`    | `CharField` (max_length=40)     | Town or city of the customer.                                                 |
| `street_address1` | `CharField` (max_length=80)     | Primary street address of the customer.                                       |
| `street_address2` | `CharField` (max_length=80)     | Secondary street address of the customer (optional).                          |
| `county`          | `CharField` (max_length=80)     | County of the customer (optional).                                            |
| `date`            | `DateTimeField`                  | Date and time the order was created.                                          |
| `delivery_cost`   | `DecimalField` (max_digits=6, decimal_places=2) | Delivery cost for the order.                                                  |
| `order_total`     | `DecimalField` (max_digits=10, decimal_places=2) | Total cost of the order before delivery.                                      |
| `grand_total`     | `DecimalField` (max_digits=10, decimal_places=2) | Grand total cost of the order including delivery.                             |
| `original_bag`    | `TextField`                     | Original cart data in text format (used for order reconstruction).            |
| `stripe_pid`      | `CharField` (max_length=254)    | Stripe payment intent ID for the order.                                       |                        |

##### OrderLineItem Model

| Field Name        | Data Type                       | Description                                                                   |
|-------------------|---------------------------------|-------------------------------------------------------------------------------|
| `order`           | `ForeignKey` (Order)            | Foreign key to the `Order` model.                                             |
| `menu_item`       | `ForeignKey` (MenuItem)         | Foreign key to the `MenuItem` model for the item being ordered.               |
| `quantity`        | `IntegerField`                  | The quantity of the item in the order.                                        |
| `lineitem_total`  | `DecimalField` (max_digits=6, decimal_places=2) | Total cost of the line item (calculated as `menu_item.price * quantity`). |


### Bookings

The bookings app allows customers to make reservations for dining at the restaurant. It uses a form to collect customer details, including name, email,number of people, reservation date, and special requests. When the form is submitted, the app validates the data and creates a booking entry. Upon successful booking, a confirmation email is sent to the customer with the reservation details. The app also displays success message to inform the user that their booking has been confirmed.

#### Bookings App Database Schema

##### Booking Model

| Field Name         | Data Type                       | Description                                                                   |
|--------------------|---------------------------------|-------------------------------------------------------------------------------|
| `name`             | `CharField` (max_length=100)    | Name of the person making the booking.                                        |
| `email`            | `EmailField`                    | Email address of the person making the booking.                               |
| `phone_number`     | `CharField` (max_length=15)     | Phone number of the person making the booking.                                |
| `number_of_people` | `IntegerField`                  | Number of people for the booking.                                             |
| `reservation_date` | `DateTimeField`                 | The date and time of the reservation.                                          |
| `special_requests` | `TextField`                     | Any special requests made by the person (optional).                           |
| `status`           | `CharField` (max_length=20)     | Status of the booking, with choices: `pending`, `confirmed`, `cancelled` (defaults to `pending`). |
| `created_at`       | `DateTimeField`                 | The date and time the booking was created.                                    |


### Contact

The contact app enables users to send inquires or feedback to the restaurant through a contact form. The form collects the users name, email, and message. When the form is submitted, the app validates the data, sends the message via email to a specified email address, and stores the data in the database for future reference. Upon successful submission, a success message is displayed to the user, informing them that their message has been sent.

#### Contact App Database Schema

##### ContactMessage Model

| Field Name  | Data Type            | Description                                                   |
|-------------|----------------------|---------------------------------------------------------------|
| `name`      | `CharField` (max_length=100) | Name of the person sending the message.                      |
| `email`     | `EmailField`         | Email address of the person sending the message.              |
| `message`   | `TextField`          | The content of the message sent by the person.                |
| `created_at`| `DateTimeField`      | The date and time the message was created.                    |


### Newsletter

The newsletter app allows users to subscribe to the restaurants newsletter by entering their email address. When a user submits their email, the app validates the email format, and if valid, saves the email address to the database for future newsletters. After successful submission, the user recieves a confirmation message indicating they have been subscibed. If the email is invalid, and error message will be displayed prompting the user to try again.

#### Newsletter App Database Schema

| Field Name    | Data Type             | Description                                                   |
|---------------|-----------------------|---------------------------------------------------------------|
| `email`       | `EmailField`          | The email address of the user subscribing to the newsletter.   |
| `date_subscribed` | `DateTimeField`  | The date and time when the user subscribed to the newsletter. |


### Account

The account app manages user accounts and order histories. It allows users to view and update their account details, such as contact information, through a form. When the form is submitted and validated, the user recieves a success message confirming the update. The app also displays the users past orders by fetching and showing associated orders.

Additionally, users can view and detailed information about individual orders, including items, prices, quantities, and the total cost, through the order history functionality. This is accessible by providing an order number, and the data is returned in JSON format.

| Field Name               | Data Type             | Description                                                                                   |
|--------------------------|-----------------------|-----------------------------------------------------------------------------------------------|
| `user`                   | `OneToOneField(User)` | A reference to the built-in `User` model. Links the `UserAccount` to a specific user.         |
| `default_phone_number`   | `CharField(max_length=20)` | The user's default phone number.                                                             |
| `default_street_address1`| `CharField(max_length=80)` | The user's default street address line 1.                                                     |
| `default_street_address2`| `CharField(max_length=80)` | The user's default street address line 2 (optional).                                          |
| `default_town_or_city`   | `CharField(max_length=40)` | The user's default town or city.                                                              |
| `default_county`         | `CharField(max_length=80)` | The user's default county (optional).                                                         |
| `default_country`        | `CountryField`         | The user's default country, stored as a country code.                                         |
| `default_postcode`       | `CharField(max_length=20)` | The user's default postcode (optional).                                                      |

## Future Features

### Loyalty Program

- Implement rewards program where customers can earn points for every purchase and redeem them for discounts or free items.

### Order Customization

- Allow customers to customize their food orders (eg. adding extra toppings, changing seasonings, etc) directly from the menu.

### Real-Time Order Tracking

- Provide customers with real time updates on their order status, from preperation to delivery, with push notifications for live tracking.

### Customer Reviews and Ratings

- Add functionality for customers to leave reviews and ratings for menu items and their overall experience.

### Gift Cards

- Implement a feature for customers to purchase and redeem digital gift cards for use in the restaurant.

# Testing

## Bugs

Issue: After deployment the send mail function was yielding a 500 server error.

Cause: Incompatability with send mail and python 3.12.

Solution: Downgrade to Pyton 3.11

Status: Fixed
_______

Issue: Unable to install allauth.

Cause: Incompatability of version of setuptools installed.

Solution: Upgrade setuptools to version 67.0.0

Status: Fixed

___

Issue: Webhooks creates the order in the database everytime a payment is processed.

Cause: Potentially cause by the matching criteria used in the webhook that checks if the order has been created being too specif, and leading to the webhook never registering the oder has been created.

Solution: Even though this was happening, it isnt creating duplicate orders and the payment flow was still working, which lead me to beleive the best option was to leave it as its not a major issue.

Status: Unfixed

## Manual Testing

### User Story Testing

#### Visitor Stories Testing

| **Test**                                      | **Description**                                                     | **Expected Result**                                                        | **Result**                               |
|-----------------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------------------------|------------------------------------------|
| View detailed menu                            | Test if users can view a detailed menu.                             | Menu should display all items with details like name, description, price.  | Pass                                     |
| Add items to shopping cart                            | Test if users can add items to the shopping cart                             | Items are added to the cart with the correct, name, price, and quantity  | Pass                                     |
| Review order                                  | Test if users can review their order before proceeding.             | Users should see the cart with the total price and itemized order.        | Pass                                     |
| Secure payment process                        | Test if users can securely pay for their order online.              | Payment should be processed securely with encrypted information.          | Pass
| Payment confirmation                          | Test if users receive a confirmation after a successful payment.     | A confirmation page with order details appears after the payment is made. | Pass                                     |
| Email confirmation                            | Test if users receive an email confirmation for their order.        | User receives an email with order details after successful payment.       | Pass                                     |
| User-friendly interface                       | Test if the website interface is easy to navigate for users.        | Website layout and design should be intuitive and easy to navigate.       | Pass                                     |
| Sign up for newsletter                        | Test if users can sign up for the newsletter.                        | A sign-up form should accept valid emails and display a confirmation.     | Pass                                     |
| Account creation                              | Test if users can create an account.                                | User should be able to register an account with valid information.        | Pass                                     |
| User login                                     | Test if users can log in to their account.                          | Users can log in using their registered credentials.                       | Pass                                     |
| User logout                                    | Test if users can log out of their account.                         | Users can log out, and their session is secured.                           | Pass                                     |


#### Admin Stories Testing

| **Test**                                      | **Description**                                                     | **Expected Result**                                                        | **Result**                               |
| Add, edit, and remove menu items              | Test if the admin can add, edit, or remove menu items.              | Admin can successfully perform these actions through the admin panel.     | Pass                                     |
| Restrict access to management functions       | Test if admin functions are restricted to authorized users.        | Unauthorized users should not have access to admin management functions. | Pass                                     |

#### Developer Stories Testing

| **Test**                                      | **Description**                                                     | **Expected Result**                                                        | **Result**                               |
|-----------------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------------------------|------------------------------------------|
| Defensive programming                         | Test if the site handles errors and invalid inputs properly.        | Site should not break and should handle invalid inputs gracefully.        | Pass                                     |
| User credentials and data access              | Test if users with correct credentials can access their data.      | Only users with valid credentials should be able to view their own data.  | Pass  

