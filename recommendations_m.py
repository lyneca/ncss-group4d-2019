import re
import random
import dateparser 
import requests
import nltk.tokenize as nt
import nltk
'''
NO QUERY
DATE
LOCATION
MOVIE
RECOMMENDATIONS
GENRE
TOP RATED
'''

def find_locations(text):
  #ss=nt.sent_tokenize(text)
  #tokenized_sent=[nt.word_tokenize(sent) for sent in ss]
  #pos_sentences=[nltk.pos_tag(sent) for sent in tokenized_sent]
  #location=""
  #for word in pos_sentences:
  #  if word[1]=="NN":
  #    location+=word[0]+' '
  #print(pos_sentences)
  #location=location[:-1]
  return text#location
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
    date=dateparser.parse(user_input)
    if not date:
        return 'DATE',{}, None
    return 'LOCATION', {'date': date}, None





# movie_location
def movie_location_on_enter_state(context):
  return "What cinemas are you interested in"

def movie_location_on_input(user_input, context):
  
  location=find_locations(user_input)
  if not location:
      return 'LOCATION',context, None
  context["location"]=location
  return 'MOVIE', context, None





# Movie state
def movie_on_enter_state(context):
  return "What are you interested in watching"

def movie_on_input(user_input, context):   
  if "no idea" in user_input.lower() or "not sure" in user_input.lower():
     return 'RECOMMENDATIONS', context, None
  
  context["movie"]=re.search(r"(i.+(see|watch) )(?P<movie>.+)",user_input).group('movie')
  if context["movie"]:
      return 'BOOKING', context, None
  context["movie"]=user_input
  return 'BOOKING', context, None





# recommendations
def movie_recommendations_on_enter_state(context):
  out= "Here are the top rated movies for your location:"  # FINISH


  out+="Do you want to define by Genre?"
  return out


def movie_recommendations_on_input(user_input, context):
  if 'yes' in user_input.lower():
    return 'GENRE', context, None 
  context["movie"]=user_input
  return 'GENRE',context, None
  




# genre
def movie_genre_on_enter_state(context):
  return "What genre of movie do you want to watch"

def movie_genre_on_input(user_input, context):
  genre=user_input
  if not genre:
      return 'GENRE',context, None
  context["genre"]=genre
  return 'TOP RATED', context, None





# top rated
def movie_toprated_on_enter_state(context):
  data=requests.get('https://www.imdb.com/search/title?genres='+context['genre']).content.replace("\n",'')
  print(re.findall(r'''(?<=\?ref_=adv_li_tt\"\>).*(?=\<\/a\>)''',data))
  return 'Here are top rated movies for [LOCATION] and [GENRE]'

def movie_toprated_on_input(user_input, context):
  context["movie"]=user_input
  return 'BOOKING', context, None



if __name__=="__main__":
  state = 'NO QUERY'
  context = None

  while state != 'END':
    output = on_enter_state(state, context)
    if output:
      print(output)

    user_input = input('> ')
    state, context, output = on_input(state, user_input, context)
    if output:
      print(output)
