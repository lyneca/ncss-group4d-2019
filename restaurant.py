import re
import random
import requests

# API KEY // da1bbf6f7e8f95d9ec57b83ab810f46c

headers = {
    'Accept': 'application/json',
    'user-key': 'da1bbf6f7e8f95d9ec57b83ab810f46c',
}

ERROR_CODE = "Sorry, I couldn't understand what you are saying"

RETURN_VALUES = {
    "NO QUERY": [
        "Hello",
        "How can I help you?",
        "What's up?",
        "What do you want to aquire?",
    ],

    "DATE": [
        "When are you wanting to go out?",
        "When would you like to go?",
        "What day are you wanting to go?",
    ],

    "LOCATION": [
        "Where are you wanting to eat out?",
        "Where abouts are you wanting to go?",
    ],

    "FOOD": [
        "What would you like to eat?",
        "What do you feeling like eating?",
    ],

    "RECOMMEND": [
        "I'm currently listing recommend foods for your area",
        "I hope these recommendations can satisfy you",
        "Here are some recommendations because you can't make up your mind",
    ],

    "MEAL": [
        "Breakfast, lunch or dinner?",
        "What time of day are you wanting to go?",
    ],

    "DEFINE": [
        "Here are meal recommendations for your preference",
        "Showing menu's for your time of day",
    ],

    "BOOKING": [
        "Now you can book your event",
        "Have fun"
    ]
}


NO_QUERY_STATE = random.choice(RETURN_VALUES["NO QUERY"])


def on_enter_state(state, context):
    if state == "NO QUERY":
        return no_query_on_enter_state(context)
    elif state == "DATE":
        return date_on_enter_state(context)
    elif state == "LOCATION":
        return location_on_enter_state(context)
    elif state == "FOOD":
        return food_on_enter_state(context)
    elif state == "RECOMMEND":
        return recommend_on_enter_state(context)
    elif state == "MEAL":
        return meal_on_enter_state(context)
    elif state == "DEFINE":
        return define_on_enter_state(context)
    elif state == "BOOKING":
        return "BOOKING"

def on_input(state, user_input, context):
    if state == "NO QUERY":
        return no_query_on_input(user_input, context)
    elif state == "DATE":
        return date_on_input(user_input, context)
    elif state == "LOCATION":
        return location_on_input(user_input, context)
    elif state == "FOOD":
        return food_on_input(user_input, context)
    elif state == "RECOMMEND":
        return recommend_on_input(user_input, context)
    elif state == "MEAL":
        return meal_on_input(user_input, context)
    elif state == "DEFINE":
        return define_on_input(user_input, context)

def no_query_on_enter_state(context):
    return "Hello! I am restaurant helper bot"

def no_query_on_input(user_input, context):
    return "DATE", {}, None    

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
    match = re.match('^(i want |i would like )?(?P<food>\w+)$', user_input, re.I)
    match_elif = re.match("^(i am not sure|i don't know|i have no clue)$", user_input, re.I)
    if match:
        context['food'] = match.group['food']
        return 'BOOKING', context, None
    elif match_elif:
        return 'RECOMMEND', context, None
    else:
        return "FOOD", context, ERROR_CODE

def recommend_on_enter_state(context):

    params = (
        ('entity_id', '260'),
        ('entity_type', 'city'),
        ('cuisines', '152'),
        ('sort', 'rating'),
        ('order', 'desc'),
        ('count', 5)
    )

    response = requests.get('https://developers.zomato.com/api/v2.1/search', headers=headers, params=params).json()

    names = [x["restaurant"]["name"] for x in response["restaurants"]]

    return f'Here are some recommendations. What would you like? {names}'

    # more code coming



def recommend_on_input(user_input, context):
    match_yes = re.match('^(i would like to eat |i would like )?(?P<meal>\w+)$', user_input, re.I)
    if user_input.startswith('No' | 'no'):
        return "FOOD", context, None
    elif match_yes:
        if user_input in names:
            context['meal'] = match.group['meal']
        else:
            return "RECOMMEND", context, ERROR_CODE
        return "BOOKING", context, None
    else:
        return "RECOMMEND", context, ERROR_CODE

def meal_on_enter_state(context):
    return "Would you like breakfast, lunch or dinner?"

def meal_on_input(user_input, context):
        context["meal type"] = user_input
        return "DEFINE", context, None
    
def define_on_enter_state(context):
    return f"Here are the top meals for {context['meal type']}:"

    # more coding coming

def define_on_input(user_input, context):
    context['meal'] = user_input
    return "BOOKING", context, None





