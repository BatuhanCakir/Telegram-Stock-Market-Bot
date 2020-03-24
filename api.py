
import requests
import json
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext.dispatcher import run_async
import time
import re
def stockPrice(firm):
    parameters = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': firm,
    'interval': '5min',
    'apikey': 'RR2X32T6PCKXAM49',
    }
    response = requests.get('https://www.alphavantage.co/query?', params=parameters)
    stakes = response.json()["Time Series (5min)"]

    lst = []
    for key in stakes.keys():
        lst.append(stakes[key]["1. open"])

    if(lst[0]>lst[1]):

        return True



def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#print(stockPrice('DAI.DE'))
#print(stockPrice('^GDAXI'))



@run_async
def bop(update, context):
   while (True):
       if(stockPrice('^GDAXI')):
           chat_id = update.message.chat_id
           context.bot.sendMessage(chat_id=chat_id, text='DER DAX IST GESTIEGEN HURRA')
           time.sleep(300)
       else :
           chat_id = update.message.chat_id
           context.bot.sendMessage(chat_id=chat_id, text='DER DAX IST GESUNKEN')
           time.sleep(300)






def main():
    updater = Updater('971255948:AAHO5jiWZR2noaJEd4hgXKXnQCUyVtXJKEo', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('stock', bop))
    #dp.add_handler(MessageHandler(Filters.all, callback_method))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()




