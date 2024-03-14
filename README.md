<h1 style="text-align:center">SoleHaven</h1>

Welcome to SoleHaven. SoleHaven is a fictional online store for consumers to purchase premium shoes. This app provides a wide selection of new shoes for users to browse and pick and choose which ones they want. It also allows users to create reviews on each product.

Live project can be found here: [SolveHaven]([LINK HERE])

![Mock Up]([LINK HERE])

## Index
* [UX Design](#ux-design)
  * [Website Goals](#website-goals)
  * [Planning](#planning)
  * [Epics](#epics)
  * [User Stories](#user-stories)

## UX Design

### Website Goals

There is no specific target audience; anyone who has even a slight interest in premium trainers is welcome. The main aim of this website is to allow those users to browse around and pick out which trainers they want. The website is a simple design so it's easy to navigate and find exactly what you're looking for.

This website also aims to allow users to create, edit and delete their own reviews of the product, giving it a rating. Users will be able to see other users reviews and what they think about a specific product. Ratings of each product will also be viewable for users.

### Planning

This website was created using the agile methodology - working and pushing small features incrementally. This project was produced in 10 days so it was important to not space out development time too much. 

Furthermore, the project features were assigned with epics, detailing the reason behind why it was needed, and also assigned labels with MoSCoW(Must Have, Should Have, Could have and Won't Have) prioritisation. "Must Have" were given top prioritisation as they are essential for the projects functionality. "Should Have" labels are second on the list, "Could Have" is third and finally "Won't Have" is last and will be added to the backlog for future iterations. It was done this way to fufil the MVP requirements and minimise the scope of the project to present a functioning website.

Below is the Kanban board which was used throughout the project development cycle and was created using Trello:
[Trello]([LINK HERE])

![Kanban Board]([LINK HERE])

### Epics

**EPIC 1 - Setup**

The first epic is the setup. The setup is necessary for the application to have a base structure and wouldn't be possible to create a project without this.


**EPIC 2 - Authentication**

This epic is a critical step for the main function of the website and is related to all the user stories related to authentication. This will allow users to create profiles and view the pages that should only be accessible to them. 

**EPIC 3 - Products**

The product epic is for all user stories relating to the products on display. Site owners will be able to create, edit and delete products if necessary so users are given the correct information on display.

**EPIC 4 - Reviews**

This is related to all the user stories that are related to creating, reading, updating and deleting reviews. This allows users to see other users opinions on certain products, as well as, site owners to see what their best rated products are.

**EPIC 5 - Deployment**

This epic is to detail the steps made in deploying the project to Heroku for users to access and use.

### User Stories

**EPIC 1 - Setup**
- As a developer, I want to create a base.html page so I can extend it to the other html pages for reusability.

- As a developer, I want to create static files so that I can store images, CSS and JavaScript code so that it can be linked to the pages and work on the deployed website.

- As a developer, I want to create a header and footer which includes navbar and necessary links so that users have an easy time navigating through the website.

**EPIC 2 - Authentication**
- As a developer, I want to incorporate authentication so that users have the ability to create an account and login/logout.

- As a Site Owner, I want authentication implementation so that users accessing the site can create an account to purchase products and leave reviews.

- As a Site User, I want authentication implemented so I can create a personal account to purchase products and leave reviews for other users.

**EPIC 3 - Products**
- As a Site Owner, I want to be able to create new products to post on the site so that I can ensure any new products after inital deployment can be added.

- As a Site Owner, I want to be able to edit/delete products so that users can only see the available products we have to offer.

- As a user, I want to be able to view any products the site are offering so that I can see if I am interested in them for potential purchase.

**EPIC 4 - Reviews**
- As a Site Owner, I want to see users reviews on products so that we have the necessary data to see why users like or don't like certain products.

- As a Site User, I want to see other user reviews so that I can make a decision on a potential purchase.

- As a Site User, I want to create reviews so that I can express my opinion on certain products.

- As a Site User, I want to edit/delete my own reviews so that in case my opinion has changed, I can reflect that in the review after the inital post.

**EPIC 5 - Deployment**
- As a developer, I want to collect static files so they are served for deployment on Heroku.

- As a developer, I want to deploy the project on Heroku so that it can be accessed by users.