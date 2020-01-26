import logging

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)



A, B, C, D = range(4)




def Start(update, context):

    update.message.reply_text('''Hallo. \nIch bin ein mediationsbot''')

    update.message.reply_photo(photo=open('januar_25/Bilder/hi.png', 'rb'))


    update.message.reply_text( '''Ich erkläre euch kurz den Ablauf der Mediation.
Ich werde euch durch einen strukturierten Ablauf führen,
um am Ende möglicherweise eine Lösung für euren Konflikt zu
finden.''')
    update.message.reply_text('''Wenn ihr eure Gedanken auf eine Frage für euch ausreichend
    formuliert habt, dann sendet bitte beide einen Sticker.
    Erst wenn ihr das beide bestätigt habt, können wir zum
    nächsten Schritt übergehen.''')

    update.message.reply_photo(photo=open('januar_25/Bilder/next.png', 'rb'))


    return A






def a(update, context):

    reply_keyboard = [['ja', 'nein']]


        update.message.reply_photo(photo=open('januar_25/Bilder/start.png', 'rb',

        update.message.reply_text('Bist du mit der Mediation einverstanden?',
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))


        return B



num_users = 2
stickers_sent = {}

def b(update, context):


    if not update.effective_user.is_bot:
        stickers_sent[update.effective_user.id] = True

    if len(stickers_sent) == num_users:
        update.message.reply_text('Frage 1',
                            reply_markup=ReplyKeyboardRemove()))

        stickers_sent = {}

        return C
    else:
        return B




def c(update, context):
    if not update.effective_user.is_bot:
        stickers_sent[update.effective_user.id] = True

    if len(stickers_sent) == num_users:
        update.message.reply_text('Frage 2')
        stickers_sent = {}

        return D
    else:
        return C


def d(update, context):
    if not update.effective_user.is_bot:
        stickers_sent[update.effective_user.id] = True

    if len(stickers_sent) == num_users:
        update.message.reply_text('Frage 3')
        stickers_sent = {}
        return A
    else:
        return D



def end(update, context):

    update.message.reply_text('Abbruch')

    return ConversationHandler.END




def cancel(update, context):

    update.message.reply_text('Abbruch',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END












def main():

    updater = Updater("836079024:AAEDt3Tc8qFuzJ3OW2K_foyTr8vfEP-9JV8", use_context=True)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={

            A: [MessageHandler(Filters.sticker, a)],

            B: [MessageHandler(Filters.regex('^(ja|nein)$'), b)],

            C: [MessageHandler(Filters.sticker, c)],

            D: [MessageHandler(Filters.sticker, d)],

        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)


    updater.start_polling()


    updater.idle()


if __name__ == '__main__':
    main()