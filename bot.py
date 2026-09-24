import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8889199194:AAEPGGFOg1SGc_wMXZ_phQHPFWvnz3ClrgY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    
    btn1 = InlineKeyboardButton("📱 تطبيقات المونتاج", callback_data="editing_apps")
    btn2 = InlineKeyboardButton("🎮 أقسام الألعاب", callback_data="games_menu")
    btn3 = InlineKeyboardButton("🔥 العروض والتخفيضات", callback_data="offers")
    btn4 = InlineKeyboardButton("❓ طريقة الشراء والتثبيت", callback_data="how_to_buy")
    btn5 = InlineKeyboardButton("💬 التواصل والطلب", callback_data="support")
    
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    welcome_text = (
        "مرحباً بك في متجر التطبيقات والألعاب! 🚀\n"
        "أفضل التطبيقات والألعاب بأرخص الأسعار في مصر.\n\n"
        "اختر القائمة المناسبة من الأسفل:"
    )
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    bot.answer_callback_query(call.id)
    
    if call.data == "editing_apps":
        apps_text = (
            "📱 **قائمة تطبيقات المونتاج والتصميم:**\n\n"
            "- CapCut Pro: 20 EGP\n"
            "- Kinemaster Pro: 15 EGP\n"
            "- VN Video Editor Pro: 15 EGP\n"
            "- PicsArt Gold: 20 EGP\n"
            "- Alight Motion Pro: 20 EGP\n"
            "- InShot Pro: 15 EGP\n"
            "- Lightroom Premium: 20 EGP\n"
            "- Remini Pro: 15 EGP\n"
            "- Canva Pro: 25 EGP\n\n"
            "📩 **للطلب والتواصل:** 01061777536\n"
            "💳 **تحويل اتصالات كاش:** 01119682198"
        )
        bot.send_message(call.message.chat.id, apps_text, parse_mode="Markdown")

    elif call.data == "games_menu":
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        
        g1 = InlineKeyboardButton("💥 ألعاب أكشن و GTA", callback_data="g_action")
        g2 = InlineKeyboardButton("⛏️ ألعاب بناء ومغامرات", callback_data="g_adventure")
        g3 = InlineKeyboardButton("🏎️ ألعاب سباقات وسرعة", callback_data="g_racing")
        g4 = InlineKeyboardButton("🕹️ محاكيات وألعاب رياضية", callback_data="g_sports")
        
        markup.add(g1, g2, g3, g4)
        
        bot.send_message(call.message.chat.id, "🎮 **اختر قسم الألعاب الذي تريده:**", reply_markup=markup)

    elif call.data == "g_action":
        text = (
            "💥 **ألعاب أكشن و GTA:**\n\n"
            "- GTA San Andreas: 25 EGP\n"
            "- GTA Vice City: 20 EGP\n"
            "- GTA III: 15 EGP\n"
            "- GTA Liberty City Stories: 20 EGP\n"
            "- Bully: Anniversary Edition: 25 EGP\n"
            "- Max Payne Mobile: 20 EGP\n"
            "- Hitman Sniper: 15 EGP\n\n"
            "📩 **للطلب والتواصل:** 01061777536\n"
            "💳 **تحويل اتصالات كاش:** 01119682198"
        )
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown")

    elif call.data == "g_adventure":
        text = (
            "⛏️ **ألعاب بناء ومغامرات:**\n\n"
            "- Minecraft PE (أحدث إصدار): 10 EGP\n"
            "- Terraria: 15 EGP\n"
            "- ROBLOX Premium Items: 15 EGP\n"
            "- Don't Starve: Pocket Edition: 20 EGP\n"
            "- Limbo: 10 EGP\n\n"
            "📩 **للطلب والتواصل:** 01061777536\n"
            "💳 **تحويل اتصالات كاش:** 01119682198"
        )
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown")

    elif call.data == "g_racing":
        text = (
            "🏎️ **ألعاب سباقات وسرعة:**\n\n"
            "- Need for Speed Most Wanted: 20 EGP\n"
            "- Real Racing 3: 15 EGP\n"
            "- Car Parking Multiplayer: 15 EGP\n"
            "- Asphalt 9 Packs: 20 EGP\n\n"
            "📩 **للطلب والتواصل:** 01061777536\n"
            "💳 **تحويل اتصالات كاش:** 01119682198"
        )
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown")

    elif call.data == "g_sports":
        text = (
            "🕹️ **محاكيات وألعاب رياضية:**\n\n"
            "- PPSSPP Gold: 10 EGP\n"
            "- PES / eFootball ISO Packs: 20 EGP\n"
            "- Football Manager 2024: 25 EGP\n"
            "- NBA 2K20: 25 EGP\n\n"
            "📩 **للطلب والتواصل:** 01061777536\n"
            "💳 **تحويل اتصالات كاش:** 01119682198"
        )
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown")

    elif call.data == "offers":
        offers_text = (
            "🎁 **عرض المتجر الخرافي:**\n\n"
            "🔥 **اشتري أي تطبيقين أو لعبتين واحصل على تطبيق أو لعبة إضافية مجاناً من اختيارك!** 🔥\n\n"
            "📌 العرض ساري عند التواصل للطلب عبر الرقم المخصص."
        )
        bot.send_message(call.message.chat.id, offers_text, parse_mode="Markdown")

    elif call.data == "how_to_buy":
        buy_text = (
            "❓ **خطوات الشراء والتثبيت:**\n\n"
            "1️⃣ حدد التطبيقات أو الألعاب التي تريدها من البوت.\n"
            "2️⃣ تواصل مع الرقم المخصص للطلب عبر الهاتف أو التيليجرام: `01061777536`.\n"
            "3️⃣ قم بتحويل المبلغ المحدد عبر محفظة **اتصالات كاش** على الرقم: `01119682198`.\n"
            "4️⃣ أرسل صورة إشعار التحويل للتأكيد.\n"
            "5️⃣ ستستلم رابط التحميل المباشر مع ملف شرح طريقة التثبيت خطوة بخطوة!"
        )
        bot.send_message(call.message.chat.id, buy_text, parse_mode="Markdown")

    elif call.data == "support":
        support_text = (
            "🛒 **للطلب والتواصل:**\n"
            "01061777536\n\n"
            "💳 **لتحويل اتصالات كاش والشكاوي:**\n"
            "01119682198"
        )
        bot.send_message(call.message.chat.id, support_text, parse_mode="Markdown")

bot.infinity_polling()
