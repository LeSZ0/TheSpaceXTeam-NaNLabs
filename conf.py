import os

trello_url = 'https://api.trello.com/1'

token = os.environ.get('TRELLO_TOKEN')
app_key = os.environ.get('TRELLO_APP_KEY')
board_id = os.environ.get('TRELLO_BOARD_ID')

query_params = {"token": token, "key": app_key}

