#CritterPictures
#Author - Dacey Black

import os #for file handling
from dotenv import load_dotenv #for api key and token storage
import discord 
import json #for api handling
import requests #for api requests
import random #for randomized responses
import logging #for logging
import sys #for console logging output

logging.basicConfig(handlers=[logging.FileHandler('CritterPictures.log'),logging.StreamHandler(sys.stdout)],level=logging.INFO,format = '%(asctime)s - %(levelname)s: %(message)s')

load_dotenv()

discord_token = os.getenv('discord_token') #bot token
cat_api = os.getenv('cat_api') #thecatapi.com api key

cat_pic_phrases = [
    "Sounds like you need a cat",
    "Did somebody say cat?",
    "It's cat-o-clock",
    "Meow",
    "Cat",
    "[insert definitely appropriately lyric-ed cat dubstep here]",
    "I think this cat would be purrfect for you",
    "na na na na na na na na na na na na na na na CATMAN!",
    "time for a little cat nap",
    "I want a cat",
    "OOOOH!!!... cat.",
    "It's time for another cat",
    "This cat is my favorite",
    "He is a cat and therefore I love him",
    "You could send me a cat sometimes too",
    "Cats are my spirit animal",
    "Cats are better than people",
    "Have you hugged a cat today?",
    "I need another cat",
    "It's time for a cat",
    "It's getting cat-ty in here",
    "For christmas, I want a cat",
    "Meeeowwww",
    "One can never have too many cats",
    "CAT!",
    "Cat? Cat.",
    "Kitty Cat",
    "KitKat's are my favorite candy",
    "Cats and computers go hand in hand. Why else would they love to sit on keyboards so much?",
    "Here kitty kitty kitty"
    ]

dog_pic_phrases = [
    "Sounds like you need a dog",
    "Did somebody say dog?",
    "It's dog-o-clock",
    "Woof",
    "Dog",
    "I think this cat would be purrfect for you",
    "I want a dog",
    "pup-po.",
    "It's time for another dog",
    "This dog is my favorite",
    "He is a dog and therefore I love him",
    "You could send me a dog sometimes too",
    "dogs are my spirit animal",
    "dogs are better than people",
    "Have you hugged a puppy today?",
    "I need another dog",
    "It's time for a dog",
    "For christmas, I want a puppy",
    "Thats a good woofer",
    "One can never have too many dogs",
    "Dog!",
    "Dog? Dog.",
    "Just a little bork",
    "Puppy love",
    ]

client = discord.Client()

#onload show all servers connected to bot
@client.event
async def on_ready():
    logging.info(str(client.user) + ' has connected to Discord and is active in the following servers: '+", ".join('"'+str(guild.name+'"'+'<'+str(guild.id)+'>') for guild in client.guilds)) #log file output

#message events
@client.event
async def on_message(message): #on message in active channel
#don't respond to self
    if message.author == client.user:
        return

#test case
    if message.content.startswith('$test'): #if "$test"
        logging.info(str(message.author)+ ' sent command "$test" in channel "'+ str(client.get_channel(message.channel.id))+'"'+'%s' % (' in guild "'+str(message.guild.name)+'"' if hasattr(message.guild,'name') else "")) #logfile output
        await message.channel.send('test success')#send test success
        logging.info('Test Success sent in channel "'+ str(client.get_channel(message.channel.id))+'"'+'%s' % (' in guild "'+str(message.guild.name)+'"' if hasattr(message.guild,'name') else "")) #logfile output
        return

#if "cat" is in message send an image of a cat
    if 'cat' in message.content.lower():
        logging.info(str(message.author)+ ' sent command string "cat" in channel "'+ str(client.get_channel(message.channel.id))+'"'+'%s' % (' in guild "'+str(message.guild.name)+'"' if hasattr(message.guild,'name') else "")) #logfile output
        catimg = json.loads((requests.get(''.join(["https://api.thecatapi.com/v1/images/search?api_key=", cat_api]))).text) #concatinates api key with thecatapi to get json output
        channel = client.get_channel(message.channel.id) #gets current channel
        await channel.send(random.choice(cat_pic_phrases), embed=discord.Embed().set_image(url=catimg[0]['url'])) #sends random cat phrase with embed img url from json output of thecatapi
        logging.info('Cat picture sent in channel "'+ str(client.get_channel(message.channel.id))+'"'+'%s' % (' in guild "'+str(message.guild.name)+'"' if hasattr(message.guild,'name') else "")) #logfile output
        return
        
#if "dog" is in message send an image of a dog        
    if 'dog' in message.content.lower():
        logging.info(str(message.author)+ ' sent command string "dog" in channel "'+ str(client.get_channel(message.channel.id))+'"'+'%s' % (' in guild "'+str(message.guild.name)+'"' if hasattr(message.guild,'name') else "")) #logfile output
        dogimg = json.loads(requests.get("https://dog.ceo/api/breeds/image/random").text) #get api output as json
        channel = client.get_channel(message.channel.id) #gets current channel
        await channel.send(random.choice(dog_pic_phrases), embed=discord.Embed().set_image(url=dogimg['message'])) #sends random dog phrase with embed img url from json output of dog.ceo api
        logging.info('Dog picture sent in channel "'+ str(client.get_channel(message.channel.id))+'"'+'%s' % (' in guild "'+str(message.guild.name)+'"' if hasattr(message.guild,'name') else "")) #logfile output
        return
        
#if good bot sent
    if message.content.lower().startswith('good bot'): #if "good bot" 
        logging.info(str(message.author)+ ' sent command "good bot" in channel "'+ str(client.get_channel(message.channel.id))+'"'+'%s' % (' in guild "'+str(message.guild.name)+'"' if hasattr(message.guild,'name') else "")) #logfile output
        await message.channel.send('Thank you :D')#send thanks
        logging.info('Thank you sent in channel "'+ str(client.get_channel(message.channel.id))+'"'+'%s' % (' in guild "'+str(message.guild.name)+'"' if hasattr(message.guild,'name') else "")) #logfile output
        return
        
#if bad bot sent
    if message.content.lower().startswith('bad bot'): #if "bad bot" 
        logging.info(str(message.author)+ ' sent command "bad bot" in channel "'+ str(client.get_channel(message.channel.id))+'"'+'%s' % (' in guild "'+str(message.guild.name)+'"' if hasattr(message.guild,'name') else "")) #logfile output
        await message.channel.send('Hey heck you too buddy')#send negative response
        logging.info('Negative response sent in channel "'+ str(client.get_channel(message.channel.id))+'"'+'%s' % (' in guild "'+str(message.guild.name)+'"' if hasattr(message.guild,'name') else "")) #logfile output
        return

client.run(discord_token) #run using discord api token