import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from google import genai

TOKEN = os.environ.get("TELEGRAM_TOKEN")
API_KEY = os.environ.get("GOOGLE_API_KEY")

# Inicializamos el cliente oficial nuevo
client = genai.Client(api_key=API_KEY)

async def handle_message(update, context):
    try:
        # Usamos gemini-2.5-flash (o gemini-1.5-flash) con la nueva estructura
                response = client.models.generate_content(
            model='gemini-2.5',
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
