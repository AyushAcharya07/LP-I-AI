import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Simp_Chatbot and I'm a simple NLTK based chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)|sorry",
        ["It's alright","No problem",]
    ],
    [
        r"i'm (.*) doing good|i am good|good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age? |age",
        ["I'm a computer program, I don't have an age.",]
    ],
    [
        r"quit|bye|exit|bye ()",
        ["Bye, take care. See you soon! :)", "It was nice talking to you. Bye!"]
    ],
    [
        r"how (can|do) I (find|get) (.*)",
        ["You can try searching on Google for %3.", "You might find %3 by looking on the internet."]
    ],
    [
        r"what is (.*)",
        ["%1 is something I'm not entirely sure about. Can you provide more context?", "I'm not certain about %1. Could you elaborate?"]
    ],
    [
        r"tell me about yourself",
        ["I'm a chatbot created using NLTK. I'm here to chat with you and answer your questions."]
    ],
    [
        r"(.*) (weather|forecast) (.*)|weather",
        ["You can check the weather forecast by visiting a weather website like Weather.com or using a weather app on your phone."]
    ],
    [
        r"(.*) (movie|film|series)",
        ["I'm not capable of watching movies, but I can recommend some popular ones if you'd like."]
    ],
    [
        r"(.*) (sport|game)",
        ["I'm not into sports myself, but I can tell you about different sports if you're interested."]
    ],
    [
        r"(.*) (book|author)",
        ["Books are fascinating! There are so many genres and authors to explore. What kind of books do you like?"]
    ],
    [
        r"(.*) (music|song|band)",
        ["Music is great! What genre or artist are you interested in?"]
    ],

]

pairs = [[pattern.lower(), response] for pattern, response in pairs]

chatbot = Chat(pairs, reflections)

def chat():
    print("Hi, I'm a simple chatbot. You can talk to me. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase
        response = chatbot.respond(user_input)
        print("Bot:", response)
        if any(word in user_input for word in ['quit', 'bye']):
            break

if __name__ == "__main__":
    chat()
