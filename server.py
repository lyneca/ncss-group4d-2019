# Import the flask library
from flask import Flask, request, jsonify

from restaurant import on_enter_state, on_input

# Create your web server
app = Flask(__name__)
state = "NO QUERY"
data = None
output = ""
# When people visit the home page '/'
@app.route('/')
def index():
  return 'Hello! I echo things back.'


# When we receive a request from Alexa
@app.route('/alexa', methods=['POST', 'GET'])
def alexa():
  global state, data, output
  output = ""
  print(state)
  alexa_request = request.get_json()['request']
  request_type = alexa_request['type']
  if request_type == 'LaunchRequest':
    state = 'NO QUERY'
    data = None
  elif request_type == 'IntentRequest':
    #get the user input
    request_intent = alexa_request['intent']
    intent_slots = request_intent['slots']
    query_slot = intent_slots['query']
    request_query = query_slot['value']

    state, data, output_on_input = on_input(state, request_query, data)
    if output_on_input:
      output += output_on_input
  
  output_on_enter = on_enter_state(state, data)

  if output_on_enter:
    output += output_on_enter
  
  end = False
  if state == 'END':
    state = 'NO QUERY'
    data = None
    end = True
  
  return jsonify({
    'version': '0.1',
    'response': {
      'outputSpeech': {
        'type': 'PlainText',
        'text': output,
      },
      'shouldEndSession': end,  # Keep the app alive
    }
  })


if __name__ == '__main__':
  # Start the web server!
  app.run(debug = True)
