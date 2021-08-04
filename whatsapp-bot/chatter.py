from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Bot')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.Portuguese")

def getBotResponse(texto):
    return chatbot.get_response(texto).text