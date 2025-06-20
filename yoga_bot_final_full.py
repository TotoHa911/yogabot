
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '7862512838:AAFTLbHVsylOGTawisvDZsvCs_6Vux5qX6E'

def start(update: Update, context: CallbackContext):
    text = (
        "добро пожаловать в наше пространство йоги и заботы 🧘‍♀️\n\n"
        "я помогу тебе сориентироваться 🌿\nвот что у нас есть:\n\n"
        "🧾 /navigation — все полезные темы\n"
        "📅 /schedule — где и когда практики\n"
        "📖 /guide — забирай бесплатный PDF “залог удачного дня”\n"
        "📬 /contacts — если есть вопрос\n\n"
        "если просто хочется почитать интересное, поболтать — заходи в чат 🤍 [основной чат](https://t.me/chatdorogakyoga/175)"
    )
    update.message.reply_text(text, parse_mode='Markdown')

def navigation(update: Update, context: CallbackContext):
    text = (
        "внутри группы 🧭\n\n"
        "🧘‍♀️ [асаны в деталях](https://t.me/chatdorogakyoga/177) — обсуждаем нюансы\n"
        "🌬 [пранаямы](https://t.me/chatdorogakyoga/185) — дыхание и концентрация\n"
        "📚 [книги](https://t.me/chatdorogakyoga/187) — вдохновение из текста\n"
        "🔮 [астрология](https://t.me/chatdorogakyoga/225) — про звёзды и предназначение\n"
        "☕️ [о личном](https://t.me/chatdorogakyoga/191) — истории из практики\n"
        "🎵 [музыка](https://t.me/chatdorogakyoga/189) — делимся треками, достойными внимания\n\n"
        "выбирай самый интересный раздел 🌿"
    )
    update.message.reply_text(text, parse_mode='Markdown')

def schedule(update: Update, context: CallbackContext):
    text = (
        "расписание практик 🧘‍♀️\n\n"
        "обновляется каждую неделю и всегда есть в закреплённом сообщении в канале.\n\n"
        "⚡️ следующая живая практика в воскресенье, в 10:00\n"
        "☁️ йога онлайн по запросу (напиши Кате)\n\n"
        "[Посмотреть расписание](https://t.me/chatdorogakyoga/176)"
    )
    update.message.reply_text(text, parse_mode='Markdown')

def guide(update: Update, context: CallbackContext):
    text = (
        "📖 Забирай PDF-гайд «Залог удачного дня» — утренний комплекс, с которого приятно начать день ☀️\n\n"
        "[Скачать гайд](https://t.me/Doroga_k_Yoga/23)"
    )
    update.message.reply_text(text, parse_mode='Markdown')

def contacts(update: Update, context: CallbackContext):
    text = (
        "📬 Контакты:\n\n"
        "Преподаватель: Екатерина Багина — @katekateri_na\n"
        "Администратор: Антон Наумов — @ANT0N_NAUM0V\n"
        "Главный канал: https://t.me/Doroga_k_Yoga"
    )
    update.message.reply_text(text)

def asanas(update: Update, context: CallbackContext):
    text = (
        "🤸‍♀️ асаны в деталях\n\n"
        "здесь мы разбираем позы — ведь грамотное их выполнение и есть польза и бережное отношение к телу 🤍\n\n"
        "[Перейти в раздел](https://t.me/chatdorogakyoga/177)"
    )
    update.message.reply_text(text, parse_mode='Markdown')

def pranayamas(update: Update, context: CallbackContext):
    text = (
        "🌬 пранаямы: суть и практика\n\n"
        "здесь мы говорим о дыхании — казалось бы, простом, но самом могучем инструменте.\n"
        "здесь есть всё, чтобы дышать осознанно, практиковать техники и слушать своё тело через вдох и выдох.\n"
        "если сложно медитировать — начни с пранаямы 💨\n\n"
        "[Перейти в раздел](https://t.me/chatdorogakyoga/185)"
    )
    update.message.reply_text(text, parse_mode='Markdown')

def meditations(update: Update, context: CallbackContext):
    text = (
        "🎧 коллекция медитаций\n\n"
        "медитации под разное настроение — расслабиться, сфокусироваться, услышать себя или просто как следует выдохнуть.\n"
        "выбирай любую, устраивайся поудобнее, погружайся вглубь себя 🌿\n\n"
        "[Перейти в раздел](https://t.me/chatdorogakyoga/183)"
    )
    update.message.reply_text(text, parse_mode='Markdown')

def books(update: Update, context: CallbackContext):
    text = (
        "📚 полка с книгами\n\n"
        "идеальна для дождливых вечеров с чашкой чая ☕️📖\n"
        "мы делимся книгами, которые вдохновляют, поддерживают и помогают идти глубже в практику — телесную и внутреннюю.\n"
        "если хочешь порекомендовать что-то особенное — пиши нам ✨\n\n"
        "[Перейти в раздел](https://t.me/chatdorogakyoga/187)"
    )
    update.message.reply_text(text, parse_mode='Markdown')

def astrology(update: Update, context: CallbackContext):
    text = (
        "🔮 астрология\n\n"
        "в этом разделе мы исследуем влияние звёзд на нашу природу, раскрываем темы предназначения, периодов силы и поддерживающей энергии.\n"
        "если тебе интересно, как астрология может стать компасом в повседневности — тебе сюда ✨\n\n"
        "[Перейти в раздел](https://t.me/chatdorogakyoga/225)"
    )
    update.message.reply_text(text, parse_mode='Markdown')

def personal(update: Update, context: CallbackContext):
    text = (
        "💌 о личном из практики\n\n"
        "это раздел для искренности.\n"
        "о том, какие ощущения в асане, какие мысли в шавасане, как включить самодисциплину или есть меньше сладкого 🍬\n\n"
        "[Перейти в раздел](https://t.me/chatdorogakyoga/191)"
    )
    update.message.reply_text(text, parse_mode='Markdown')

def music(update: Update, context: CallbackContext):
    text = (
        "🎵 музыка\n\n"
        "плейлисты для йоги, медитации, пробуждения и шавасан.\n"
        "здесь — то, что звучит у нас в зале, и в наушниках на прогулке 🍃\n\n"
        "[Перейти в раздел](https://t.me/chatdorogakyoga/189)"
    )
    update.message.reply_text(text, parse_mode='Markdown')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("navigation", navigation))
    dp.add_handler(CommandHandler("schedule", schedule))
    dp.add_handler(CommandHandler("guide", guide))
    dp.add_handler(CommandHandler("contacts", contacts))
    dp.add_handler(CommandHandler("asanas", asanas))
    dp.add_handler(CommandHandler("pranayamas", pranayamas))
    dp.add_handler(CommandHandler("meditations", meditations))
    dp.add_handler(CommandHandler("books", books))
    dp.add_handler(CommandHandler("astrology", astrology))
    dp.add_handler(CommandHandler("personal", personal))
    dp.add_handler(CommandHandler("music", music))

    print("Бот запущен!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
