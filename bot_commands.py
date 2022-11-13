from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text(f'Приветствую {update.effective_user.full_name},Выбери желаемую функцию\n/help\n/time\n/sum\n/sub\n/mult\n/div')

# async def Hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
#     await update.message.reply_text(f'hi {update.effective_user.first_name}')

async def time_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text(f'{datetime.datetime.now(tz=None)}')

async def help_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text(f'/time\n/help\n/sum\n/sub\n/mult\n/div')

async def sum_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    z = x + y
    await update.message.reply_text(f'{x} + {y} = {z}')

async def div_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    z = x / y
    await update.message.reply_text(f'{x} / {y} = {z}')

async def sub_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    z = x - y
    await update.message.reply_text(f'{x} - {y} = {z}')

async def mult_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    z = x * y
    await update.message.reply_text(f'{x} * {y} = {z}')