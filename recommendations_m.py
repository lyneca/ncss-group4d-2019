import re
import random

def on_enter_state(state, context):
  if state == 'NO QUERY':
    return no_query_on_enter_state(context)
  elif state == '':
    return (context)



def on_input(state, user_input, context):
  if state == 'NO QUERY':
    return no_query_on_input(user_input, context)
  elif state == '':
    return (user_input, context)



#no query state
def no_query_on_enter_state(context):
  return ""

def no_query_on_input(user_input, context):
  # Store the full response text as the location.
  location = user_input
  return 'LOCKED OUT LOCATION', {'location': location}, None






#enter date state
def movie_date_on_enter_state(context):
  return "What day are you wanting to go?"

def movie_date_on_input(user_input, context):
  # Store the full response text as the location.
  location = user_input
  return 'LOCKED OUT LOCATION', {'location': location}, None





# movie_location
def movie_location_on_enter_state(context):
  return "What cinemas are you interested in"

def movie_location_on_input(user_input, context):
  return 'END', {}, 'Bye!'





# Movie state
def movie_on_enter_state(context):
  return "What are you interested in watching"

def movie_on_input(user_input, context):
  return 'END', {}, 'Bye!'





# recommendations
def recommendations_on_enter_state(context):
  return "Here are the top rated movies for your location"  # FINISH

def recommendations_on_input(user_input, context):
  return 'END', {}, 'Bye!'





# genre
def genre_on_enter_state(context):
  return "What genre of movie do you want to watch"

def genre_on_input(user_input, context):
  return 'END', {}, 'Bye!'





# top rated
def top_rated_on_enter_state(context):
  return 'Here are top rated movies for [LOCATION] and [GENRE]'

def top_rated_on_input(user_input, context):
  return 'END', {}, 'Bye!'



