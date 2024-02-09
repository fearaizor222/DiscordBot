import lightbulb
from API import *
import requests
from global_config import *

plugin = lightbulb.Plugin('Info')

@plugin.command
@lightbulb.command("info", "Return info")
@lightbulb.implements(lightbulb.SlashCommand)
async def thisUserInfo(ctx: lightbulb.Context):
    try:
        sess = requests.Session()
        access_token = client['Users'].find_one({'discord_id': ctx.author.id})['access_token']
        if not access_token:
            raise TypeError
        sess.headers['authorization'] = f'bearer {access_token}'
        await ctx.respond(Info(sess)['ma_sv'])
        sess.close()
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        await ctx.respond('Timeout')
    except TypeError:
        await ctx.respond('You have not linked your account yet.')

def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)