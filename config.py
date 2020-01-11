from dotenv import load_dotenv
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
