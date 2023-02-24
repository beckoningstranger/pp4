# pp4

SocialBlog is a simple social network that allows user to post blog entries. They can also follow other users to see their blog entries on their own timeline. The social component is that users can also leave likes and comments on blog posts which enables users to leave feedback and discuss.

Take a look at the deployed website: <a href="https://pp4-social-blog.herokuapp.com/" target="_blank" rel="noopener">SocialBlog</a>.

# Contents

* [**User Experience UX**](#user-experience-ux)
  * [User Stories](#user-stories)
  * [Design](#design) 
    * [Site Structure](#site-structure)
    * [Color Scheme](#color-scheme)
    * [Typography](#typography)
    * [Wireframes](#wireframes)
* [Features](#features)
  * [Existing Features](#existing-features)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)
* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
* [Testing](#testing)
  * [Validator Testing](#validator-testing)
    * [HTML and CSS](#html-and-css)
    * [Javascript](#javascript)
    * [Python](#python)
    * [Lighthouse Test](#lighthouse-test)
    * [Web Accessibility Evalution Tool](#wave-test)
  * [Responsiveness Test](#responsiveness-test)
  * [Testing User Stories](#testing-user-stories)

* [Deployment](#deployment)
  * [How to Deploy the Project on GitHub Pages](#how-to-deploy-the-project-on-github-pages)
  * [How to Fork the Repository on GitHub](#how-to-fork-the-repository-on-github)
  * [How to Clone the Repository on GitHub](#how-to-clone-the-repository-on-github)
* [Credits](#credits)
  * [Content](#content)
  * [Media](#media)
  * [Code](#code)
* [Acknowledgements](#acknowledgements)

# User Experience UX

## User Stories

  * As a user, I can get a good idea of what the page is about just by looking at the landing page so that I have an incentive to sign up.

  * As a user I can create an account and login so that I can access all of the site's features, such as posting my own blogs, commenting, liking and following other people.

  * As a user I can create blog posts and find them easily on a timeline that acts as a central hub from where I will access most of the site's content so that access all of the content that's relevant to me.

  * As a user, I can easily share posts that I find on SocialBlog on other social media websites such as Facebook and Twitter so that I can spread the news.

  * As a user I can create and maintain a user profile including an image so that I can show others who I am and also to give them an incentive to follow me so that I will gain followers and traction on the site.

  * As a user I can read each blog post in a convenient manner and also look at all uploaded images so that I can enjoy the content and keep up to date with all of the content that's relevant to me.

  * As a user I can comment on other people's posts so that we can get a discussion going and interact with each other.

  * As a user, I can edit and delete my comments so that I can correct spelling errors, expand my posts or delete them entirely when I find for whatever reason that I don't want other people to read them anymore.

  * As a user, I can follow other people so that I can keep up with what they are doing.
  
  * As a user, I can unfollow other people so that I can keep my timeline orderly when I'm no longer interested in their posts.

  [Back to top](<#contents>)

## Design

### Site Structure

  Upon loading the site, users are shown a landing page that gives a brief description of what the site is about. Users are incentivised do sign up, but the top menu allows them to navigate to the login page as well. After logging in, users are taken to their timeline. This shows both their blog posts as well as the blog posts of all people the users follow. On the timeline, users can navigate to the individual blog posts by clicking them and create new blog posts via the top menu which would take them to a form where they can compose text and upload pictures.
  The top menu also allows them to go to their own profile page which they can then edit. Clicking the names of other authors - they are shown on each blog post card - takes users to the profile pages of the respective other authors. Profile pages show some data on each user, such as number of posts, join date etc., as well as all of their posts ordered by date.
  The last thing the top menu allows users to do is navigate to their circle. Here, the circle is the sum of all users that the user follows. The circle feature will show users everyone that they follow already. It also offers options to follow and unfollow users by clicking the respective buttons.
  After clicking a blog post, users can read the blog contents and look at the uploaded pictures. They can also leave likes and comments.

  [Back to top](<#contents>)

### Color Scheme

  ![Color Scheme](/static/images/readme/color-scheme.jpg)

  The colors of this project are mostly the bootstrap default colors, i.e. Eerie Black is the 'dark' background color, Amber is the 'warning' color used as a font color on the landing page, Vivid Sky Blue is the 'info' color that is used for comment boxes and Flickr Blue is 'primary' color used for most buttons. Steel Pink is used as an accent font and button color on the landing page and for the blog post cards on the timeline page. Here, it appears darker as I have applied a transparency value to make the color more subdued so that it's easier on the eyes.

  [Back to top](<#contents>)

### Typography

  Google Fonts was used for the following fonts:

  * Roboto is used every except for the logo. It was picked because of its excellent readibility.

  * The 'SocialBlog' logo that is shown on every page at the top left uses the Monoton font.

  [Back to top](<#contents>)

### Wireframes

  I created detailed wireframes in Balsamiq and have realized them almost perfectly:

  ![Landing Page](/static/images/readme/Landing%20Page.png)
  ![Login Page](/static/images/readme/Login%20Page.png)
  ![Signup Page](/static/images/readme/SignUp%20Page.png)
  ![Timeline Page](/static/images/readme/Timeline%20Page.png)
  ![Add Post Page](/static/images/readme/Add%20Post%20Page.png)
  ![Delete Post Page](/static/images/readme/Delete%20Post%20Page.png)
  ![Post Details Page](/static/images/readme/Post%20Details%20Page.png)
  ![Edit Comment Page](/static/images/readme/Edit%20Comment%20Page.png)
  ![Delete Comment Page](/static/images/readme/Delete%20Comment%20Page.png)
  ![Circle Page](/static/images/readme/Circle%20Page.png)
  ![Follow More Users Page](/static/images/readme/Follow%20More%20Users%20Page.png)

  [Back to top](<#contents>)

# Features

## Existing Features

### Landing Page

  * The landing page gives users a good idea of what the page is about and is reasonably attractive looking so that users have an incentive to sign up.

### Login Page, Signup Page

  * Both of these pages have a simple layout that lets users sign up and login without distractions. In the event that users with an existing account navigated to the sign up page by mistake there are links to navigate to the login page and vice versa. As both pages are similar in that they are basically forms the fact that their layout (at least on larger devices) is different makes them easier to tell apart from each other. On one page, the image is on the left side, on the other it's on the right side. Of course, the image itself and the text on each page is also different.

### Top Menu

  * The top menu is context dependent, i.e. it doesn't show the same items on every page.
  * It shows the logo at the top left consistently. The logo is a link that takes users that are not logged in back to the landing page and users that are logged in back to their timeline.
  * Once logged in, the consistent items are the 'Timeline' and 'Circle' buttons as well as an expandable item which shows the username of the logged in user. Upon clicking this items, it reveals a link to the logged in user's profile and a button to log out.
  * On top of the actions above, the top menu shows context dependent actions based on where users are at the moment. On the timeline page, it shows a button to add a new post, on the circle page a button to follow more users. On post detail pages of posts that were posted by the logged in user, the user can edit and delete posts from here.

  ![Example of Top Menu on the Timeline Page](/static/images/readme/topmenu.png)

[Back to top](<#contents>)

### Timeline cards

  Each of the cards shown on the timeline contains
  1. A link to the poster's profile page
  2. A link to the post's detail page
  3. A timestamp
  4. Details about how many pictures were uploaded with the post and how many comments and likes it has received
  5. A featured image. If users have uploaded pictures, one of these pictures is used, otherwise a placeholder is used.
  6. Buttons that allow users to easily share this post on Twitter and Facebook

  ![Example Timeline Card](/static/images/readme/example%20post.png)

### Post Detail Page

  * On the post detail page, users can read the whole post. When the poster has uploaded a picture, this is also shown below the post header consisting of the poster's username, the post title and the posts timestamp. When posters upload more than one picture, an additional image picker is shown where users can magnifiy each picture so that it can be viewed in large. Clicking a thumnail from the image picker essentially promotes this pictures to be the features picture.
  * Apart from the post itself, there's a like button for each post and a form where users can submit comments. Once comments have been posted, they are shown above the comment form.
  * The like button also shows the number of likes that the post has already received.
  * Post Detail pages are also viewable for users that are not logged in, i.e. if they found the post because it had been shared on Twitter or Facebook. For them, the like button incentivizes them to sign up or login so that they can leave a like, too.
  * On this page, the top menu contains an 'Edit this post' and a 'Delete this post' buttons for posts that the logged in user has posted.

### Circle Page

  * The Circle Page is a simple list of all users who the logged in user already follows. For each user a card is shown that contains the user's profile picture, their username, the number of posts they have created, their bio and an Unfollow button.
  * On this page, the top menu contains a 'Find more people to follow' button that enables users to add more people to their circle.
  * When users don't follow anybody yet (or anymore), e.g. right after they have signed up, the page shows a message than incentivizes them to add somebody to their circle.

### Find somebody to follow Page

  * Just like the Circle page, this shows a list of users, but here all users that the logged in users does not already follow are shown. The logged in user's account is also omitted.
  * Instead of an 'Unfollow' button as on the Circle Page, each user card contains a 'Follow' button here.

### Profile pages

  ![Example Profile Page](/static/images/readme/profilepage.png)
  
  * Profile pages show the respective user's uploaded profile picture at the top left and an info box with details about this user at the top right. If users have not uploaded a profile picture, a placeholder picture is shown instead.
  * The info box next to the profile picture contains the user's username, their join date, their locations (if provided), their age (if provided), their biography (if provided, if not a standardized message), the number of posts they have created, and the total number of likes and comments their posts have received. This should give interested users who look at these profile pages an idea of who the users they are looking at are as well as how popular they are.
  * Below profile picture and info box users will also find a card for each post this users has posted just as they would appear on the timeline page. If users like an another user's posts and they want to read more from the same author, the profile page gives them an easy way to find more content they are interested in, especially if they follow many users and their timeline get crowded.


## Future Implementations

### Admin section

  * A dedicated admin section that allows moderators to either greenlight content (both posts and comments) or, in the event that the content is problematic, edit or delete it. On a site like this that could potentially have hundreds of users, not showing content until a moderator has looked at it is impractical in my view, but it would still be great to moderate content after it has been published. Right now, this can be done through the admin section provided by Django, but allowing many people to access with sensitive part of the website is not a good idea from a security standpoint.

### Search function for both users and posts

  * In order to give users a better way to find content they are interested in, a search function could be implemented that filters through all posts and users, looking for keywords users have entered.

### Tag for posts and users

  * Users should be able to assign tags to themselves, their posts and possibly other people's profiles and posts. This data could then be used to interact with the search function or pages where users can view content based on specific tags. All of this would again serve the purpose of showing users more content that they are interested in. By assigning tags such as 'New' or 'Interesting', or even tags that are automatically assigned such as 'Hot' for posts that get a lot of views, one could create way to feature these posts in special sections that could draw all users' attentions.

### Automatically compress user uploaded images

  * This would save bandwidth and provide a better UX by loading pages more quickly.
  * It would also save storage space on the image server.

## Accessibility

I have tried to keep the website as accessible as possible by using semantic HTML elements, providing adequate contrast for fonts, using the alt attribute for images, the title attribute for links, etc. To further ensure that the site is accessible, I ran tests with the Web Accessibility Evaluation Tool (WAVE) and also used a Chrome browser extension called Web Disability Simulator. More on this in [Testing](#testing).

[Back to top](<#contents>)

# Technologies Used

## Languages Used

  * HTML5
  * CSS3
  * Javascript
  * Python 3

## Frameworks, Libraries & Programs Used

  * [Am I Responsive?](https://ui.dev/amiresponsive) - To showcase the website on all of the images used in this documentation file

  * [Bootstrap 5](https://getbootstrap.com/) - To create responsive websites

  * [Compressor.io](https://compressor.io) - To compress images

  * [Coolors.co](https://coolors.co/) - To create the color palette above

  * [Django](https://www.djangoproject.com/) - As my backend framework

  * [Favicon.io](https://favicon.io/) - To create a favicon

  * [Font Awesome](https://fontawesome.com/) - For the Restart and Off Button icons

  * [Git](https://git-scm.com/) - For version control

  * [GitHub](https://github.com) - To save and store my project files

  * [Google Fonts](https://fonts.google.com/) - To find and import fonts

  * [Google Dev Tools](https://developer.chrome.com/docs/devtools/) - To work out bugs, troubleshoot and test features and play around with property values and to test the website using the Lighthouse Test

  * [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) - To further ensure accessibility for all users

  [Back to top](<#contents>)


# Database Design

This ERD Chart shows the make up of the database this project is based on:

![ERD Chart](/static/images/readme/ERD%20Chart.jpg)

The User model is built into Django. Here, it is used mostly for the authentification process.

The SocialUser model is basically an extension of the User model. Its user key has a one-to-one relationship with the User model. The way it is set up, each time entries in the User model table are created or modified, entries in the SocialUser table are either created or updated as well, so they are kept in sync. This is accomplished with @receiver decorators in models.py. I learned how to do this reading this article: [How to Extend Django User Model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html) and opting for the second option.
The SocialUser model then expands the User model with fields that contain information that can be shown in the profile pages as well as a 'following' key that stores information on who the user is following. This information is stored as an array consisting of usernames.
The id key of this model has a one-to-many relationship with the author key in the Comment model, as each comment can only have one author. Here, the author key could instead also have the same relationship with the id key of the User model and it would not have made a big difference.

The Post model contains all the information that is needed for posts. The likes key has a many-to-many relationship with the User model's id key, as many posts and be liked by many users. The author key has a many-to-one relationship with the id key of the User model, as each post can only have one author.
In both of these cases I could also have used the id key of the SocialUser model and it would not have made a big difference, but this works, too.

The Comment model contains all the information that is needed for comments. Its post key has a many-to-one relationship with the Post model, as each comment is linked to only one post. Its author key has a many-to-one relationship with the User model's id key and it additionally has a author_social key that has the same relationship with the SocialUser model's id key. This seems redundant but was helpful when I struggled to retrieve the desired information in a specific situation. I guess this is a possible improvement, but it works and does not cause any problems apart from being a bit convoluted.


# AGILE Workflow



# Testing

## Validator Testing

### HTML and CSS



### Javascript

### Python

### Lighthouse Test

### WAVE Test

## Responsiveness Test

## Testing User Stories

[Back to top](<#contents>)

# Deployment

## Heroku

The steps were followed step by step exactly as mentioned in the Django Walkthrough project "I think therefore I blog". The write up attached [here](/static/images/readme/heroku_deployment_steps.pdf) was taken from a former CI student's Readme file.

# Credits

## Media

  * When I researched how to create an ERD chart for my database I found [a good tutorial](https://www.youtube.com/watch?v=QpdhBUYk7Kk) on LucidChart's own Youtube channel.

  * For all the pictures that are not user uploaded, I used resources I found on [undraw.co](https://undraw.co/). Specifically I used their SVGs called 'Teaching', 'Happy Feeling', 'Social interaction', 'Add post', 'Mobile User', 'Wall Post' and 'Login'.

  * For my Favicon, I used [favicon.io](https://favicon.io/favicon-generator/) where you can generate icons on the basis of letters.

## Code

  As this was my first Django project and the first time I used Bootstrap, I often searched the web for solutions to my problems. Here are the pages I have used and sometimes taken code from: 

  * Before I settled for an collapsible top menu bar, I had a permanently collapsed side bar in mind that users would trigger with a floating button. For this, I used [this tutorial](https://www.youtube.com/watch?v=x977EY47d-M).

  * When figuring out how to structure my database and specifically how to store more information about users, I found [this article](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html) that explained how to expand the User model that is built into Django.

  * The [Create A Simple Django Blog](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) by Codemy also proved very useful during this project.

  * To see how I following other users would work, I looked at [this Youtube Tutorial](https://www.youtube.com/watch?v=1tZg5YLsCO4).

  * As I wanted to created slugs automatically, I revised with [Stackoverflow article](https://stackoverflow.com/questions/50436658/how-to-auto-generate-slug-from-my-album-model-in-django-2-0-4).

  * Before I got a better understanding about how I could link directly to pages that were part of the allauth module, I used <base href=...> to solve my problems. I learned about relative paths in [this Stackoverflow article](https://stackoverflow.com/questions/24028561/relative-path-in-html), but could later on get rid of this because I found a better solution, which is importing LoginView and SignupView in my urls.py which I learned about [in this Stackoverflow article](https://stackoverflow.com/questions/38126241/over-riding-django-allauth-login-registration-urls-with-custom-url-pages).

  * For many small things, like styling a button so that it looks like a link, I again referred to Stackoverflow, e.g. [this article](https://stackoverflow.com/questions/1367409/how-to-make-button-look-like-a-link). I used this to style my logout button that can be found in the top menu when users click their username.

  * Revising how to filter objects from models and how to modify querysets I read both [this Stackoverflow article](https://stackoverflow.com/questions/33350362/django-listview-form-to-filter-and-sort) and [this page](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#listview) from the Django Documentation.

  * Looking for a way to order timelines by date, I found [another Stackoverflow article](https://stackoverflow.com/questions/431628/how-can-i-combine-two-or-more-querysets-in-a-django-view).

  * Trying to find ways for users to upload their custom pictures to their posts I read a lot of the [documentation provided by Cloudinary](https://cloudinary.com/documentation/django_integration) even though I feel that there is probably a more elegant way of doing what I have done. 

  * As there is so much to memorize I often have to rely on research to remember things that I have probably done in the past, e.g. extracting [parts of strings](https://stackoverflow.com/questions/5864485/how-can-i-split-this-comma-delimited-string-in-python). This was used when saving URLs from images that I stored on Cloudinary in the array field responsible for images in my Post model.

  * When implementing the share buttons with which users can share SocialBlog posts on Twitter or Facebook, I relied on this [cheat sheet for creating social media buttons](https://blog.hubspot.com/blog/tabid/6307/bid/29544/the-ultimate-cheat-sheet-for-creating-social-media-buttons.aspx)

  * Even though I had done this before in my Javascript project I had to look up how inserting elements into the DOM works again and found [a nice tutorial](https://www.tutorialspoint.com/how-to-add-a-new-element-to-html-dom-in-javascript).

  * As I wanted to set a user that every newly registered user follows automatically I found how that could work in [this Stackoverflow article](https://stackoverflow.com/questions/60779234/how-to-add-a-default-array-of-values-to-arrayfield) that explains how to set default values for array fields.
  
  [Back to top](<#contents>)

# Acknowledgements

I would like to thank the following people

* My wife for proofreading my work.

[Back to top](<#contents>)