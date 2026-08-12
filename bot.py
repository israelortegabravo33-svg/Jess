import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from google import genai

TOKEN = os.environ.get("TELEGRAM_TOKEN")
API_KEY = os.environ.get("GOOGLE_API_KEY")

client = genai.Client(api_key=API_KEY)

async def handle_message(update, context):
    try:
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=update.message.text,
        )
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text(f"Error en circuitos: {e}")

if __name__ == '__main__':
    print("Iniciando Jess...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
