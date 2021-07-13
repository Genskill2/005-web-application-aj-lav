# Introduction

The repository contains a web app to manage a pet store. The following
features are supported

1. List of pets
1. Sorting pets by various fields (clicking on the headers)
1. Click on a pet id to see details.
1. Edit the pet to be change description
1. Edit the pet to change whether it's sold or not.
1. Click on a tag in the details page to see only pets which have that
   tag.
   
   
# Setting up

1. Clone repository
1. Create a virtualenv and activate it
1. Install dependencies using `pip install -r requirements.txt`
1. Setup application using `python setup.py develop`
1. `export FLASK_APP=petshop` to set the application
1. `flask initdb` to create the initial database
1. `flask run` to start the app.


You can also, instead of running the app, run the tests using `py.test`

# Tasks

The app is currently incomplete. These are marked in the source code
using `# TODO`. These tasks have to be completed for the app to work.

1. Enable sorting by all columns. Right now, only the id sorting works
   and all the other columns also sort by id.
1. Description is not displayed in the pet details page. This should
   be inside a `<p>` tag with `class` `description`. So something like
   this

         <p class="description"> 
             Description here
          </p>

1. It's not possible to mark a pet as sold now. This needs to be
   fixed.

