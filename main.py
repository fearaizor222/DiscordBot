import json
from API import *
from Module import *
import lightbulb
from global_config import *
from lightbulb.ext import tasks

app = lightbulb.BotApp(
    token=config['token'],
    prefix='!'
)

app.load_extensions_from("Extensions")

tasks.load(app)
app.run()