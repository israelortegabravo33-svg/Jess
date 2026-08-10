import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters
import google.generativeai as genai

TOKEN = os.environ.get("TELEGRAM_TOKEN")
API_KEY = os.environ.get("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)

# Usamos gemini-1.5-flash pero con la sintaxis correcta que exige la API actual
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

async def handle_message(update, context):
    try:
        response = chat.send_message(update.message.text)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text(f"Error en circuitos: {e}")

if __name__ == '__main__':
    print("Iniciando Jess...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()

