# EarthAlchemy Naturals

EarthAlchemy Naturals is a B2C e-commerce application specializing in natural and holistic products. The site is designed to offer users a visually appealing and user-friendly online shopping experience. Its core features include product offerings, discounts, a newsletter, social media presence, and a user-friendly profile function for saving customer information.

One standout feature of EarthAlchemy Naturals is the membership option. Customers can purchase a 12-month membership, which unlocks exclusive benefits, including a remarkable 30% discount on every product in the catalog. Additionally, members have the opportunity to customize their packaging box and receive luxurious packaging for a truly premium experience.

The site operates as a virtual retail store, allowing users to browse, search, and filter a wide range of natural products. Customers can select items to add to their shopping cart and make secure payments through a seamless checkout process.

For general users, the platform provides comprehensive product details, along with information about the main (star) ingrediant of each products. Customers can also subscribe to the company's newsletter to stay updated. Registered users can save their profile details, to make their future purchases faster and also have the availability to buy the membership. 

Admin users hold the ability to oversee and manage the product catalog and herb profiles. Their responsibilities encompass tasks such as adding new products, adjusting pricing, explaining the main herb used for each products, and constantly updating these information.

The project involves a variety of web marketing strategies, including organic social media marketing through Facebook, and email marketing via a newsletter subscription managed through Mailchimp. 
The structure and purpose of EarthAlchemy Naturals take inspiration from the Code Institute's Boutique Ado example application, ensuring a solid foundation for this e-commerce venture.

This full-stack project was built using the Django framework, Python, HTML, Bootstrap, and CSS. Additionally, ElephantSQL and AWS were used to store data, images, and static files. Stripe was used for payment processing.

![Application](README_docs/images/responsive.png "Application")

