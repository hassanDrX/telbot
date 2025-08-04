from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8241514661:AAH7VyEJDJvaYPUtmfdkdsUDRIV6yz98i7Y"

# Define menu buttons
menu_buttons = [
    [KeyboardButton("Camera")],
    [KeyboardButton("Instagram")],
    [KeyboardButton("Facebook")],
    [KeyboardButton("Carding UC")],
    [KeyboardButton("Free Fire")],
    [KeyboardButton("Gallery")],
    [KeyboardButton("Location")],
    [KeyboardButton("SIM Database")]
]

links_and_desc = {
    "Camera": ("https://example.com/camera", "Open the camera page."),
    "Instagram": ("https://instagram.com/example", "Visit our Instagram profile."),
    "Facebook": ("https://facebook.com/example", "Follow us on Facebook."),
    "Carding UC": ("https://example.com/cardinguc", "Learn about Carding UC."),
    "Free Fire": ("https://example.com/freefire", "Play Free Fire now!"),
    "Gallery": ("https://example.com/gallery", "View our photo gallery."),
    "Location": ("https://example.com/location", "Check out our location."),
    "SIM Database": ("https://example.com/simdb", "Access SIM database info.")
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(menu_buttons, resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text("Welcome! Please choose an option:", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_choice = update.message.text
    if user_choice in links_and_desc:
        link, desc = links_and_desc[user_choice]
        await update.message.reply_text(f"{desc}\nLink: {link}")
    else:
        await update.message.reply_text("Please select an option from the menu.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()
