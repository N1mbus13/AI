# Rule-Based Chatbot using simple pattern matching
import re
import random

# Define chatbot responses as patterns and replies
patterns = {
    r"hi|hello|hey": [
        "Hello! How are you today?",
        "Hi there! What's on your mind?",
        "Hey! How can I help you?"
    ],
    r"my name is (.*)": [
        "Nice to meet you, %1!",
        "Hello %1! How are you doing today?"
    ],
    r"i am (.*)": [
        "Why are you %1?",
        "How long have you been %1?",
        "What makes you feel %1?"
    ],
    r"i feel (.*)": [
        "Why do you feel %1?",
        "Do you often feel %1?",
        "What caused you to feel %1?"
    ],
    r"i need (.*)": [
        "Why do you need %1?",
        "Would it really help you to get %1?",
        "Are you sure you need %1?"
    ],
    r"because (.*)": [
        "Is that the real reason?",
        "What other reasons might there be?",
        "Does that reason explain anything else?"
    ],
    r"(.*) sorry (.*)": [
        "It's okay, no worries!",
        "No problem, I understand.",
        "You don't have to apologize."
    ],
    r"(.*) help (.*)": [
        "I'm here to help. What do you need?",
        "Sure! Tell me more about how I can assist you."
    ],
    r"quit|bye|exit": [
        "Goodbye! Have a great day!",
        "It was nice talking to you. Bye!"
    ],
    r"(.*)": [
        "Please tell me more.",
        "I see... go on.",
        "Why do you say that?",
        "Can you explain that in detail?"
    ]
}

# Chatbot main loop
def eliza_chatbot():
    print("ELIZA: Hi! I'm Eliza, your virtual therapist. Type 'bye' to exit.\n")
    while True:
        user_input = input("You: ").lower()
        for pattern, responses in patterns.items():
            match = re.match(pattern, user_input)
            if match:
                response = random.choice(responses)
                for i, group in enumerate(match.groups(), 1):
                    response = response.replace(f"%{i}", group)
                print("ELIZA:", response)
                break
        if re.search(r"bye|quit|exit", user_input):
            break

# Run the chatbot
eliza_chatbot()