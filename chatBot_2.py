chatbot_response = {
    "hello": "Hi there! How can I help you?"
}
greet = input("chat with AI : ")

if greet in chatbot_response:
    print(chatbot_response[greet])