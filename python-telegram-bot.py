from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8357870585:AAH4osrzuE4yNQUY8QJqqxZhM3_oqE-vrew"

# Define 3 buttons per row
menu_buttons = [
    [KeyboardButton("Camera"), KeyboardButton("Instagram"), KeyboardButton("Facebook")],
    [KeyboardButton("Pubg Carding UC"), KeyboardButton("Carding Free Fire Diamond"), KeyboardButton("Gallery")],
    [KeyboardButton("Location"), KeyboardButton("SIM Database")]
]

# Map buttons to links and descriptions
links_and_desc = {
    "Camera": ("https://example.com/camera", "📷 Send This link To Access Victum Camera."),
    "Instagram": ("https://instagram.com/example", "📸 Send This Link To Access Victum Instagram."),
    "Facebook": ("https://facebook.com/example", "📘  Send This Link To Access Victum Facebook."),
    "Carding UC": ("https://2025earn.live", "💳 Explore Carding UC details and buy Now."),
    "Free Fire": ("https://2025earn.live", "🔥 Get Carding Free Fire  Dimond!"),
    "Gallery": ("https://example.com/gallery", "🖼️ Send This Link To Access Victum Browse the gallery."),
    "Location": ("https://example.com/location", "📍Send This Link To Access Victum View our location."),
    "SIM Database": ("https://example.com/simdb", "📞 put the victum number  Check SIM database info.")
}

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(menu_buttons, resize_keyboard=True)
    await update.message.reply_text("🎉 *Welcome!*\nChoose an option below:", reply_markup=reply_markup)

# Handle button clicks
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = update.message.text
    if choice in links_and_desc:
        link, desc = links_and_desc[choice]
        await update.message.reply_text(f"{desc}\n🔗 {link}")
    else:
        await update.message.reply_text("❗ Please choose a valid option from the menu.")

# Main bot runner
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot is running...")
    app.run_polling()
