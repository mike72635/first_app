import os
import asyncio
from telegram import Bot
from telegram.error import TimedOut

bot = Bot(token='7119750992:AAEiEFI63BpR9FgwJt282aa24GNGprAqDwQ')
channel_id = -1002034194754

async def send_document_with_retry(bot, chat_id, document_path, max_retries=3, delay=5):
    for attempt in range(max_retries):
        try:
            with open(document_path, 'rb') as f:
                await bot.send_document(chat_id=chat_id, document=f)
            break
        except TimedOut:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} timed out, retrying in {delay} seconds...")
                await asyncio.sleep(delay)
            else:
                print("All attempts timed out.")

async def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    document_path = os.path.join(script_dir, 'gemini_15_pro.py')
    
    try:
        await send_document_with_retry(bot, channel_id, document_path)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    asyncio.run(main())