import re
import random


def on_enter_state(state, context):
    if state == "NO QUERY":
        return 

def on_input(state, user_input, context):








def no_query_on_enter_state(context):
    return "Hello! I am restaurant helper bot"

def no_query_on_input(user_input, context):
    return "DATE STATE", {}, None    

def date_on_enter_state(context):
    return "What day are you wanting to go?"
    
def date_on_input(user_input, context):
    context['date'] = user_input
    return 'LOCATION', context, None

def location_on_enter_state(context):
    return 'Where are you wanting to eat'

def location_on_input(user_input, context):
    context['location'] = user_input
    return 'FOOD', context, None

def food_on_enter_state(context):
    return 'What would you like to eat?'

def food_on_input(user_input, context):
    if user_input.startswith('I want to eat'):
        context['food'] = user_input[len('I want to eat'):]
        return 'BOOKING', context, None
    elif user_input == "i'm not sure":
        return 'RECOMMEND', context, None
    else:
        return 'Sorry I didn\'t understand that', context, None

def recommend_on_enter_state(context):
    return 'Here are some recommendations. What would you like?'

    # more code coming 





def recommend_on_input(user_input, context):
    if user_input.startswith('No'):
        return "FOOD", context, None
    elif user_input.startswith("Yes, I would like to eat"):
        context['meal'] = user_input[len("I would like to eat")]
        return "MEAL", context, None
    else:
        return "Sorry I didn\'t understand that", context, None
    
