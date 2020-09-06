# Twitterclone -- attack of the Kenzie clones!

## Overview

Here's my version of a Twitter 'clone' application, using Django and meeting all of the rubric requirements for this Q-4 project at Kenzie Academy.

Just like the original Twitter, this app allows you to post 140-character "Tweets" for your followers to see. Each post is marked with a time stamp.

Create a profile page with an "About Me" section and an image. Follow other users to see their posts, and tag users to bring their attention to your posts. Edit your posts, and your profile. Even delete them, if you must.

Feel free to invite non-logged in, non-users, to view your profile and your individual posts, gaining you more potential followers, and more traffic to your page.

## Details of features

If you try to access the homepage without logging in, you will be directed to a login page, which also includes a link to the signup page, in case you don't already have an account. Signing up for an account will log you in automatically.

The homepage lists all of your “Tweets,” along with the posts of the people you are following. A list of users who you are NOT following will also appear on the homepage, so you can browse to see if there’s anyone you might want to connect with. Click on the link to see a list of your "connections", including a bit about them and their profile pic.

You can easily choose to "follow" or "unfollow" other users with the buttons on their profile pages. If you follow them already, the only option will be to "unfollow", while if you are not following them yet, only the "follow" button will appear on the page.

Your profile page shows whether you have "notifications" -- if you have them, it will provide a link taking you to a page listing the messages you are tagged in. Viewing this page will then clear the page and show no notifications. The posts will still appear on your homepage post feed, if they are from one of your "connections."

To send notifications, simply create a Twitterclone, and include the '@' symbol, followed by the user's "display name".

Profile pages list only that user's posts, plus the count of total posts made by that user. The information on this page is visible to anyone, whether logged into the program or not. It can be accessed directly, using the "display name" in the URL.

To see how many people that user is following, or to follow/unfollow them, you must be logged in. A link to create a post -- which will send you to the log in page first -- is included on the profile.

Users who are not logged in can also view a detailed page for each of your posts, with a link to your profile. This way, you can gain new followers by attracting them to your posts!

## Work in progress

Still need to add some styling and formatting to the project! I'm hoping to also add some screenshots. 

I am already working on an updated version, and have some ideas for fetaures I'd like to add/improve. As I grow my Django skills, hopefully the functionality of my Twitterclone will grow as well.

Once changes are made, the repo and this README will be updated. Stay tuned!

## Requirements
Python 3.8.5
Django 3.1
Poetry >= 0.12

## Authors

Assistance provided by instructors and facilitators at Kenzie Academy. Special shout-outs to Joe and Matt!

## Support

Any comments regarding problems with this application, or general feedback, can be directed to: pokeyjess72@gmail.com

Thanks for checking out my project!
