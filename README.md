# Overview

This program was primarily written to help me have exposure to cloudbased databases.

Eventually I would like to attach the database to an app that will allow me to have access to recipies and share recipies with others.

My program allows the user to read, write, and modify the database. It will display options for what the user can do and based
on the user selection and input it will make adjustmets to the database or display the database.

[Software Demo Video](https://www.youtube.com/watch?v=s14PYIVBKV8)

# Cloud Database

This database is stored in Google's firebase cloud storage.

The database has the tabe which is the meal type i.e. Breafast, Dessert, ect...

It then has the recipe and within the recipe it has the ingredients and quantity of ingredients


# Development Environment

I used VS Code using Python and Googles firebase site to store my database

Python includes most functionality with its built in library so the only libraries I needed were the ones that
I used to link to the data base.

Libraries Used:
- firebase_admin: Allows user to access google firebase libraries 
    - credentials: Finds specifc database
    - firestore: Allows user to access database

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Firebase How to Query](https://firebase.google.com/docs/firestore/query-data/queries#array_membership)
- [Free Code Camp How to use firebase with python](https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/)
- [How NoSQL databases work](https://www.guru99.com/nosql-tutorial.html)

# Future Work

- Reformat Ingredients to allow query for specific ingredients
- Attach database to App
- Allow user to query multiple tables at once
- Increase database library