[Link to the live project](https://earthalchemy-naturals-99139eee523b.herokuapp.com/)

# Contents

- [User Experience (UX)](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#user-experience-ux)
  - [Ideal client](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#ideal-client)
  - [User stories & Epics](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#user-stories-and-epics)
- [Planning](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#planning)
- [Design](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#design)
  - [Wireframes](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#wireframes)
  - [Entity Relationship Diagrams](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#entity-relationship-diagrams)
  - [Theme](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#theme)
  - [Typography](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#typography)
- [Languages Used](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#languages-used)
- [Frameworks, Libraries, Programs & Technologies Used](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#frameworks-libraries-programs--technologies-used)
- [Features](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#features)
- [User Story - Features Cross-Reference table](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#user-story---features-cross-reference-table)
- [Deployment](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#deployment)
- [Testing](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#testing)
  - [Manual Testing](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#manual-testing)
  - [Further Testing](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#further-testing)
  - [Bugs](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#bugs)
- [Credits](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#credits)
  - [Media and Content](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#media-and-content)
  - [Acknowledgments and Code](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#acknowledgments-and-code)
  - [Disclaimer](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#disclaimer)

# User Experience (UX)

### Ideal client

The ideal client for this business is:

-	English speaking
-	Health and Wellness Enthusiasts
-	Value Quality and Customization
-	Eco-Conscious Consumers
-   Regular Online Shoppers
-   Avid Shoppers of Natural Products

Visitors to the EarthAlchemy Naturals website are seeking:

- A user-friendly and informative online store that provides reliable and comprehensive information about natural and holistic products, offering insights into their benefits and uses.
- Features that foster a sense of community and engagement. Members not only enjoy substantial discounts applied to all products, promoting a shared sense of value and savings within the community but also have the opportunity to select a VIP box in their choice of two beautiful colors as a complimentary add-on.
- The option to access a wide array of natural and holistic products, supporting a holistic lifestyle and promoting eco-conscious consumer choices.
- A variety of product categories to choose from, including toners, serums, sun protection and more, catering to diverse individual preferences and needs.
- A flexible shopping experience, allowing users to adjust their orders and quantities as needed, ensuring a convenient and personalized shopping journey.

This website is the best way to help them achieve these goals because:

- The user-friendly menu makes accessing different functionalities very easy and intuitive.
- The website's content is carefully curated and regularly updated to provide reliable and up-to-date information to the visitors.
- The membership program offers substantial discounts on all products and the added benefit of a VIP box in two color choices. This not only provides cost savings but also an element of personalization, creating a sense of value for members.
- EarthAlchemy Naturals offers a wide variety of natural and holistic products across different categories, catering to individual preferences and needs. Visitors can find an array of items that resonate with their lifestyle and goals.
- The website ensures a flexible and personalized shopping experience. Visitors can adjust their orders and quantities as needed, reflecting a commitment to customer convenience.
- The website also ensures a seamless and secure payment process, while registered users can save their profile details making this process even faster or the next time. 


In summary, the EarthAlchemy Naturals website effectively supports visitors in achieving their goals by offering information, community engagement, discounts, personalization through the VIP box, a diverse product range, and a user-friendly shopping experience. This combination of features and offerings aligns with the needs and interests of individuals seeking natural cosmetic products while creating a supportive and engaged community.

[Back to top](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#contents)


### User stories and Epics

#### Epic 1: User Management

- US0101: User Registration: As a new user, I can register an account with my email and password so that I can view my profile.
- US0102: User Authentication: As a returning user, I can log in using my existing credentials or log out so that I can access my personal information in a secure way.
- US0103: Receive Email Confirmation After Registration: As a new user, I can receive an email confirmation after registering so that I can verify that my account registration was successful.
- US0104: Personal User Profile: As a site user, I can access my personalized user profile so that I can view my order history and payment information and keep track of purchases

#### Epic 2: Product Management

- US0201: Purpose of website and navigation: As a site user I can quickly identify what the website is selling and easily navigate the pages so that I can quickly find the information and functionality I am looking for

- US0202: Product Creation: As an admin, I can add new products to the website so that I can keep my shop up to date.
- US203: Product Update: As an admin, I can edit product information so that all products have the most relevant and useful information.
- US0204: Product Deletion: As an admin, I can remove products that are no longer available so that I can keep my shop up to date.
- US0205: Product View: As a shopper, I can view a list of products so that I can browse and discover the collection.
- US0206: Product Details: As a shopper, I can view detailed information about each product so that I can make the best decision for my purchase.
- US0207: View main herb: As a site user I can view bio details of the main herb of the product was made of so that I can easily learn more about it.
- US0208: Product Search: As a shopper, I can search for products by keywords or categories so that I can target and speed up my purchase time.
- US0209: Product Filtering: As a shopper, I can filter products based on various criteria (e.g., price, ingredients, skin type) so that I can find the best selection of products specifically for me.
- US0210: Sort Products: As a shopper, I can sort specific category of products so that I can find the cheapest, most purchased, most expensive products easier.
- US0211: Handle 404 and 500 errors: As a site user I can return to Home after http 404 or 500 response so that I feel I am still working within the website and can navigate easily

#### Epic 3: Shopping Cart and Checkout

- US0301: Add to Cart: As a shopper, I can add products to my shopping cart so that I can purchase 1 or multiple items at the same time.
- US0302: Cart Management: As a shopper, I can update the quantity or remove items from my cart so that I can make changes later on in the process and/ or rectify any mistakes.
- US0303: View shopping cart total: As a shopper, I can view the total of my cart at any time so that I can avoid over-spending.
- US0304: Secure Payment Process: As a shopper, I can enter my card details with an intuitive checkout process so that I proceed with a secure and payment and purchase.
- US0305: Checkout Summary: As a, I can view a checkout page so that see details of my order and my delivery and payment details.
- US0306: Order Confirmation: As a shopper I can view an order confirmation so that I see the relevant details after completing my purchase.
- US0307: Email Confirmation: As a shopper, I can receive an email confirmation so that I have records of my purchases.
- US0308: Notifications: As a shopper, I can receive small messages from the website so that I am reassured on all actions and interactions throughout my visit.

#### Epic 4: Membership

- US0501: Understand Membership Benefits: As a shopper, I can learn about the benefits of being a member so that I can make informed decisions about joining.
- US0502: Join Membership Program: As a shopper, I can enroll in the membership program to access bonus points and exclusive offers.
- US0503: Member’s Price: As a member, I can access the member’s price for each product so that I can select that.
- US0504: VIP Access: As a member, I can see new products before they would go public so that I can purchase them first.
- US0505: Savings: As a member, I can view and track how much I have saved, paying the member price, in my user profile so that I can see the worth of my membership.
- US0506: Opt-Out of Membership: As a member, I can opt-out of the membership program if I no longer wish to participate so that I have flexibility.

#### Epic 5: Events and Blog

- US0601: Event Announcements: As an admin, I can announce upcoming events so that I can make my customers aware of new opportunities.
- US0602: Event Details: As a shopper, I can view detailed information about each event so I can decide to join.
- US0603: Educational Blog Posts: As an admin, I can publish informative blog posts about natural cosmetics so that I can spread information in the topic.
- US0604: Blog Reading: As a shopper, I can read blog posts and articles so that I can learn. more in the topic.

#### Epic 6: Admin Panel

- US0701: Admin Dashboard: As an admin, I can have a dashboard to manage products, discounts, and memberships so that I can stay organised.
- US0702: User Management: As an admin, I can manage user accounts and their activities so that I can take responsibility for my website.

#### Epic 7: SEO and Web Marketing

- US0801: Subscribe to Newsletter: As a site user, I can subscribe to the company newsletter so that I can keep up with company news and offers.
- US0802: Follow Brand Updates and Explore on Social Media: As a site user, I can find, visit and and follow the company's Facebook page so that I can stay connected with brand updates and announcements.
- US0803: SEO: As a site user, I can find the site through web searches so that I can easily access the site.
- US0804: View Privacy Policy: As a site user, I can access and view the company's privacy policy so that I can ensure the company is GDPR compliant and respects my privacy.
- US0805: Access Educational Content: As a site user, I can access blog posts and educational content about natural cosmetics and skincare so that I can learn more about the products.
- US0806: Easily Contact Customer Support: As a site user, I can find clear contact information and options for reaching out to customer support so that I can get assistance when needed.
- US0807: Share Feedback and Reviews: As a site user, I can leave reviews and feedback about products I've purchased so that I can share my experiences and help other shoppers.

[Back to top](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#contents)

# Planning

The planning process began by identifying the target clientele, which involved creating a Persona Profile using Code Institute's template based on design thinking principles. This Persona Profile helps in understanding the needs, expectations, and preferences of the identified persona, and the website is designed to cater to these specific requirements.
You can see the persona profile [HERE](README_docs/design_thinking_persona_template.pdf).

Given the prevalence of mobile usage among our target users, creating a responsive website was a top priority in our design approach. To achieve this, the power of Bootstrap grids, elements, and responsive utilities combined with custom CSS was leveraged, to ensure seamless adaptability across various devices.

### Agile Methodology

In this project Github issues were used to create the User stories and groupped into Epics, Milestones in a Github Project. This served as the Agile tool. The issues' development was managed through a Kanban board. Currently, all the issues have been marked as "Done”.

For easy access, you can find the Epics, Issues/ User Stories with their Acceptance Criteria and Kanban board [HERE](https://github.com/users/Lilla-Kavecsanszki/projects/6).

[Back to top](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#contents)

# Design

### Wireframes

[Desktop Wireframes](README_docs/wireframes_desktop.pdf)

[Tablet Wireframes](README_docs/wireframes_ipad.pdf)

[Mobile Wireframes](README_docs/wireframes_mobile.pdf)

### Entity Relationship Diagrams

To support the functionality of the DownwardDog app, five models have been designed and implemented to store essential information in databases.

To showcase the relationships between the models, I have divided them into two categories: one relevant to the Articles and the other to the Booking functionality.
The Likes and User tables in the ER diagrams are for conceptual representation only and do not directly correspond to the models.py file or the physical database tables. They provide a logical view of data relationships without showing all the actual database details managed by Django and the database system.

The Entity Relationship Diagrams below illustrate how the models are connected to each other for the Articles section:

- Post and Comment have a one-to-many relationship, where one post can have multiple comments, but each comment is associated with only one post.
- User and Likes have a many-to-many relationship, where multiple users can like multiple posts, and each like is linked to both a user and a post.
- User and Post have a one-to-many relationship, where one user can be associated with multiple posts, but each post is linked to only one user (the author). This feature is however limited for the admin.

<p>
<details><summary>Article ERD</summary><br/>
<img src="README_docs/images/article_erd.png" alt="Article ERD">
</details>

The Entity Relationship Diagrams below illustrate how the models are connected to each other for the Booking section:

- Classes and Timetable have a one-to-many relationship, where one class can have multiple timetables, but each timetable is associated with only one class.
- Timetable and Booking have a one-to-many relationship, where one timetable can have multiple bookings, but each booking is linked to only one timetable.
- Booking and User have a many-to-one relationship, where one user can create many bookings.

The unique_booking constraint in the Booking model ensures that a user can create multiple bookings, but only one booking for the same class on the same date/time.

<p>
<details><summary>Booking ERD</summary><br/>
<img src="README_docs/images/booking_erd.png" alt="Booking ERD">
</details>

[Back to top](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#contents)

### Theme

- Whitesmoke - #f5f5f5
- Wisp Pink - #eae4e2
- Swiss Coffee - #d4c9c5
- Goldenrod - #daa520
- Matterhorn - #555
- Nero - #222
- Black - #000000

![colour_palette](README_docs/images/colorkit.png "colour_palette")

The chosen color palette for the EarthAlchemy Naturals website serves the purpose of conveying a clean, fresh, and elegant aesthetic that aligns with the brand values and the nature of the products. It combines neutral and vibrant tones to create a sense of purity and well-being, while also highlighting key elements for engagement and readability.

### Typography

- Poppins (Body Font):
  - Poppins is a modern and versatile sans-serif font that offers excellent readability. It provides a clean and organized look for body texts, making it easy for visitors to read and navigate the content.
- Quicksand (Body Font):
  - Quicksand is another modern sans-serif font known for its rounded and friendly appearance. It pairs well with Poppins and offers a slightly different feel, contributing to a visually pleasing and approachable design.
- Cinzel Decorative (Header Font):
  - Cinzel Decorative brings the alchemical vibes with its decorative and mystical style, making headers and titles stand out, adding a touch of intrigue and uniqueness to the design.

![Poppins](README_docs/images/poppins.png "poppins")

Overall, this combination provides a clear distinction between body text and headers while maintaining a cohesive and balanced visual appeal, creating the desired ambiance for the shop.

[Back to top](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#contents)

# Languages Used

- HTML5
- Python
- CSS3
- Jquery

[Back to top](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#contents)

# Frameworks, Libraries, Programs & Technologies Used

- [Balsamiq](https://balsamiq.com/) was used to create the Wireframes
- [Lucid](https://lucid.app/documents#/documents?folder_id=recent) was used to create the ER Diagrams
- [Canva](https://www.canva.com/) was used to photoshop the images used
- [ColorKit](https://colorkit.co/palette/F5F5F5-EAE4E2-D4C9C5-DAA520-555-222-000000/) was used to create the colour palette.
- Github was used as the repository for the projects code after being pushed from Git
- CodeAnywhere was used for version control, allowing me to commit changes and push them to GitHub directly from the CodeAnywhere terminal. It was the primary tool used for creating and editing all the code.
- [Google Fonts](https://fonts.google.com/) used for the Montserrat and Poiret One fonts
- [Font Awesome](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes
- [Favicon](https://favicon.io/favicon-converter/) was used to create the favicon
- [Bootstrap](https://getbootstrap.com/) was used to build a responsive website quicker
- Microsoft Word was used to create the wireframes during the design process.
- [Django](https://www.djangoproject.com/) was used as the framework of the application
- [Gunicorn](https://gunicorn.org/) was used as the Web Server to run Django on Heroku
- [Pillow](https://pillow.readthedocs.io/en/stable/index.html) - Python Imaging Library used for image handling
- Django allauth used for account registration and authentication
- Django crispy forms used for form rendering
- [Amazon Web Services (AWS)](https://aws.amazon.com) used to store all of static files and images
- [Boto3](https://pypi.org/project/boto3/) the Amazon Web Services (AWS) Software Development Kit (SDK) for Python.
- [Stripe](https://js.stripe.com/v3/) used for secure payments
- [Heroku](https://heroku.com/) was used to deploy the application and provides an enviroment in which the code can execute

[Back to top](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#contents)

# Features

## Home Page

### F01 Navigation Bar

The navigation bar provides easy access to all active pages for the user.

**Menu Options:**

- **Account button:** This button provides quick access to register or login and then view and manage the user's profile. In case the user is logged in already, they can find the logout option in this dropdown menu also, and in case the admin user is logged in, they can find an extra, 'Product Management' option. 
The user can quickly determine their login status by looking at the user icon located at the top left corner of the screen. When the user is not logged in, the user icon is displayed as an outline with the label "Account". In contrast, when the user is logged in, the user icon is solidly filled, and their username is shown underneath the icon.

![Not Logged_In_Account](README_docs/images/not_logged_in_account.png "notlogged_in_account")

![Not Logged_In_Dropdown](README_docs/images/not_logged_in_dropdown.png "notlogged_in_dropdown")

![Logged_In_Account](README_docs/images/logged_in_account.png "logged_in_account")

![Logged_In_Dropdown](README_docs/images/logged_in_dropdown.png "logged_in_dropdown")

![Logged_In_Dropdown_Admin](README_docs/images/logged_in_dropdown_admin.png "logged_in_dropdown_admin")

- **Logo:** Essentially it indicates the name of the website, while it also serves as a button that is linked to the homepage as an instant solution for the user.

- **Search bar:** Users have the option to find their specific product, or narrow down the list of results by entering a search term, which will be used to search for matches within the products. The number of matching results is shown on screen and the results can be ordered by price, name and category.

- **Shopping bag:** Shows the total price of the items in cart, allowing the user to review and manage the costs of their selections.

![Top Navbar](README_docs/images/top_navbar.png "top_navbar")

- **Home:** This button serves as a quick link to the homepage, enabling users to navigate back to the main landing page at any point.
- **All Products:** This button enables users to view products sorted by either their price or category.

![All Products](README_docs/images/all_products.png "all_products")

- **Skin Types:** This button enables users to view products narrowed down and selected by their skin types, offering a more personalised approach.

![All Products](README_docs/images/all_products.png "all_products")

- **Shop:** This button enables users to view products narrowed down and selected based on their category, again to offer a personalised approach.

![All Products](README_docs/images/all_products.png "all_products")

- **About Us:** This button takes the user to a page, where they can learn more about the company.
- **Membership:** This button takes the user to a page, where they can learn about the membership and can purchase it too.
- **Contact:** This button takes the user to the Contact page, where they can fill out a form and get in touch with the company.

![Navbar](README_docs/images/navbar.png "navbar")

**Special Case for Administrators**

When the signed-in user is the admin user or superuser, an additional link labeled "Admin" is displayed on the navigation bar.

- **Admin:** This link grants access to the Django Admin window, allowing the superuser to manage the website's data, such as adding new, modifying, deleting or using them.
  
![Navbar Admin](README_docs/images/navbar_admin.png "navbar_admin")

### F02 Membership Banner

Beneath the navigation bar, each page features a banner that effectively captures the user's attention, piques their interest in the membership, its discounts, and potential purchases. This aligns with the main purpose of the website.

![Membership Banner](README_docs/images/banner.png "membership_banner")

### F03 Hero Image and Overlay Text

On the Home page, just below the navigation bar and banner, you'll find a highly relevant image featuring a cream product labeled as 'Illumination Mask' on some stones, with a herb on the side and a gold accessory under it. This image aligns with the website's purpose and brand ambiance. Additionally, a text overlay is positioned on the top left side of the image, displaying "Luxury awaits." This conveys the idea of exclusive quality available on the website, encouraging users to become regular shoppers and, in turn, members.

![Hero Image and Text](README_docs/images/hero_feature.png "hero_image&text")

### F04 Shop Now button

On top of the hero image, below the overlay text, there is a large, golden button, instantly leading to the goal of the website, which is to get the user to purchase products. The button therefore directs the user to the Products page, that lists all available the products.

![Shop Now Button](README_docs/images/shop_now_button.png "shop_now_button")

### F05 Footer

Just like the navigation bar and banner, the footer is consistently displayed on every page. Located at the very bottom, it provides information about the company's social media presence, with a link for users to easily follow. It also includes a link to the company's Privacy Policy and a user-friendly subscription form, allowing users to sign up for the monthly newsletter. The footer ends with a disclaimer, mentioning the website's creator and providing a convenient link to the developer's LinkedIn profile. It also clarifies that the website was created solely for educational purposes.

![Footer](README_docs/images/footer.png "footer")

## Products Page

### F06 List and View of the Products

The user can effortlessly navigate the assortment of available products for purchase on the website by utilizing the "All Products" option found in the navigation bar. The displayed product cards include an image of each product, along with relevant details such as name, category, skin type it's useful for and its price.

![Product_List](README_docs/images/product_list.png "product_list")

### F07 Information Button

 A gold "Information" button, in the bottom right corner, allowes quick access to the contact page for any questions that could come up while browsing through the products, offering faster solution and better user experience. The button is fixed to the screen, ensuring it remains accessible while the user scrolls up or down. Additionally, it features a jumping effect designed to capture the user's attention.

![Information](README_docs/images/information.png "information")

### Future ambitions - Planned for the Next Sprint

- I
- S
- E
- j

[Back to top](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#contents)

# User Story - Features Cross-Reference table

How the Features align with and fulfill the User Stories by providing the necessary functionality and interactions that meet the users' needs and requirements.

[Cross-reference Table](README_docs/us_f_crossreference.pdf "crossreference_table")

[Back to top](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#contents)

# Deployment

**How to Clone**
<p>
<details><summary>Steps</summary><br/>

1. Go to the <https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals> repository.
2. Click the Code button to the left of the green Gitpod button, then choose Local.
3. Click on headings for HTTPS, SSH, and Github CLI to find their individual URL links. Choose the HTTPs one.
4. Open your own terminal in your editor and change the current working directory to the location of where you want
   the cloned directory to be.
5. In the terminal type git clone, and then paste the URL you copied from the repository page.
6. Press enter to start the process.
7. To install the packages required by the application use the command : pip install -r requirements.txt
8. When developing and running the application locally set DEBUG=True in the settings.py file
9. Modifications performed on the local clone can be synchronized with the repository by executing the following commands:
    -  git add filenames (or "." to add all changed files)
    -  git commit -m "your message"
    -  git push
 Modifications pushed to the main branch will be implemented in the live project after re-deployment from Heroku. Ensure that you do not include DEBUG=True in the settings.py file on GitHub; this setting is intended exclusively for local use.

</details>
<br>

**How to Fork**
<p>
<details><summary>Steps</summary><br/>

1. Go to the <https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals> repository.
2. Click the fork button in the top right of the screen, between the watch, and the star buttons.

</details>
<br>

**Deployment of the project**
<p>
<details><summary>Create a respository on GitHub</summary><br/>

- Use the [CI Full Template](https://github.com/Code-Institute-Org/ci-full-template) to create a project
- Click on 'Use this template' then 'Create a new respository'
- Fill out the form, especially the 'Repository name' then click on 'Create repository'
- Copy over the URL of the repository and paste it into a New Workspace on Codeanywhere then it will start to build.
- Install Django and supporting libraries in the terminal:
- Create requirements file: 'pip3 freeze --local > requirements.txt'
- Create Project: 'django-admin startproject PROJ_NAME .'
- Create App: 'python3 manage.py startapp APP_NAME'
- Create a new env.py file in the root directory and include the database:
  - 'import os' on the top in env.py file
  - Set the environment variables (same values as later in Heroku Config Vars)
  
</details>
<br>


<p>
<details><summary>ElephantSQL</summary><br/>

- Create an account on [ElephantSQL](https://www.elephantsql.com/) and click "Create New Instance"
- In "Create new instance" section setup details:
    - Select the TINY TURTLE database plan and name,
    - Select region,
    - click confirm
- In the Details section you will find the URL which is necessary for the DATABASE_URL config variable later on Heroku.
  
**Connecting ElephantSQL database in Code Anywhere**

After having our instance created on Elephant SQL and the app on Heroku:

- After installing dj_database_url and psycopg2 in the terminal
- Import dj_database_url underneath the import for os in settings.py:
    import os
    import dj_database_url
- Update the DATABASES to the following code, so that the original connection to sqlite3 is commented out and we connect to the new ElephantSQL database instead. Paste in your ElephantSQL database URL.
'
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     }
    # }
            
    DATABASES = {
        'default': dj_database_url.parse('database-url-here')
    }
    `

    Do not commit with this database string in the code to avoid leaving database URL in version control. It is a temporary solution so that you can connect to the new database and make migrations. This setting needs to be removed afterwards.
- In the terminal, run the showmigrations command to confirm you are connected to the external database:
  - python3 manage.py showmigrations
  - If you are, the list of all migrations should appear, but none of them should be checked off.
- Run migrations:
  - python3 manage.py makemigrations --dry-run
  - python3 manage.py makemigrations
  - python3 manage.py migrate --plan
  - python3 manage.py migrate
- Load in the fixtures if you are wokring with those. Note, that The order is very important here. Categories need to be loaded first, then products:
  - python3 manage.py loaddata categories
  - python3 manage.py loaddata products
- Create a Superuser:
  - python3 manage.py createsuperuser
- Prevent exposing the database when pushing to GitHub and delete it from settings.py.

    `
     DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    `

**Confirming migrations in ElephantSQL**

- On the ElephantSQL page for your database, select BROWSER (left hand side menu)
- Click the Table queries button and select auth_user.
- Click “Execute”, and you should be able to see the new created superuser details.
- This is your proof that the tables have been created and you can add data to your database.

</details>
<br>

<details>
<summary>Heroku</summary>

- Create a Heroku application by pressing "New" on located on the upper right side of the main page
- Select: 'Create new app' from the dropdown menu.
- Go to the next page, fill the form with the following data: 'App name' and 'Choose a region'
- Press 'Create app'
- On the Application Configuration page for the new app, click on the Resources tab.
- In the Resources tab, search for Heroku Postgre and add it to your project.
- You need to install dj_database_url and pyscopg2 in your terminal:
    - pip3 install dj_database_url
    - pip3 install psycopg2
- Click on Settings on the Application Configuration page then "Reveal Config Vars" to add credentials
- Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1.
- Add a new Config Var called SECRET_KEY and assign it a value.
- The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :
  - if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
  - SECRET_KEY = os.environ.get('SECRET_KEY')
- Install gunicorn:
  - pip3 install gunicorn
- Freeze requirements: 
  - pip3 freeze > requirements.txt
- Create a Procfile, needs to contain the following code:
  - web: gunicorn (the_app_name).wsgi:application
- Disable Heroku from collecting static files:
  - heroku config:set DISABLE_COLLECTSTATIC=1 -- app-name
- Add the host names to settings.py file:
  - ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']
- Set DEBUG flag to False in settings.py
- In order to be able to run the application on localhost, add SECRECT_KEY and DATABASE_URL and their values to env.py as well
- Connect Heroku to your Github (See further below)

Config Vars in Heroku should have:

  AWS_ACCESS_KEY_ID = 'your variable'
  AWS_SECRET_ACCESS_KEY = 'your variable'
  DATABASE_URL = 'your variable'
  DISABLE_COLLECTSTATIC = 1
  EMAIL_HOST_PASS = 'your variable'
  EMAIL_HOST_USER = 'your variable'
  SECRET_KEY = 'your variable'
  STRIPE_PUBLIC_KEY = 'your variable'
  STRIPE_SECRET_KEY = 'your variable'
  STRIPE_WH_SECRET = 'your variable'
  USE_AWS = True

</details>

<details>
<summary>Connect the Heroku application to the GitHub repository</summary>

- Go on the Heroku page of the application then 'navigate to the Deploy' tab
- Scroll down to 'Deployment method' and select GitHub
- Below that search for the Github repository to connect
- Click on 'Connect'
- Below that there are two options: 'Automatic deploys' or 'Manual deploy'
- To manually deploy: enter 'main' as the name of the branch and press 'Deploy Branch'
- Main branch starts building up automatically
- At the end of the build a message pops up: 'Your app was successfully deployed' and a button: 'View'
- Click on 'View' to see the live project. The live link to the project is [HERE](<https://earthalchemy-naturals-99139eee523b.herokuapp.com/>)

</details>

<details>
<summary>Configure Amazon Web Services S3 to store static files and images</summary>

- Go to aws.amazon.com - create an account and log in
- Access the S3 services from the dashboard
- Create a new 'bucket', it is recommended to give this a name matching your application, choose a region, uncheck "Block all public access" and acknowledge that the bucket will be public.  Next, click on the new bucket to create it.
- Go to the properties tab and turn on static website hosting, fill in default values for index and error document settings - e.g. index.html and error.html and click on Save.
- Go to the permissions tab and make the following changes to configure the bucket :

**Configure CORS:**
    - Paste the following CORS configuration string : <br>
    	[ { "AllowedHeaders": ["Authorization"],<br>
                "AllowedMethods": ["GET"],<br>
                "AllowedOrigins": ["*"],<br>
                "ExposeHeaders": [] } ]<br>

**Generate Policy:**
    - Go to the bucket policy area, click on Edit and click on policy generator.  
    - Choose S3 bucket policy from drop-down
    - Put '*' in Principal field
    - Select get object from Actions drop-down
    - Copy ARN and paste into ARN box on the policy generator page
    - Click Add Statement
    - Click Generate Policy then copy the policy into the policy editor window
    - Add /* to the end of the Resource key
    - Click Save

**Access Control List (ACL):**
    - Go to the Access Control List area
    - Set the list objects permission: For Everyone (public access) under the Public Access section and
		check the box to confirm you want this permission setting

**AWS IAM (Identity and Access Management) setup:**
  - From the IAM dashboard (on the left side), select User Groups: click Create a new group then click 
    through and finally click Create Group
  - On the same page click on Policies, then Create Policy, go to JSON table and select Import Managed Policy
  - Click on Import managed policy
  - Search for S3 and select AmazonS3FullAccess and click on Import
  - Go back and get the Bucket Policy ARN
  - Change the Resource value from *to ARN bucket and its contents - e.g : <br>
        "Resource": [<br>
                    "arn:aws:s3:::earthalchemy-naturals",<br>
                    "arn:aws:s3:::earthalchemy-naturals/*"<br>
                ]<br>
  - Click Next and then Review Policy
  - Give the policy a name and click Create Policy
  - Attach the policy to the group you created: 
        Go to groups, click on your group, go to the Permissions tab, click Add permissions and select Attach policies, select the policy created on previous step and click Attach permissions
  - Create user to put into the group. Click Users on the side menu, click Add User, assign name check the programmatic access checkbox, click on Next:Permissions.  Add user to group, click through to the end and click Create User.

- Download and save the generated csv which contains the users access and secret access keys
- Update the AWS section of the settings.py file - replace the bucket name and region with the values you set up in the previous steps :

			if 'USE_AWS' in os.environ:
				# Bucket Config
				AWS_STORAGE_BUCKET_NAME = 'earthalchemy-naturals'
				AWS_S3_REGION_NAME = 'eu-west-2'
				AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
				AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

- Add the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY config vars to heroku using the values from the downloaded cvs
- Add USE_AWS = True to the Heroku config vars
- Remove the DISABLE_COLLECTSTATIC config var at this point from Heroku
- The custom_storages.py file that is part of this project will tell Django to use S3 to store static and media files when collectstatic is run
- The remaining AWS configuration settings needed are already configured in this projects settings.py file
- Go to the S3 dashboard and create a folder called media in the new bucket.  Specify grant public-read access on the folder and tick the checkbox to confirm.

**Connecting Heroku to AWS S3**

Install boto3 and django-storages
- pip3 install boto3
- pip3 install django-storages
- pip3 freeze > requirements.txt
Add the values from the .csv you downloaded to your Heroku Config Vars, then delete the DISABLE_COLLECTSTATIC variable and deploy your Heroku app.

With your S3 bucket now set up, you can create a new folder called media and upload any required media files to it. - these folder and so the files need to be publicly accessable!

</details>

<details>
<summary>Configure STRIPE config vars and webhooks</summary>

- Log in to your Stripe account
- Add STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY to the Heroku config vars, find these variables values in your Stripe account dashboard
- Create a webhook endpoint for use with your applications.  On the stripe dashboard go to 'Developers' then Webhooks, click add endpoint, use the url of your Heroku application with '/checkout/wh/' added onto the end of the url string.  When configuring the endpoint, add all events.
- Once the endpoint is set up, retrieve the signing secret key for the webhooks and save this value as a Heroku config var called STRIPE_WH_SECRET.

</details>

#### The live link to the application can be found here - [EarthAlchemy Naturals](https://earthalchemy-naturals-99139eee523b.herokuapp.com/)


[Back to top](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#contents)

# Testing

<p>
<details><summary>W3C HTML Validator result</summary><br/>
to validate all HTML code written and used in this website
<img src="README_docs/images/html_validator.png" alt="HTML Validator">
</details>

<p>
<details><summary>W3C CSS Validator result</summary><br/>
to validate all CSS code written and used in this website
<img src="README_docs/images/css_validator.png" alt="CSS Validator">
</details>

<p>
<details><summary>JS Hint result</summary><br/>
to validate the javascript code written and used in this website
<img src="README_docs/images/jshint.png" alt="JSHint">
</details>

<p>
<details><summary>CI Python Linter - views.py</summary><br/>
to validate python code written and used in the views.py
<img src="README_docs/images/python_linter_views.png" alt="Python Validator views.py">
</details>

<p>
<details><summary>CI Python Linter - models.py</summary><br/>
to validate python code written and used in the models.py
<img src="README_docs/images/python_linter_models.png" alt="Python Validator models.py">
</details>

<p>
<details><summary>CI Python Linter - forms.py</summary><br/>
to validate python code written and used in the forms.py
<img src="README_docs/images/python_linter_forms.png" alt="Python Validator forms.py">
</details>

<p>
<details><summary>CI Python Linter - admin.py</summary><br/>
to validate python code written and used in the admin.py
<img src="README_docs/images/python_linter_admin.png" alt="Python Validator admin.py">
</details>

<p>
<details><summary>CI Python Linter - application urls.py</summary><br/>
to validate python code written and used in the app's urls.py
<img src="README_docs/images/python_linter_urls.png" alt="Python Validator urls.py">
</details>

<p>
<details><summary>CI Python Linter - project urls.py</summary><br/>
to validate python code written and used in the project's urls.py
<img src="README_docs/images/python_linter_p_urls.png" alt="Python Validator project urls.py">
</details>

<p>
<details><summary>CI Python Linter - project settings.py</summary><br/>
to validate python code written and used in the project's settings.py
<img src="README_docs/images/python_linter_p_settings.png" alt="Python Validator project settings.py">
</details>

## Manual Testing

The table provided below presents the test cases that were utilized, with the corresponding results, and references to the corresponding Feature IDs that each test case addressed. These test cases were primarily designed based on the Acceptance Criteria specified for each User Story.

Details here:
[Manual Testing Document](README_docs/manual_testing_cases.pdf)

All tests passed successfully, indicating that the specified features and functionalities are working as intended.

### Further testing

<p>
<details><summary>Details</summary><br/>
I asked friends and family to look at the application on their devices, browsers and report any issues they find. A few responsiveness and semantical issues were resolved as a result of this.
</details>

[Back to top](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#contents)


## Bugs

1. 
  The checkout_success function brake when I added the membership purchase logic to it. The error occured essentially because the profile variable was not defined in the scope of the checkout_success function when however it was called. I could resolve the problem by adding the 'profile = UserProfile.objects.get(user=request.user)' line inside the if statement, just as it was done under this for the authentication bit.

debugging statement in profile.html:

{% if user.is_authenticated %}
<p>User is authenticated</p>
<p>Membership Status: {{ user.userprofile.membership_status }}</p>
{% if 'packaging_choice' in form.fields %}
<p>Field is present</p>
{% else %}
<p>Field is not present in the form</p>
{% endif %}
{% else %}
<p>User is not authenticated</p>
{% endif %}

result: not present in the form

https://stackoverflow.com/questions/46773416/rendering-different-templates-to-the-same-url-pattern-in-django

2. 
   Integrity Error occured, when trying to register, login. Foreign Key constraint failed:

   In the create_or_update_user_profile, needed to also pass the membership_status when we create the user profile. The user object contained all the dat needed, but not the membership_status. We use get_or_create, to set the membership status to 'None', but that also returned a tuple, so eventually the solution was to get seperated by saying: membership_instance, created. This means we get membership_instance as an instance of Membership, and created as True/False.

[Back to top](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#contents)

# SEO

Keyword Research -> Google to narrow down the list, consider relevance, authoritativeness, volume and competition.
I need high enough volume, but low enough competition. URL and aria attributes. rel="noopener" in footer
Useful links for the About page - External link ideas - sources for the herb descriptions
image alts
meta data
useful, well informed and trustworthy content also helps in ranking.

![keyword_research](README_docs/images/keyword-search.png "keyword_research")

Wordtracker
[Wordtracker](https://www.wordtracker.com/search?query=*%20natural%20products%20for%20skin)

Results:

- natural skin care products
- holistic skin care routine
- best online shopping sites for women
- members only discount
- premium box packaging
- natural products buy online
- exclusive discounts
- custom packaging
- online shopping with best discounts
- membership
- natural
- organic

# Credits

## Media and Content

All images were taken from [Unsplash.com](https://unsplash.com/)

Inspiration:
- <https://www.naturisimo.com/>
- <https://www.beautypie.com>

Resources:
- ginseng:
<https://www.medicalnewstoday.com/articles/262982#_noHeaderPrefixedContent>
- rosemary:
<https://www.medicalnewstoday.com/articles/266370#_noHeaderPrefixedContent>
- chamomile:
<https://www.health.com/chamomile-benefits-7494692>
- ginger:
<https://www.health.com/ginger-benefits-7372485>
- rose:
https://www.health.com/search?q=rose


## Acknowledgments and Code

I drew inspiration for this project from my personal hobby of creating natural skincare products and my passion for playing around with essential oils, ingredients and cosmetics.
To ensure the creation of a successful and comprehensive project, I researched similar e-commerce platforms and reviewed the work of fellow students, aiming to gain a clearer perspective on project scope and to identify best practices for the development of a Milestone Project 5.

The below websites and Youtube channels have been used to understand the logic of building this project with Django;

The walk-through project 'Boutique Ado' from Code Institute videos - its codes were also heavily used in the project: <https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+2021_T1/courseware/eb05f06e62c64ac89823cc956fcd8191/3adff2bf4a78469db72c5330b1afa836/>


shimmer button : <https://codepen.io/Amarjit/pen/mrbjNy>
admin site list_display: <https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display>
forms: https://docs.djangoproject.com/en/3.2/ref/forms/fields/
https://docs.djangoproject.com/en/3.2/ref/forms/fields/

contact - email send: <https://docs.djangoproject.com/en/3.2/topics/email/>
<https://medium.com/powered-by-django/send-emails-with-django-contact-form-example-d8820c875731>

customising the form fields
https://stackoverflow.com/questions/65730017/using-widgets-to-change-the-css-of-label-in-django-forms
https://stackoverflow.com/questions/43762471/how-to-use-the-attrs-in-forms-charfieldwidget-forms-passwordinput
how to make a form field read only, not editable
https://stackoverflow.com/questions/324477/in-a-django-form-how-do-i-make-a-field-readonly-or-disabled-so-that-it-cannot

membership
<https://levelup.gitconnected.com/building-a-membership-system-in-django-under-5-mins-5efd7e03627d>

<https://stackoverflow.com/questions/57019042/django-time-zone-and-timezone-now>

https://www.geeksforgeeks.org/python-datetime-timedelta-function/

<https://stackoverflow.com/questions/4406377/django-request-to-find-previous-referrer>

I also would like to take the chance and express my sincere gratitude to my mentor, Elaine Roche, and the tutoring team for their steadfast support and invaluable feedback. Their guidance, tips, and resources have played a crucial role in enhancing my coding and testing skills. While Elaine has embarked on a new journey, she was instrumental in initiating this project and guiding me throughout this year and four previous projects. Gareth McGirr has since taken me under his mentoring wings, and I am very appreciative of his assistance, suggestions, and ideas that have contributed to the project's finest appearance and functionality.

## Disclaimer

This application is for educational use only.

[Back to top](https://github.com/Lilla-Kavecsanszki/EarthAlchemyNaturals#contents)
