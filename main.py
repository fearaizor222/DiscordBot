import json
from API import *
from Module import *
import lightbulb
from global_config import *

app = lightbulb.BotApp(
    token=config['token'],
    prefix='!'
)

app.load_extensions_from("Extensions")

app.run()