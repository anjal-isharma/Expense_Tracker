import re
import random


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    return text


responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how_are_you": ["I'm just code, but I'm doing great 😄", "All good! What about you?"],
    "name": ["I'm your Python chatbot 🤖", "You can call me ChatPy!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
    "default": ["I didn't understand that 🤔", "Can you rephrase?", "Hmm, interesting... tell me more."]
}


def get_intent(user_input):
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif "how are you" in user_input:
        return "how_are_you"
    elif "your name" in user_input:
        return "name"
    elif any(word in user_input for word in ["bye", "exit", "quit"]):
        return "bye"
    else:
        return "default"


print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    cleaned = clean_text(user_input)

    intent = get_intent(cleaned)
    response = random.choice(responses[intent])

    print("🤖 Chatbot:", response)

    if intent == "bye":
        break