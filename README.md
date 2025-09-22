# tg-360-bot

Telegram-бот с кнопкой для открытия 360° мини-аппы в Telegram WebApp.

## Запуск на Render

1. Создайте новый Web Service из этого репозитория.
2. Добавьте переменные окружения:
   - `BOT_TOKEN` — токен от @BotFather
   - `WEBAPP_URL` — ссылка на GitHub Pages мини-аппы (например, https://oneperec.github.io/tg-360-miniapp/)
   - `WEBHOOK_HOST` — URL сервиса на Render (будет виден после деплоя)
3. После первого деплоя вставьте `WEBHOOK_HOST` и сделайте **Redeploy**.
4. В Telegram откройте бота и отправьте `/start`.  
   Кнопка должна открыть мини-апп внутри Telegram.
