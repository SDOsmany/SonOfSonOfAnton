# bot.py
import os # for importing env vars for the bot to use
from twitchio.ext import commands
import dotenv
dotenv.load_dotenv()

bot = commands.Bot(
    # set up the bot
    token=os.getenv('oauth'),
    client_secret=os.getenv('CLIENT_ID'),
    prefix="!",
    initial_channels=["CodingArc"]
)

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"SonOfAnton is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.getenv('CHANNEL'), f"/me has landed!")
    print(f"Sent message to {os.getenv('CHANNEL')}")

@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')

if __name__ == "__main__":
    bot.run()
    print("Bot is running")