

bot_response = {"Hi": "Good morning",
                "How are you": "I am fine",
                "What's ur name" : "Chatbot",
                "what you do":"i am chatbot"
}

user = input("ask a question : ")

if user in bot_response:
    print(bot_response[user])
else:
    print("ask another question")


user2= input("ask a question : ")

if user2 in bot_response:
    print(bot_response[user2])


user3= input("ask a question : ")

if user3 in bot_response:
    print(bot_response[user3])