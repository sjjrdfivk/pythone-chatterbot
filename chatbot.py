from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new instance of a ChatBot
bot = ChatBot(
    'Rex',
    # storage_adapter='chatterbot.storage.SQLStorageAdapter',
    # logic_adapters=[
    #     'chatterbot.logic.MathematicalEvaluation',
    #     'chatterbot.logic.TimeLogicAdapter',
    #     'chatterbot.logic.BestMatch'
    # ],
    # database_uri='sqlite:///database.sqlite3'
)

trainer = ListTrainer(bot)

trainer.train([
    "Hi there!",
    "Hello",
])

trainer.train([
    "Greetings!",
    "Hello1",
])

print('Type something to begin...')

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
