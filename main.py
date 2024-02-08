import json
from API import *
from Module import *
import lightbulb

additional_data = ''
with open('Additional_Data.json', 'r') as file:
    additional_data = json.load(file)

app = lightbulb.BotApp(
    token=additional_data['token'],
    prefix='!'
)

app.load_extensions_from("Extensions")

app.run()