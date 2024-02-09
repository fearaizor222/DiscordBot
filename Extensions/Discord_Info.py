import lightbulb
from API import *
import requests
from global_config import *
import hikari

plugin = lightbulb.Plugin('Info')

@plugin.command
@lightbulb.command("info", "Return info")
@lightbulb.implements(lightbulb.SlashCommand)
async def thisUserInfo(ctx: lightbulb.Context):
    try:
        sess = requests.Session()
        access_token = client['Users'].find_one({'discord_id': ctx.author.id})['access_token']
        sess.headers['authorization'] = f'bearer {access_token}'
        data = Info(sess)
        embed = hikari.Embed(
            title=f'Thông tin sinh viên {data["ma_sv"]}',
            description=f'**Họ và tên:** {data["ten_day_du"]}'
        )
        embed.set_image(data['image'])
        await ctx.respond(embed=embed)
        sess.close()
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
        access_token = client['Users'].find_one({'discord_id': ctx.author.id})['access_token']
        sess.headers['authorization'] = f'bearer {access_token}'
        await ctx.respond(f'You are currently linked with {Info(sess)["ma_sv"]}')
        sess.close()
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        await ctx.respond('Timeout')
    except TypeError:
        await ctx.respond('You have not linked your account yet.')

def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)