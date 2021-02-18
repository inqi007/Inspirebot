import discord
import os
import requests
import json
from keep_alive import keep_alive


client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote) 

def get_joke():
  response = requests.get("https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/jokes")
  data = response.json()
  joke = (f"{data['setup']} \n{data['punchline']}")
  return(joke) 

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
      quote = get_quote()
      await message.channel.send(quote)

    if message.content.startswith('$joke'):
      joke = get_joke()
      await message.channel.send(joke)


keep_alive()
client.run(os.getenv('TOKEN'))

