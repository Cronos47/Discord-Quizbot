Note:
This is a QuizBot on Discord Channel "Neural Net Geeks" , the link for which is given below, 
'https://discord.gg/2EPJxX9H'.
After clicking on 'Accept Invite' the user would be able to access the public channels under "Voice Channels" section.

-> In the discord group homepage , navigate to 'quiz channel' section and where the quiz bot resides.
-> This bot has been made using DjangoDB and Django Rest Framework and necessary Python Fundamentals.

Bot Specifications and Working Principle:
-> This is generally a quiz bot that contains 15 questions and the questions are chosen randomly from the database by the bot.
-> To ask for a question you have to type in "$question" so the bot will recognize the string the generate a random question picked out from the database. 
-> Every question consists of only three options , and only one of which is correct 
-> The way to answer to any question is to just message the index of the correct answer option in the channel.
-> The person who's telling to bot to invoke the questions only that person will be able to answer that particular question.
-> Each question will have a time limit of 5 seconds to answer. 
-> Every question may not have the same valuation , it actually depends on the difficulty of it , that was predefined while inserting the questions into database.
-> Every time a correct answer is spotted by the bot it'll change the leaderboard scores instantly.
-> To view scores just type in "$score"
-> The bot will automatically change the rank of the players according to the scores.
-> To alter any detail regarding questions , answers and scores just navigate to the site "https://limitless-depths-89751.herokuapp.com/admin/" 
   (Username - admin , Password - @Cr7rocks)
-> To quit using the quizbot just type "$quit".