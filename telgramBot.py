import time
import telegram
from telegram.ext import Updater, CommandHandler
import logging
import Quiz
import datetime as dt
# Quiz.start()
que = Quiz.questions
ans = Quiz.answers
answer = Quiz.write
print("Question length:", len(que))
print("Question length:", ans)
TOKEN = "1453960586:AAE3B-dCuotUK6hC_pmi2tAfAotlmsil7jE"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
bot = telegram.Bot(token=TOKEN)


def Start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hello I am Bot")
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Bot has been started\n '/start' for introduction\n'/poll' for poll")


def quiz(update, context):
    """Send a predefined poll"""
    # message = update.effective_message.reply_poll(
    #     "તમે શું ક્વીશન કરો છો? ADS?erygewrhserhgrtjrejtyjrtktrjuytijroikrtjufgregrgrg?", questions,
    #     type=telegram.Poll.QUIZ, correct_option_id=2)
    date = dt.datetime.now().strftime("%I:%M:%S %p")
    text = "Poll Start at {} \nTotal {} Quetions".format(date, len(que))
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    for i in range(0, len(que)):
        longque = False
        if len(que[i]) > 300:
            longque = True

        for x in ans[i]:
            if len(x) > 99:
                longque = True
        if longque == True:
            print("Question", i, "has been skip for exceeding limit")
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Question {} has been skip for exceeding limit".format(i+1))
            continue
        message = update.effective_message.reply_poll(
            que[i], ans[i],
            type=telegram.Poll.QUIZ, correct_option_id=answer[i] - 1, explanation="Join: @swagatgk")
    print("Quiz Finish")
    date = dt.datetime.now().strftime("%I:%M:%S %p")
    text = "Poll End at {}".format(date)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    # # Save some info about the poll the bot_data for later use in receive_quiz_answer
    # payload = {
    #     message.poll.id: {"chat_id": update.effective_chat.id,
    #                       "message_id": message.message_id}
    # }
    # context.bot_data.update(payload)


start_handler = CommandHandler('start', Start)
dispatcher.add_handler(start_handler)
poll_handler = CommandHandler('poll', quiz)
dispatcher.add_handler(poll_handler)

print("Bot has been started\n '/start' for introduction\n'/poll' for poll")
updater.start_polling()
# updater.stop()
