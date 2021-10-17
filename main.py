import os
import discord #importing discord library

client = discord.Client() #Declaring discord client

#When bot is started:
@client.event #Whenever occurs a event this will be triggered
async def on_ready(): #Function that will be executed when the bot starts
    print('VeK has been awaked as {0.user}'.format(client)); #Print that the bot has been awaked as client user "name"
    channel = client.user
    print('Channel: {0}'.format(channel))
    #await client..send('whomst has summoned the almighty one?!') #Send message when started

@client.event
async def on_message(message): #triggers on receiving message, and receive message as parameter
    #Formmating User Name
    author = '{}'.format(message.author) #receiving author name as string
    author = author.split('#',1) #spliting the name
    author = author[0] #getting only the name

    #Getting message and transforming into lower case
    message.content = message.content.lower()
    
    if author == client.user: #If the bot is the author: do nothing
        return

    if message.content==('vek'): #if message starts with "vek"
        await message.channel.send('Fala tu!') #says: "Fala tu!"

    if message.content==('vek hello world'): #if message starts with "vek"
        await message.channel.send('Hello World!') #says: "Fala tu!"

    if message.content==('vek hello'): #if message starts with "vek hello"
        sendingMessage = 'Hello {name}!'.format(name = author)
        await message.channel.send(sendingMessage) #says: "Hello {username}"

    if message.content==('vek salve'):
        await message.channel.send('Salve Caraio!') #says: "Salve Caraio!"

    if message.content==('vek ola'):
        await message.channel.send('Olá {0}!'.format(author)) #says: "Olá {username}"

    if message.content==('vek olá'):
        await message.channel.send('Olá {0}!'.format(author)) #says: "Olá {username}"
    
    if message.content==('vek oi'):
        await message.channel.send('Oi {0}!'.format(author)) #says: "Olá {username}"

    if message.content==('vek hi'):
        await message.channel.send('Hi {0}!'.format(author)) #says: "Olá {username}"


token = os.environ['token']
client.run(token) #Running the bot