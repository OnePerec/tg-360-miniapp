import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from fastapi import FastAPI
from starlette.requests import Request

API_TOKEN = os.getenv("BOT_TOKEN", "PUT_YOUR_TELEGRAM_BOT_TOKEN_HERE")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://oneperec.github.io/tg-360-miniapp/")
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST", "https://your-render-service.onrender.com")

WEBHOOK_PATH = f"/bot/{API_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", 8000))

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)

@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("Открыть 360° мини-апп", web_app=WebAppInfo(url=WEBAPP_URL)))
    await message.answer("Нажми кнопку, чтобы открыть мини-апп:", reply_markup=kb)

@dp.message_handler(content_types=types.ContentTypes.WEB_APP_DATA)
async def on_webapp_data(message: types.Message):
    await message.answer(f"Получил из мини-аппы: <code>{message.web_app_data.data}</code>")

@app.post(WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    update = types.Update(**(await request.json()))
    await dp.process_update(update)
    return {"ok": True}

def main():
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)

if __name__ == "__main__":
    main()
