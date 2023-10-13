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

- [User Experience (UX)](https://github.com/Lilla-Kavecsanszki/downwarddog#user-experience-ux)
  - [Ideal client](https://github.com/Lilla-Kavecsanszki/downwarddog#ideal-client)
  - [User stories & Epics](https://github.com/Lilla-Kavecsanszki/downwarddog#user-stories-and-epics)
- [Planning](https://github.com/Lilla-Kavecsanszki/downwarddog#planning)
- [Design](https://github.com/Lilla-Kavecsanszki/downwarddog#design)
  - [Wireframes](https://github.com/Lilla-Kavecsanszki/downwarddog#wireframes)
  - [Entity Relationship Diagrams](https://github.com/Lilla-Kavecsanszki/downwarddog#entity-relationship-diagrams)
  - [Theme](https://github.com/Lilla-Kavecsanszki/downwarddog#theme)
- [Languages Used](https://github.com/Lilla-Kavecsanszki/downwarddog#languages-used)
- [Frameworks, Libraries, Programs & Technologies Used](https://github.com/Lilla-Kavecsanszki/downwarddog#frameworks-libraries-programs--technologies-used)
- [Features](https://github.com/Lilla-Kavecsanszki/downwarddog#features)
- [User Story - Features Cross-Reference table](https://github.com/Lilla-Kavecsanszki/downwarddog#user-story---features-cross-reference-table)
- [Deployment](https://github.com/Lilla-Kavecsanszki/downwarddog#deployment)
- [Testing](https://github.com/Lilla-Kavecsanszki/downwarddog#testing)
  - [Manual Testing](https://github.com/Lilla-Kavecsanszki/downwarddog#manual-testing)
  - [Further Testing](https://github.com/Lilla-Kavecsanszki/downwarddog#further-testing)
  - [Bugs](https://github.com/Lilla-Kavecsanszki/downwarddog#bugs)
- [Credits](https://github.com/Lilla-Kavecsanszki/downwarddog#credits)
  - [Media and Content](https://github.com/Lilla-Kavecsanszki/downwarddog#media-and-content)
  - [Acknowledgments and Code](https://github.com/Lilla-Kavecsanszki/downwarddog#acknowledgments-and-code)
  - [Disclaimer](https://github.com/Lilla-Kavecsanszki/downwarddog#disclaimer)

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

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)


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

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

# Planning

The planning process began by identifying the target clientele, which involved creating a Persona Profile using Code Institute's template based on design thinking principles. This Persona Profile helps in understanding the needs, expectations, and preferences of the identified persona, and the website is designed to cater to these specific requirements.
You can see the persona profile [HERE](README_docs/design_thinking_persona_template.pdf).

Given the prevalence of mobile usage among our target users, creating a responsive website was a top priority in our design approach. To achieve this, the power of Bootstrap grids, elements, and responsive utilities combined with custom CSS was leveraged, to ensure seamless adaptability across various devices.

### Agile Methodology

In this project Github issues were used to create the User stories and groupped into Epics, Milestones in a Github Project. This served as the Agile tool. The issues' development was managed through a Kanban board. Currently, all the issues have been marked as "Done”.

For easy access, you can find the Epics, Issues/ User Stories with their Acceptance Criteria and Kanban board [HERE](https://github.com/users/Lilla-Kavecsanszki/projects/6).

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

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

### Theme

Gold - #DAA520
White Powder - #FDFDFD
Light Pink - #eae4e2
Dusk Pink - #d4c9c5
Light Grey - #808080
Medium Grey - #555
Dark Grey - #222
Black - #000000

![colour_palette](README_docs/images/colorkit.png "colour_palette")

### Typography

- Poppins (Body Font):
  - Poppins is a modern and versatile sans-serif font that offers excellent readability. It can provide a clean and organized look for your body text, making it easy for visitors to read and navigate your content.
- Quicksand (Body Font):
  - Quicksand is another modern sans-serif font known for its rounded and friendly appearance. It pairs well with Poppins and offers a slightly different feel, contributing to a visually pleasing and approachable design.
- Cinzel Decorative (Header Font):
  - Cinzel Decorative brings the alchemical vibes you're looking for. Its decorative and mystical style can make your headers and titles stand out, adding a touch of intrigue and uniqueness to your design.

![Poppins](README_docs/images/poppins.png "poppins")

Overall, this combination provides a clear distinction between body text and headers while maintaining a cohesive and balanced visual appeal, creating the desired ambiance for the shop.

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

Inspiration:

https://www.naturisimo.com/
<https://www.beautypie.com>

Resources:
ginseng:
https://www.medicalnewstoday.com/articles/262982#_noHeaderPrefixedContent
rosemary:
<https://www.medicalnewstoday.com/articles/266370#_noHeaderPrefixedContent>

code:

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

Technologies:

<https://favicon.io/favicon-converter/>
canva - to photoshop
https://colorkit.co/color-palette-generator/00563F-DAA520-FDFDFD-d4c9c5-d6c9c0-808080-555-000000/
