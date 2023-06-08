import pyrogram
from dotenv import load_dotenv
import os

load_dotenv()
app = pyrogram.Client('ACCOUNT', api_id=os.getenv('api_id'), api_hash=os.getenv('api_hash'))
app.start()
app.send_message(
    chat_id="me",
    text="Login was successful".upper()
)
app.stop()
