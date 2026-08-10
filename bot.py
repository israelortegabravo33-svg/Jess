import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters
import google.generativeai as genai

# Usamos variables de entorno para mayor seguridad (Render las gestionará)
TOKEN = os.environ.get("TELEGRAM_TOKEN")
API_KEY = os.environ.get("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

async def handle_message(update, context):
    response = chat.send_message(update.message.text)
    await update.message.reply_text(response.text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("Jess está operativa...")
    app.run_polling()
