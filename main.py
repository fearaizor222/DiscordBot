from API import *
from Module import *
import lightbulb
from global_configuration import *
from lightbulb.ext import tasks

app = lightbulb.BotApp(
    token=CONFIG['token'],
    prefix='!'
)

app.load_extensions_from("Extensions")

tasks.load(app)
app.run()