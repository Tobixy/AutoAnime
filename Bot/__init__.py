import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = int(environ.get('API_ID', 28374181)) #API ID
API_HASH = environ.get('API_HASH', '00b7ca7f535e816590db39e76f85d0c7') #API HASH
BOT_TOKEN = environ.get('BOT_TOKEN', '6103019135:AAHsZsIcBkueu7CAm1BMUp7C3976U5J97Js') #BOT TOKEN
DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://HoshinoAI:HoshinoV1@hoshinodb.cfany1w.mongodb.net/?retryWrites=true&w=majority') #MONGO DB
OWNER_ID = int(environ.get('OWNER_ID', 5715764478)) #OWNER ID
MAIN_CHANNEL = int(environ.get('MAIN_CHANNEL',-1001876834254))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get('ARCHIVE_CHANNEL', -1001555306198))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get('MESSAGE_ID', 45624)) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
