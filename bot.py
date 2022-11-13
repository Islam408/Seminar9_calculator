from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *




app = ApplicationBuilder().token("5617935185:AAG7aSq9bfGl6suiU9WAXkeh2Sz3q5C1His").build()

app.add_handler(CommandHandler("start", start))
# app.add_handler(CommandHandler("hi", Hello))
app.add_handler(CommandHandler("time", time_comm))
app.add_handler(CommandHandler("help", help_comm))
app.add_handler(CommandHandler("sum", sum_comm))
app.add_handler(CommandHandler("sub", sub_comm))
app.add_handler(CommandHandler("mult", mult_comm))
app.add_handler(CommandHandler("div", div_comm))


print('the bot is activated')

app.run_polling()


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.full_name}')

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.full_name}')
