# Portfolio webpage with personal blog

![Project Image](https://i.ibb.co/CQ2yNY2/folio.png)

The goal of this project was to create a perfonal portfolio featuring various projects that I have worked on. The webpage should list various projects, allow for a detail page of such projects, a personal blog, as well as easy management of projects and blog posts via an admin interface.

### User Information

```
username: admin
password: admin
```
### Admin Edits

Website administrator should first log in via the Django login pannel at localhost:8000/admin
Once logged in as admin going back to the home page should enable edit options throughout the website

![Admin Edits](https://i.ibb.co/ZgjW39k/edinoedit.png)

### Folder Structure
```
|   .gitignore                  # Git ignore configurations
|   README.md                   # This File
|   requirements.txt            # Project Dependacies
|       
└───portfolio                   # Main project folder
    |   db.sqlite3              # Project Database
    |   manage.py               # Django main file
    |   
    ├───blog                    # Blog application folder
    |   |   admin.py            # Blog admin model registration
    |   |   apps.py             # App configutation
    |   |   models.py           # Blog Models definitions
    |   |   tests.py            # Empty
    |   |   urls.py             # Blog URL definitions
    |   |   views.py            # Blog views definitions
    |   |   __init__.py
    |   |   
    |   ├────migrations         # App migrations folder, Not pushed to Git
    |   ├────templates          # Templates folder
    |   |   └───blog            # App name subfolder (Convention)
    |   |           blog.html   # Blog template (Diplays one entry)
    |   |           index.html  # Blog homepage (Display multiple entries)
    |   | 
    ├───folio                   # Portfolio application folder
    |   |   admin.py            # Porfolio admin model registration
    |   |   apps.py             # App configuration
    |   |   models.py           # Portfolio Models definitions
    |   |   tests.py            # Empty
    |   |   urls.py             # Portfolio URL definitions
    |   |   views.py            # Portfolio  views definitions
    |   |   __init__.py
    |   |   
    |   ├───migrations          # App migrations folder, Not pushed to Git
    |   ├───static              # Static files folder
    |   |   └───folio           # App name subfolder (Convention)
    |   |           jeff.jpg
    |   |           script.js
    |   |           style.css         
    |   ├───templates           # Templates folder
    |   |   └───folio           # App name subfolder (Convention)
    |   |           about.html  # About (Bio) template
    |   |           folio.html  # Portfolio template (Displays one entry)
    |   |           index.html  # Portfolio homepage (Displays multiple entries)       
    ├───portfolio               # Main project configuration folder
    |   |   settings.py
    |   |   urls.py             
    |   |   wsgi.py
    |   |   __init__.py
    |   |          
    └───templates               # Global templates folder 
            base.html           # Common template used across multiple apps
```