import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you today?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine, thank you! How about you?"]
    ],
    [
        r"(.*) your name ?",
        ["My name is ChatBot. What's yours?", "I'm ChatBot. What about you?"]
    ],
    [
        r"what (.*) want ?",
        ["I'm here to assist you. Just ask me anything.", "I'm here to help. What do you need?"]
    ],
    [
        r"(.*) (good|great|fine)",
        ["That's wonderful!", "Glad to hear that!"]
    ],
    [
        r"(.*) (bad|not good)",
        ["I'm sorry to hear that. How can I help you?", "Is there anything I can assist you with?"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you please rephrase?", "I'm not sure I understand. Could you elaborate?"]
    ]
]

# Create a chatbot with the defined patterns
chatbot = Chat(pairs, reflections)

# Start chatting
print("Welcome to ChatBot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    else:
        print("ChatBot:", chatbot.respond(user_input))
