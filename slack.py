from flask import Flask, jsonify, request
from bot import on_enter_state, on_input

app = Flask(__name__)

state = 'NO QUERY'
context = {}

@app.route('/slack/slash', methods=['GET', 'POST'])
def slack_slash():
  global state, context
  payload = request.values
  print(payload)  # Print payload for debugging.

  if payload:
    user_input = payload.get('text')

    # todo: finish this slack interface!
@app.route('/slack/event', methods=['GET', 'POST'])
def slack_event():
  json=request.json
  if 'challenge' in json:
    return json["challenge"]
if __name__ == '__main__':
  app.run()
