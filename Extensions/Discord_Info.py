import lightbulb
from API import *
from Module import generateIdCard 
import requests
from global_configuration import *
import hikari
import os

plugin = lightbulb.Plugin('Info')

@plugin.command
@lightbulb.command("info", "Return info")
@lightbulb.implements(lightbulb.SlashCommand)
async def thisUserInfo(ctx: lightbulb.Context):
    try:
        sess = requests.Session()
        access_token = CLIENT['Users'].find_one({'discord_id': ctx.author.id})['access_token']
        sess.headers['authorization'] = f'bearer {access_token}'
        generateIdCard(requestInfo(sess))
        await ctx.respond(hikari.File('info.png', filename='info.png'))
        os.remove('info.png')
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        await ctx.respond('Timeout')
    except TypeError:
        await ctx.respond('You have not linked your account yet.')

@plugin.command
@lightbulb.command('whoami', 'Return UIS account that linked with your Discord account')
@lightbulb.implements(lightbulb.SlashCommand)
async def whoami(ctx: lightbulb.Context):
    try:
        sess = requests.Session()
        access_token = CLIENT['Users'].find_one({'discord_id': ctx.author.id})['access_token']
        sess.headers['authorization'] = f'bearer {access_token}'
        await ctx.respond(f'You are currently linked with {requestInfo(sess)["ma_sv"]}')
        sess.close()
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        await ctx.respond('Timeout')
    except TypeError:
        await ctx.respond('You have not linked your account yet.')

def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)