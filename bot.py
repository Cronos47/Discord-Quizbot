import discord
import requests
import json
import asyncio

client = discord.Client()

def get_score():
    leaderboard = ''
    id = 1
    response = requests.get("https://limitless-depths-89751.herokuapp.com/api/score/leaderboard/")
    json_data = json.loads(response.text)

    for item in json_data:
        leaderboard += str(id) + ' ' + item['name'] + ". " + str(item['points']) + "\n"
        id += 1 

    return(leaderboard)

def update_score(user='testuser', points = 10):

    url = 'https://limitless-depths-89751.herokuapp.com/api/score/update/'
    new_score = {'name': user, 'points': points}
    x = requests.post(url, data = new_score)

    return

def get_question():
    qs = ''
    id = 1
    answer = 0
    points = 0
    response = requests.get("https://limitless-depths-89751.herokuapp.com/api/random/")
    json_data = json.loads(response.text , strict = False , encoding = 'utf-8')
    qs += "Question: \n"
    qs += json_data[0]['title'] + "\n"

    for item in json_data[0]['answer']:
        qs += str(id) + ". " + item['answer'] + "\n"

        if item['is_correct']:
            answer = id
        
        id += 1 

    points = json_data[0]['points']
    
    return(qs, answer , points)

@client.event
async def on_message(message):
    global client
    if message.author == client.user:
        return

    if message.content.startswith('$score'):
        leaderboard = get_score()
        await message.channel.send(leaderboard)

    elif message.content.startswith('$question'):

        qs, answer  , points= get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isdigit() 

        try:
            guess = await client.wait_for('message', check=check, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Sorry, you took too long')

        if int(guess.content) == answer:
            user = guess.author
            msg = str(guess.author.name) + ' got it right! +' + str(points) + ' points'
            await message.channel.send(msg)
            update_score(user , points)
        else:
            await message.channel.send('Oops. That is not right')


    elif message.content.startswith('$quit'):
        await message.channel.send('Okay , we can play later then!')
        await client.close()
        return 
        
client.run('ODM4MDM4MDY0MTAxOTgyMjM4.YI1RxA.YalhHLC-1DE5XIiJwhTH_5oFUno')
exit(0)