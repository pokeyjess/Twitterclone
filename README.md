# Twitterclone -- attack of the Kenzie clones!

## Overview

Here's my version of a Twitter 'clone' application, using Django and meeting all of the rubric requirements for this Q-4 project at Kenzie Academy.

Just like the original Twitter, this app allows you to post 140-character "Tweets" for your followers to see. Each post is marked with a time stamp.

Create a profile page with an "About Me" section and an image. Follow other users to see their posts, and tag users to bring their attention to your posts. Edit your posts, and your profile. Even delete them, if you must.

Feel free to invite non-logged in, non-users, to view your profile and your individual posts, gaining you more potential followers, and more traffic to your page.

## Details of features

<img width="901" alt="Screen Shot 2020-09-07 at 11 25 15 PM" src="https://user-images.githubusercontent.com/65363804/92431322-387e1780-f165-11ea-8157-4385e751a24f.png">

If you try to access the homepage without logging in, you will be directed to a login page, which also includes a link to the signup page, in case you don't already have an account. Signing up for an account will log you in automatically.

The homepage lists all of your “Tweets,” along with the posts of the people you are following. 

<img width="937" alt="Screen Shot 2020-09-07 at 11 14 27 PM" src="https://user-images.githubusercontent.com/65363804/92431275-171d2b80-f165-11ea-996d-4bed6b86e413.png">

From the navigation bar, which appears on all of the pages, you can: go to your profile, return to your newsfeed, create a new Twitterclone or log out of the app. Two separate lists are also available from the navigation bar -- a list of users you are currently following, and a list of ones you have not yet "followed.

<img width="813" alt="Screen Shot 2020-09-07 at 10 57 38 PM" src="https://user-images.githubusercontent.com/65363804/92431746-408a8700-f166-11ea-8a62-ee4c589b5657.png">

You can easily choose to "follow" or "unfollow" other users with the buttons on their profile pages. If you follow them already, the only option will be to "unfollow", while if you are not following them yet, only the "follow" button will appear on the page.

If you have notifications, a bell will appear to the very right of the navigation bar, with a count of how many notifications you have. If there are no notifications, an "X" will appear instead. Both link to a page listing the messages you have been tagged in, with the notifications automatically clearing when you visit this page.

<img width="196" alt="Screen Shot 2020-09-07 at 10 56 11 PM" src="https://user-images.githubusercontent.com/65363804/92431665-11741580-f166-11ea-8291-c4ab27354b14.png">

To send notifications, simply create a Twitterclone, and include the '@' symbol, followed by the user's "display name".

Profile pages list only that user's posts, plus the count of total posts made by that user. You will see edit and trash icons on your own profile and post pages. Delete functions are equipped with basic JavaScript alerts, and further controls are in place to prevent staff members from deleting their accounts.

<img width="580" alt="Screen Shot 2020-09-07 at 11 27 45 PM" src="https://user-images.githubusercontent.com/65363804/92432185-767c3b00-f167-11ea-8dc2-e9a44a3d6945.png">

The information on the profile page is visible to anyone, whether logged into the program or not. It can be accessed directly, using the "display name" in the URL.

To see how many people that user is following, or to follow/unfollow them, you must be logged in. A link to create a post -- which will send you to the log in page first -- is included on the profile.

Users who are not logged in can also view a detailed page for each of your posts, with a link to your profile. This way, you can gain new followers by attracting them to your posts!

## Work in progress
 
I am already working on an updated version, and have some ideas for features I'd like to add/improve. There are also a couple of potential bugs I need to figure out. As I grow my Django skills, hopefully the functionality of my Twitterclone will grow as well. I am open to suggestions!

Once changes are made, the repo and this README will be updated. Stay tuned!

## Requirements
Python 3.8.5
Django 3.1
Poetry >= 0.12

## Authors

Assistance provided by the instructors and facilitators at Kenzie Academy. Special shout-outs to Joe and Matt! Stackoverflow was an invaluable resource while working through all the bugs.

In keeping with the theme of "clones," I drew inspiration for the style of this project from Star Wars: Attack of the Clones (no longer the second-worst movie in the franchise!). Colors were designed to match the palette found here: https://www.vox.com/culture/2015/12/17/10322514/star-wars-colors.

## Support

Any comments regarding problems with this application, or general feedback, can be directed to: pokeyjess72@gmail.com

Thanks for checking out my project!
