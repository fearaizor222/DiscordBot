import lightbulb
from API import *
import requests

plugin = lightbulb.Plugin('Info')

@plugin.command
@lightbulb.command("info", "Return info")
@lightbulb.implements(lightbulb.SlashCommand)
async def thisUserInfo(ctx: lightbulb.Context):
    try:
        with requests.Session() as sess:
            Login(sess,{
                'username': 'N21DCCN165',
                'password': '25092003',
                'grant_type': 'password'
            })

            await ctx.respond(Info(sess)['ma_sv'])
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        await ctx.respond('Timeout')

def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)