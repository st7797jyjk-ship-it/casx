from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8988797748:AAFFDRAh-VRy6ogJw2UAS_pmPKr-1GPvwpU"
MINI_APP_URL = "https://st7797jyjk-ship-it.github.io/casx/mini-app/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎰 ОТКРЫТЬ КАЗИНО", web_app=WebAppInfo(url=MINI_APP_URL))],
    ]
    await update.message.reply_text(
        "🎮 *Добро пожаловать в казино!*\n\n"
        "Нажми на кнопку чтобы открыть приложение\n"
        "с рулеткой, блэкджеком и апгрейдом 🎰🃏📈",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🎰 Casino Mini App запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()