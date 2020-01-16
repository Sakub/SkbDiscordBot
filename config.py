from dotenv import load_dotenv
import discord
import os
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

    def redditClient():
        REDDIT_ID = os.getenv('REDDIT_CLIENT_ID')
        REDDIT_SECRET = os.getenv('REDDIT_SECRET')
        REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
        REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')
        REDDIT_AGENT = os.getenv('REDDIT_AGENT')
        reddit = praw.Reddit(client_id=REDDIT_ID, client_secret=REDDIT_SECRET, username=REDDIT_USERNAME, password=REDDIT_PASSWORD, user_agent=REDDIT_AGENT)
        return reddit
