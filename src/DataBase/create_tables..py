# -*- coding: utf-8 -*-
##IN PROGRESS

import psycopg2
from config import config
 
 
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE user_interests (
            user_handle INTEGER ,
            interest_tag TEXT,
            date_followed TIMESTAMP,
            PRIMARY KEY (user_handle, interest_tag)
        )
        """,
        """ CREATE TABLE user_course_views (
                user_handle ​INTEGER ,
                view_date TIMESTAMP,
                course_name TEXT,
                author_handle INTEGER<
                level TEXT,
                course_view_time_seconds INTEGER,
                PRIMARY KEY (user_handle, view_date, course_name)
                )
        """,
        """
        CREATE TABLE course_tags (
            course_id INTEGER PRIMARY KEY,
            course_tags TEXT
        )
        """,
        """
        CREATE TABLE user_assessment_scores (
            user_handle INTEGER,
            user_assessment_date TIMESTAMP,
            assessment_tag TEXT,​ 
            user_assessment_score INTEGER,
            PRIMARY KEY (user_handle, assessment_date, user_assessment_score)
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    create_tables()
