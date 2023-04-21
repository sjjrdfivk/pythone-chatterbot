from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

bot = ChatBot("Rex",
              logic_adapters=[
                  {
                      'import_path': 'customAdapter.CustomAdapter'
                  }
              ]
)

# 创建新的训练器
trainer = ChatterBotCorpusTrainer(bot)

# 语料库
trainer.train("chatterbot.corpus.chinese", "chatterbot.corpus.english")

trainer = ListTrainer(bot)

trainer.train([
    "你是",
    "Rex",
    "你是谁",
    "REX大哥",
])

trainer.train([
    "吃饭了吗",
    "没有",
])

print("开始对话")
while True:
    try:
        user_input = input()
        bot_response = bot.get_response(user_input)
        print(bot_response)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
