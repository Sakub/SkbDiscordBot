from dotenv import load_dotenv
import discord
import os
import random
import praw
class Config:
    
    def token():
        load_dotenv()
        TOKEN = os.getenv('DISCORD_TOKEN')
        return TOKEN
        
    
    def guildName():
        load_dotenv()
        GUILD = os.getenv('DISCORD_GUILD')
        return GUILD

    def eBallAnswers():
        answers = [
            'yes',
            'no',
            'maybe',
            'why',
            'not really',
            'i cant tell'
        ]
        return answers

    def cogsPath():
        path = './cogs/'
        return path

    def headsOrTails():
        itemList = ['heads', 'tails']
        return itemList

    def botStatus():
        status = discord.Game('playing with the API')
        return status
    
    def ratePersonRandomNum():
        MIN = 0
        MAX = 10
        randomNum = random.randint(MIN, MAX)
        return randomNum


    def permissionErrorMessage():
        message ='you are not allowed to do this!'

        return message


    def redditClient():
        REDDIT_ID = os.getenv('REDDIT_CLIENT_ID')
        REDDIT_SECRET = os.getenv('REDDIT_SECRET')
        REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
        REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')
        REDDIT_AGENT = os.getenv('REDDIT_AGENT')
        reddit = praw.Reddit(client_id=REDDIT_ID, client_secret=REDDIT_SECRET, username=REDDIT_USERNAME, password=REDDIT_PASSWORD, user_agent=REDDIT_AGENT)
        return reddit

    def jokeSubreddit():
        subreddit = 'Jokes'
        return subreddit

    def loadJokes():
        listOfJokes = []
        subr = Config.redditClient().subreddit(Config.jokeSubreddit())
        hotSubr = subr.hot(limit = 100)
        for submission in hotSubr:
            if not submission.stickied:
                if not submission.url.endswith('.jpg') or not submission.url.endswith('.png'):
                    listOfJokes.append(submission.selftext)
        return listOfJokes