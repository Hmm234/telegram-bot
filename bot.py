from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN =8999173275:AAG1c3EdCEhDZLo-6CQGfBsqfpNCvJv2Lzo
GROUP_ID = -1003955187640

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await context.bot.copy_message(
            chat_id=GROUP_ID,
            from_chat_id=update.message.chat.id,
            message_id=update.message.message_id
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, forward))

app.run_polling()
