# -*- coding: utf-8 -*-
"""
@author: Sarah
"""

import os
import pandas as pd
import numpy as np
from os.path import normpath, basename

root = ".."
os.chdir(root)
root = os.getcwd()
from src.Classes.matrix_class import DistanceMatrixClass
root = "Documents/pluralsight_ml_exercise/pluralsight_ml_exercise"

def setdir():
    os.chdir(root)
    print(os.getcwd())

def configure():
    course_tags = pd.read_csv('Data/course_tags.csv')
    user_scores = pd.read_csv('Data/user_assessment_scores.csv')
    user_views = pd.read_csv('Data/user_course_views.csv')
    user_interests = pd.read_csv('Data/user_interests.csv')
    user_views = user_views.merge(course_tags, on="course_id", how="left")
    user_views["level_course"] = user_views["level"].map(str) + "_" + user_views["course_tags"].map(str)
    return (user_views, user_scores, user_interests)


def prepare_rating_matrix():
    user_views, user_scores, user_interests = configure()
    ##get users in data
    int_users = list(user_interests['user_handle'].unique())
    scores_users = list(user_scores['user_handle'].unique())
    views_users = list(user_views['user_handle'].unique())
    total_users = list(set(int_users + scores_users + views_users))
    total_users.sort()
    total_users = np.array(total_users)
    ##for each matrix create rating matrix
    os.makedirs("Data/intermediate", exist_ok=True)
    # INTEREST
    user_int_class = DistanceMatrixClass(user_interests, 'user_handle', total_users)
    rating_matrix = user_int_class.frametoratingmatrix(['date_followed'], 'interest_tag', len)
    int_m = user_int_class.calculate_similarity(rating_matrix)
    np.save("Data/intermediate/rating_matrix_int", int_m)

    # VIEWS
    user_int_class = DistanceMatrixClass(user_views, 'user_handle', total_users)
    rating_matrix = user_int_class.frametoratingmatrix(
        ['view_date', 'author_handle', 'course_id', 'course_tags', 'level'], 'level_course', np.mean)
    views_m = user_int_class.calculate_similarity(rating_matrix)
    np.save("Data/intermediate/rating_matrix_view", views_m)

    # SCORES
    user_int_class = DistanceMatrixClass(user_scores, 'user_handle', total_users)
    rating_matrix = user_int_class.frametoratingmatrix(['user_assessment_date'], 'assessment_tag', np.mean)
    score_m = user_int_class.calculate_similarity(rating_matrix)
    np.save("Data/intermediate/rating_matrix_score", score_m)

def join_similarities(matrix_list):
    """
    Join_similarities
    Takes a list of rating matrixes, creates a 3D matrix and gets matrix, rowwise

    Parameters
    ----------
    rating_matrix : DataFrame
          DataFrame as rating matrix
    Returns
    -------
    matrix_mean: Matrix
          Matrix of Means: Final Rating Matrix

    """
    m = np.array(matrix_list)
    del matrix_list
    matrix_mean = np.nanmean(m, axis=0)
    return matrix_mean

def createfinalmatrix():
    int_m = np.load("Data/intermediate/rating_matrix_score.npy")
    views_m = np.load("Data/intermediate/rating_matrix_view.npy")
    score_m = np.load("Data/intermediate/rating_matrix_int.npy")
    # CREATE FINAL MATRIX
    matrix_list = [int_m, views_m, score_m]
    del (int_m, views_m, score_m)
    rating_matrix = join_similarities(matrix_list)
    np.save("Data/intermediate/rating_matrix", rating_matrix)


def nearest_users(user_id, number_of_neighbours):
    if ((basename(normpath(os.getcwd()))) != 'pluralsight_ml_exercise'):
        setdir()
    matrix_list = ["rating_matrix_int.npy", "rating_matrix_score.npy", "rating_matrix_view.npy"]
    array_list = []
    for m in matrix_list:
        matrix = "Data/intermediate/%s" % m
        if os.path.exists(matrix):
            rating_matrix_1 = np.load(matrix)
        else:
            prepare_rating_matrix()
            createfinalmatrix()
            rating_matrix_1 = np.load(matrix)
        try:
            # index starts at 0 so add 1
            rating_matrix_1 = rating_matrix_1[(user_id - 1), ]
        except:
            print("User does not exist in data")


        array_list.append(rating_matrix_1)
        del(rating_matrix_1)
    rating_matrix = join_similarities(array_list)
    rating_matrix[np.isnan(rating_matrix)] = 0
    nearest_users_i = np.argsort(rating_matrix)[::-1][:number_of_neighbours]
    nearest_users_i = ' '.join(str(v) for v in nearest_users_i)
    nearest_users_i = str(nearest_users_i)
    print(nearest_users_i)
    return nearest_users_i
