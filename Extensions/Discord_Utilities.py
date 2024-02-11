import lightbulb
from API import *
import requests
from global_configuration import *
from lightbulb.ext import tasks

plugin = lightbulb.Plugin('Utilities')


@plugin.command
@lightbulb.option("password", "Your UIS password")
@lightbulb.option("username", "Your UIS username")
@lightbulb.command("link", "Link your Discord account with your UIS account")
@lightbulb.implements(lightbulb.SlashCommand)
async def link(ctx: lightbulb.Context):
    try:
        sess = requests.Session()
        access, refresh = requestLogin(sess, {
            'username': ctx.options.username,
            'password': ctx.options.password,
            'grant_type': 'password'
        })

        if access:
            if CLIENT['Users'].find_one({'discord_id': ctx.author.id}):
                CLIENT['Users'].update_one({'discord_id': ctx.author.id}, {'$set': {'access_token': access, 'refresh_token': refresh}})
                await ctx.respond('Overwrited your linked account.')
            else:
                CLIENT['Users'].insert_one({'discord_id': ctx.author.id, 'access_token': access,
                                            'refresh_token': refresh})
                await ctx.respond('Linked your account.')
        else:
            await ctx.respond('Linking failed. Please check your username and password.')

        sess.close()

    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        await ctx.respond('Your request was timeout')


@plugin.command
@lightbulb.command("unlink", "Unlink your Discord account with your UIS account")
@lightbulb.implements(lightbulb.SlashCommand)
async def unlink(ctx: lightbulb.Context):
    result = CLIENT['Users'].delete_one({'discord_id': ctx.author.id})
    if result.deleted_count:
        await ctx.respond('Unlinked your account.')
    else:
        await ctx.respond('You have not linked your account yet.')


@tasks.task(m=90, auto_start=True)
async def refresh():
    for user in CLIENT['Users'].find({}, {'_id': False}):
        try:
            refreshToken(user['discord_id'])
            print('refresh for user', user['discord_id'],)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as err:
            print(err)


def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)
