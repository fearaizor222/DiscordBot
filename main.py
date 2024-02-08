import requests
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

@app.command
@lightbulb.command('info', 'return info')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context):
    with requests.Session() as sess:
        login_data = {
            'username': 'n21dccn165',
            'password': '25092003',
            'grant_type': 'password'
        }
        Login(sess, login_data)

        await ctx.respond(Info(sess)['ma_sv'])

app.run()