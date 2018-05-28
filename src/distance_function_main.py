# -*- coding: utf-8 -*-
"""
Created on Sun May 27 20:44:33 2018

@author: Sarah
"""

from matrix_class import DistanceMatrixClass
import os
import pandas as pd
import numpy as np

root = "C:/Users/Sarah/Documents/pluralsight_ml_exercise"
def configure(root):
    os.chdir(root)
    course_tags = pd.read_csv('data/course_tags.csv')
    user_scores = pd.read_csv('data/user_assessment_scores.csv')
    user_views = pd.read_csv('data/user_course_views.csv')
    user_interests = pd.read_csv('data/user_interests.csv')
    user_views = user_views.merge(course_tags, on="course_id", how = "left")
    user_views["level_course"] = user_views["level"].map(str) + "_" + user_views["course_tags"].map(str)
    return(user_views, user_scores, user_interests)
    
    
def prepare_rating_matrix():
    user_views, user_scores, user_interests = configure(root)
    ##get users in data
    int_users = list(user_interests['user_handle'].unique())
    scores_users = list(user_scores['user_handle'].unique())
    views_users = list(user_views['user_handle'].unique())
    total_users = list(set(int_users + scores_users + views_users))
    total_users.sort()
    total_users= np.array(total_users)
    ##for each matrix create rating matrix
    
    #INTEREST
    user_int_class = DistanceMatrixClass(user_interests, 'user_handle', total_users)
    rating_matrix = user_int_class.frametoratingmatrix('date_followed', 'interest_tag', len)
    int_m = user_int_class.calculate_similarity(rating_matrix)    
    
    #VIEWS
    user_int_class = DistanceMatrixClass(user_views, 'user_handle', total_users)
    rating_matrix = user_int_class.frametoratingmatrix(['view_date','author_handle','course_id','course_tags','level'], 'level_course', np.mean)
    views_m = user_int_class.calculate_similarity(rating_matrix) 
    
    #SCORES
    user_int_class = DistanceMatrixClass(user_scores, 'user_handle', total_users)
    rating_matrix = user_int_class.frametoratingmatrix('user_assessment_date', 'assessment_tag', np.mean)
    score_m = user_int_class.calculate_similarity(rating_matrix) 
    
    #CREATE FINAL MATRIX
    matrix_list =[int_m, views_m, score_m]
    rating_matrix = user_int_class.join_similarities(matrix_list)
    os.makedirs("data/intermediate", exist_ok=True)
    rating_matrix.dump("data/intermediate/rating_matrix.dat")
    
def nearest_users(user_id, number_of_neighbours):
    matrix  = "%s/data/intermediate/rating_matrix.dat" % root
    if os.path.exists(matrix):
        rating_matrix = np.load(matrix)
    else:
        prepare_rating_matrix()
        rating_matrix = np.load(matrix)
    print(rating_matrix)
    
    
nearest_users(1)
    
        
        
        