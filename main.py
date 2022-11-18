import os
import discord
import random
import re
from dotenv import load_dotenv
import json

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Bot(intents=intents)
with open('data.json', 'r') as fp:
    social_credits = json.load(fp)


##Opening the JSON files containing the "Good" or "bad" words
with open('bad.json', 'r') as fp:
    bad = json.load(fp)

with open('good.json', 'r') as fp:
    good = json.load(fp)

punctuation = ['!', '?', '.', ',', '`', '~', '@', '#', '$', '%', '&', '*', '(', ')']


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

##TODO: Create a word suggest command
##Credit Command
@bot.slash_command(name="get_credit", description="Get your current social credit")
async def get_credit(ctx):
    auth = str(ctx.author)
    value = social_credits.get(auth)
    print(auth)
    await ctx.respond('You have %s social credit' % (value))

##Leaderboard command
@bot.slash_command(name="leaderboard", description="Show global social credit rankings")
async def leaderboard(ctx):
    leaderb0 = dict(sorted(social_credits.items(), key=lambda item: item[1], reverse=True))
    leaderb1 = str(leaderb0)
    leaderb2 = leaderb1.replace('{', '%temp%').replace('{','}').replace('%temp%','')
    leaderb3 = leaderb2.replace('}', '%temp%').replace('{', '}').replace('%temp%', '')
    Leaderb = leaderb3.split(",")
    print(Leaderb)
    embed = discord.Embed(title="Leaderboard", description="The overall social credit rankings", color=discord.Colour.red())
    embed.add_field(name='ZE RANKINGS', value="\n".join('%03d %s' % (i, s) for i, s in enumerate(Leaderb, 1)))
    await ctx.respond(embed=embed)


@bot.event
async def on_message(message): #usual check it's not the bot yada yada
    with open ('data.json', 'r') as fp:
        scdiff = json.load(fp)
    if message.author == bot.user:
        return
    if message.author.bot:
        return
    lower = message.content.lower()
    messa = lower  #splitting words and getting rid of punctuation
    translation_table = str.maketrans('', '', ''.join(punctuation))
    messa = messa.translate(translation_table)
    words = re.split("\s", messa)
    if (set(bad) & set(words)): #bad response
        neg = [
            'That is not right citizen!',
            "I'm sorry, I don't think that happened.",
            'No',
            'Nothing Happened',
            '*Hits with gun*',
        ]
        response = random.choice(neg)
        await message.channel.send(response)
        authr = str(message.author)
        print(authr)
        with open ('data.json', 'r') as fp:
            scdiff = json.load(fp)
        print(scdiff) #Credit application
        if authr in scdiff:
            value = social_credits.get(authr)
            print(value)
            value = value - 100
            social_credits.update({authr: value})
            scdiff = social_credits
            print(scdiff)
            with open('data.json', 'w') as fp:
                json.dump(scdiff, fp)
            return
        else:
            value = 1500
            social_credits.update({authr: value})
            scdiff = social_credits
            await message.channel.send('Social credit account created, you have 1500 social credit')
            print(scdiff)
            with open('data.json', 'w') as fp:
                json.dump(scdiff, fp)
    if (set(good) & set(words)): #good response
        pos = [
            'Nice citizen!',
            'Keep doing your part!',
            '*Tips hat*',
            '*Smiles and nods*',
        ]
        response = random.choice(pos)
        await message.channel.send(response)
        authr = str(message.author)
        print(authr)
        scdiff = social_credits    #this section is the applying of social credit
        print(scdiff)
        if authr in scdiff:
            value = social_credits.get(authr)
            print(value)
            value = value + 100
            social_credits.update({authr: value})
            scdiff = social_credits
            print(scdiff)
            with open('data.json', 'w') as fp:
                json.dump(scdiff, fp)
            return
        else:
            value = 1700
            social_credits.update({authr: value})
            scdiff = social_credits
            await message.channel.send('Social credit account created, you have 1700 social credit')
            with open('data.json', 'w') as fp:
                json.dump(scdiff, fp)
            print(scdiff)
            return


bot.run(TOKEN) #RUUUUUUUUUUNNNNNNNNNNNNN
