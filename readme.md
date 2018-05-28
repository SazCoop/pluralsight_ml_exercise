##PluralSight

**Author: Sarah Cooper**
--Python 3.6
--IDE: PyCharm

*Exercise*

###Overview:

Code generates an API in FLASK that calculates the distance betwen users.
Distance Metric used is Cosine similarity due to Sparsity of rating matrix.

No explicit rating, create implicit rating matrix detailed below.

**Rating matrix is created by :**

*User Course Views Matrix:* Composite Key of Course Tags(Obtained through a joined to Course Name) and Level Rating matrix for each user is a mean of view_time_in_seconds for each course tag-level. 

*User Scores Matrix:* Rating Matrix for each user is mean of assessment score for each course tag.

*User Interest Matrix:* Rating Matrix for each user with count of interests by course tag.

*Rating Matrix:* 

Average of : *User Scores Matrix:* + *User Interest Matrix:* + *Rating Matrix:* not including when it is NAN/0

### Usage

1. Clone the project repository

`git clone https://github.com/SazCoop/pluralsight_ml_exercise.git`

2. Install python dependencies

`pip install -r requirements.txt`

3. Move Data files to Data/* obtained from pluralsight zip

4. CD to directory and run the server.py

`python server.py`

4. Use postman or curl to post to API running at localhost
*NOTE: First API Post will be slow, preparing matrix object*

` curl -H "Content-type: application/json" \ -X POST http://127.0.0.1:8000/nearest_users_post -d '{"user_id": X}, {"number_of_neighbours": X}`' `

###To improve

1. Set up in cloud - use docker to containerise the flask app.
2. Run docker in amazon ECS or azure kubernetes, obtain docker image from docker hub
3. Set up PostgresSQL database or SQLLite

###CodeBase: 

`Data/*` : files provided by pluralsight

    1. course_tags.csv
    2. user_assessment_scores.csv
    3. user_course_views.csv
    4. user_interests.csv

`Data/intermediate/*`: intermediate files folder created, matrix bject saved here

`Info/*` : information about exercise

    1. Information about exercise
    2. Exercise answers

`src/*` : codebase

    1. `Classes/*`: Helper functions and a Class for creating rating matrix
    2. `EDA/*`: Notebook with some adhoc EDA Scripts
    3. `Database/*`: Create Tables for the PostgresSQL database
    4. `tests/*: folder for unit_test.py
    4.  distance_function_main.py : Main Script that runs the distance metrics

`app/*`: flask app

    1.`templates/*` : folder to put template.html
    2. `server.py/*`:  generates post method to call the distance_function_main.py

`.gitignore`: not uploaded data or info to git

`requirements.txt` : requirements to run app