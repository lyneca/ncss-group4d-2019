import re
import random

'''
NO QUERY
DATE
LOCATION
MOVIE
RECOMMENDATIONS
GENRE
TOP RATED
'''



def on_enter_state(state, context):
  if state == 'NO QUERY':
    return no_query_on_enter_state(context)
  elif state == 'DATE':
    return movie_date_on_enter_state(context)
  elif state == 'LOCATION':
    return movie_location_on_enter_state(context)
  elif state == 'MOVIE':
    return movie_on_enter_state(context)
  elif state == 'RECOMMENDATIONS':
    return movie_recommendations_on_enter_state(context)
  elif state == 'GENRE':
    return movie_genre_on_enter_state(context)
  elif state == 'TOP RATED':
    return movie_toprated_on_enter_state(context)



def on_input(state, user_input, context):
  if state == 'NO QUERY':
    return no_query_on_input(user_input, context)
  elif state == 'DATE':
    return movie_date_on_input(user_input, context)
  elif state == 'LOCATION':
    return movie_location_on_input(user_input, context)
  elif state == 'MOVIE':
    return movie_on_input(user_input, context)
  elif state == 'RECOMMENDATIONS':
    return movie_recommendations_on_input(user_input, context)
  elif state == 'GENRE':
    return movie_genre_on_input(user_input, context)
  elif state == 'TOP RATED':
    return movie_toprated_on_input(user_input, context)






#no query state
def no_query_on_enter_state(context):
  return ""

def no_query_on_input(user_input, context):
  return 'DATE',{}, ''






#enter date state
def movie_date_on_enter_state(context):
  return "What day are you wanting to go?"

def movie_date_on_input(user_input, context):
    date=''
    if not date:
        return '','', None
    return 'LOCATION', {'date': date}, None





# movie_location
def movie_location_on_enter_state(context):
  return "What cinemas are you interested in"

def movie_location_on_input(user_input, context):
  return 'MOVIE', {}, None





# Movie state
def movie_on_enter_state(context):
  return "What are you interested in watching"

def movie_on_input(user_input, context):
  return 'END', {}, None





# recommendations
def movie_recommendations_on_enter_state(context):
  return "Here are the top rated movies for your location"  # FINISH

def movie_recommendations_on_input(user_input, context):
  return 'END', {}, None





# genre
def movie_genre_on_enter_state(context):
  return "What genre of movie do you want to watch"

def movie_genre_on_input(user_input, context):
  return 'END', {}, None





# top rated
def movie_toprated_on_enter_state(context):
  return 'Here are top rated movies for [LOCATION] and [GENRE]'

def movie_toprated_on_input(user_input, context):
  return 'END', {}, None



