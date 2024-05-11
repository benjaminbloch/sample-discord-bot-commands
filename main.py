from discord.ext import commands
import discord
import sys
import os
import time
import random
from dotenv import load_dotenv


# Loads the .env file that resides on the same level as the script.
load_dotenv()

# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Creates a new Bot object with a specified prefix. It can be whatever you want it to be.
bot = commands.Bot(command_prefix="$")

# on_message() event listener. Notice it is using @bot.event as opposed to @bot.command().
@bot.event
async def on_message(message):
	# Check if the message sent to the channel is "hello".
	if message.content == "hello":
		# Sends a message to the channel.
		await message.channel.send("pies are better than cakes. change my mind.")

	# Includes the commands for the bot. Without this line, you cannot trigger your commands.
	await bot.process_commands(message)

# Command $ping. Invokes only when the message "$ping" is send in the Discord server.
@bot.command()
async def start(ctx):
  await ctx.send(f"Hello. I am going to help you today. To start, pick what item you want to buy. once ready please run the command !ready")
@bot.command()
async def insta1k(ctx):
  await ctx.send(f"[STRIPE](https://buy.stripe.com/6oEeWS2RLb824Tu4gi) or [PAYPAL](https://www.paypal.me/drsusplayz). When you are done please run !complete command")
@bot.command()
async def insta2k(ctx):
  await ctx.send(f"[STRIPE](https://buy.stripe.com/fZe5mi4ZT0to3Pq6or)  or [PAYPAL](https://www.paypal.me/drsusplayz). When you are done please run !complete command")
@bot.command()
async def insta3k(ctx):
  await ctx.send(f"[STRIPE](https://buy.stripe.com/8wM5mifEx5NIbhSdQU) or [PAYPAL](https://www.paypal.me/drsusplayz). When you are done please run !complete command")
@bot.command()
async def insta4k(ctx):
  await ctx.send(f"[STRIPE](https://buy.stripe.com/eVaaGC2RLb822Lm3ch) or [PAYPAL](https://www.paypal.me/drsusplayz). When you are done please run !complete command")
@bot.command()
async def insta5k(ctx):
  await ctx.send(f"[STRIPE](https://buy.stripe.com/6oEbKGakdcc62Lm9AG) or [PAYPAL](https://www.paypal.me/drsusplayz). When you are done please run !complete command")
@bot.command()
async def vip(ctx):
  await ctx.send(f"[STRIPE](https://buy.stripe.com/3cs01Y0JDgsm4Tu14h) or [PAYPAL](https://www.paypal.me/drsusplayz). When you are done please run !complete command")
@bot.command()
async def complete(ctx):
  await ctx.send(f"thanks for buying. We really apreciate you!")
  time.sleep(2.5)
  await ctx.send(f"Is there anything else you need?")
  time.sleep(1)
  await ctx.send(f"<@369179538615173121>. There is a new purchase")
@bot.command()
async def tiktok1k(ctx):
  await ctx.send(f"[STRIPE](https://buy.stripe.com/28o8yu7818ZU4Tu9AH) or [PAYPAL](https://www.paypal.me/drsusplayz). When you are done please run !complete command")
@bot.command()
async def tiktok2k(ctx):
  await ctx.send(f"[STRIPE](https://buy.stripe.com/28o7uqeAt8ZU5Xy3ck) or [PAYPAL](https://www.paypal.me/drsusplayz). When you are done please run !complete command")
@bot.command()
async def tiktok3k(ctx):
  await ctx.send(f"[STRIPE](https://buy.stripe.com/3csbKGeAtgsmadOfZ7) or [PAYPAL](https://www.paypal.me/drsusplayz). When you are done please run !complete command")
@bot.command()
async def tiktok4k(ctx):
  await ctx.send(f"[STRIPE](https://buy.stripe.com/dR64ie1NHdga5Xy28j)  or [PAYPAL](https://www.paypal.me/drsusplayz). When you are done please run !complete command")
@bot.command()
async def tiktok5k(ctx):
  await ctx.send(f"[STRIPE](https://buy.stripe.com/fZe5mieAt4JE5Xy3co) or [PAYPAL](https://www.paypal.me/drsusplayz). When you are done please run !complete command")

@bot.command()
async def ready(ctx):
  await ctx.send(f"Enter the command for the item your purchasing. ```!vip for VIP``````!insta1k for 1k followers (instagram)``````!insta2k for 2k followers (instagram)``````!insta3k for 3k followers (instagram)``````!insta4k for 4k followers (instagram)``````!insta5k for 5k followers (instagram)``````!tiktok1k for 1k followers (TikTok)``````!tiktok2k for 2k followers (TikTok)``````!tiktok3k for 3k followers (TikTok)``````!tiktok4k for 4k followers (TikTok)``````!tiktok5k for 5k followers (TikTok)``````!twitter1k for 1k followers (Twitter)``````!twitter2k for 2k followers (Twitter)``````!twitter3k for 3k followers (Twitter)``````!twitter4k for 4k followers (Twitter)``````!twitter5k for 5k followers (Twitter)```")
# Executes the bot with the specified token. Token has been removed and used just as an example.
bot.run(DISCORD_TOKEN)
