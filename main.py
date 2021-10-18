#Imports
#-------------------------------------------------------------
import discord #importing discord library
import os #importing os commands
import json #for work with json
import random #random generator library
from replit import db #working with replit database
from keep_alive import keep_alive #keeping the bot awake

client = discord.Client() #Declaring discord client

#-------------------------------------------------------------
#Functions
#-------------------------------------------------------------

#Function that verifies if the is a repeated item on list
def is_repeated_on_list(list,input): #receives list and input as parameters
    if input in list:
        return True
    else:
        return False

#Trigger Words
#-------------------------------------------------------------        

#function that gets trigger_words list:
def list_trigger_words():
    trigger_words = db["trigger_words"] #getting list from db
    final_message = "Palavras trigger:\n" #return this message in the end
    
    if trigger_words != []: #if there is a trigger word:
        i = 1
        for word in trigger_words: #print every trigger_word
            final_message += '{0}: "{1}"\n'.format(i,word)
            i += 1
    else: #print that arent any trigger_words
        final_message += 'Não há palavras trigger'

    return final_message

#Function for defining new words as triggers
def define_new_trigger_word(message):
    #print('Entrou')
    if "trigger_words" in db.keys(): #verifies if there is a key called trigger_words
        trigger_words = db["trigger_words"] #getting all trigger words from database
        if isinstance(trigger_words,str):
            trigger_words = [trigger_words]
        trigger_words.append(message) #inserting new message in the list
        db["trigger_words"] = trigger_words #updating trigger_words key in database
        return 'Palavra Trigger "{}" cadastrada com sucesso!'.format(message)
    else:
        db["trigger_words"] = message #creates trigger word on database
        return 'Palavra Trigger "{}" cadastrada com sucesso!'.format(message)

#function that deletes existing triggers word
def delete_trigger(word):
    if "trigger_words" in db.keys():
        trigger_words = db["trigger_words"] #get all trigger_words from db
        try: #Tries to remove the word from the list
            trigger_words.remove(word)
            db["trigger_words"] = trigger_words #updates database
            return 'Palavra trigger: "{}" removida com sucesso!'.format(word)
        except:
            return 'Falha ao tentar remover palavra trigger'
    else:
        return 'Não há palavras trigger no database'

#Random Phrases
#-------------------------------------------------------------

#listing random phrases
def list_random_phrases():
    if "random_phrases" in db.keys():
        random_phrases = db["random_phrases"]
        final_message = 'Random Phrases:\n'
        if random_phrases != []:
            i = 1
            for phrase in random_phrases:
                final_message += '{0}: {1}\n'.format(i,phrase)
                i += 1
            return final_message
        else:
            return 'Nenhuma frase foi encontrada'
    else:
        return 'Não foi encontrado nada no db'

#function that return new random words called by trigger
def call_random_phrase():
    if "random_phrases" in db.keys(): #If the is a random_phrase key on database
        random_phrases = db["random_phrases"]
        random_phrase = random.choice(random_phrases) #generate a random phrase from list
    else:
        random_phrase = 'Não há random phrase no database'
    
    return random_phrase

#function that insert random phrases on database
def define_new_random_phrase(phrase):
    if "random_phrases" in db.keys(): #if there is random_phrases key on db
        random_phrases = db["random_phrases"]
        if phrase in random_phrases: #if the phrase already exists, will be not added
            final_message = 'frase "{}" já existe no database'.format(phrase)
            return final_message
        else: #insert phrase on database
            random_phrases.append(phrase)
            db["random_phrases"] = random_phrases
            final_message = 'frase "{}" adicionada com sucesso!'.format(phrase)
            return final_message
    else:
        db["random_phrases"] = [phrase]
        final_message = 'frase "{}" adicionada com sucesso!'.format(phrase)
        return final_message

#function that deletes random phrases from database    
def delete_random_phrase(phrase):
    if "random_phrases" in db.keys(): #if there the phrase on db, it will be deleted
        random_phrases = db["random_phrases"]
        try:
            random_phrases.remove(phrase)
            db["random_phrases"] = random_phrases
            return 'Frase "{}" removida com sucesso!'.format(phrase)
        except:
            return 'Erro ao remover a frase do db'
    else: #else will return a error
        return 'Erro: database não encontrado'

#-------------------------------------------------------------
#Events
#-------------------------------------------------------------

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

    #Greetings
    #-------------------------------------------------------------

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

    #New Words
    #-------------------------------------------------------------

        #Trigger Words
        #-------------------------------------------------------------
    #listing trigger words
    if message.content.startswith('vek trigger list'): #if it is the trigger list command, send the all trigger words list
        await message.channel.send(list_trigger_words()) #tries to define and send the message

    #adding new trigger word
    if message.content.startswith('vek new trigger word') or message.content.startswith('vek nova palavra trigger'): #the model of message will be 'vek new trigger word "<trigger_word>"'
        #await message.channel.send('Comando recebido!') 
        new_trigger = message.content.split('"')[1]
        #await message.channel.send('"{}"'.format(new_trigger)) 
        await message.channel.send(define_new_trigger_word(new_trigger)) #tries to define and send the message

    #deleting trigger words
    condition = message.content.startswith('vek delete trigger word') 
    condition = condition or message.content.startswith('vek delete trigger')
    condition = condition or message.content.startswith('vek delete palavra trigger')
    if condition: #if any of conditions above were matched
        trigger_word = message.content.split('"')[1]
        await message.channel.send(delete_trigger(trigger_word))

        #Random phrases
        #-------------------------------------------------------------
    #listing random phrases
    condition = message.content.startswith('vek random phrases list')
    condition = condition or message.content.startswith('vek list random phrases')
    condition = condition or message.content.startswith('vek list random phrase')
    condition = condition or message.content.startswith('vek random phrase list')
    if condition: #if any of conditions above were matched
        await message.channel.send(list_random_phrases())

    #inserting new random phrase
    condition = message.content.startswith('vek new random phrase')
    condition = condition or message.content.startswith('vek insert random phrase')
    condition = condition or message.content.startswith('vek insert new random phrase')
    condition = condition or message.content.startswith('vek new phrase')
    condition = condition or message.content.startswith('vek insert new phrase')
    condition = condition or message.content.startswith('vek insert phrase')
    if condition: #if any of conditions above were matched
        random_phrase = message.content.split('"')[1]
        await message.channel.send(define_new_random_phrase(random_phrase))

    #deleting existing random phrase
    condition = message.content.startswith('vek delete random phrase')
    condition = condition or message.content.startswith('vek delete phrase')
    condition = condition or message.content.startswith('vek delete frase')
    condition = condition or message.content.startswith('vek delete frase aleatoria')
    if condition: #if any of conditions above were matched
        random_phrase = message.content.split('"')[1] #get phrase
        await message.channel.send(delete_random_phrase(random_phrase)) #tries to delete phrase

    #calling random phrase by command
    condition = message.content.startswith('vek call random phrase')
    condition = condition or message.content.startswith('vek call phrase')
    condition = condition or message.content.startswith('vek diga frase')
    condition = condition or message.content.startswith('vek diga frase aleatoria')
    if condition: #if any of conditions above were matched
        await message.channel.send(call_random_phrase()) #call phrase

    #calling phrase if a trigger word is detected
    trigger_words = db["trigger_words"]
    if any(word in message.content for word in trigger_words): #if it finds a trigger word in message
        await message.channel.send(call_random_phrase()) #send a random phrase

keep_alive()    
token = os.environ['token']
client.run(token) #Running the bot