from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer

bot = ChatBot("Rex")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

# 语料库
trainer.train("chatterbot.corpus.chinese", "chatterbot.corpus.english")

trainer = ListTrainer(bot)

trainer.train([
    "你是?",
    "Hello",
    "你是谁?",
    "AI",
])

print("开始对话")
while True:
    try:
        user_input = input()
        bot_response = bot.get_response(user_input)
        print(bot_response)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
