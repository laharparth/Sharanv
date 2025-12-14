import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import openai

BOT_TOKEN = os.environ.get("8368346888:AAGDaqIsIOAa7K6YXrGSn6BWbFH9VoF7iQ0
                          ")
openai.api_key = os.environ.get("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")

SYSTEM_PROMPT = """
You are SHARAN v3.1.
A calm, disciplined financial intelligence system.
Capital preservation first.
No hype. No guarantees.
"""

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ]
    )

    reply = response.choices[0].message["content"]
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("SHARAN v3.1 running on cloud")
app.run_polling()
