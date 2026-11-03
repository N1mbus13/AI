import re
import random

# (pattern, replies) pairs. Use {0} to insert the captured text.
rules = [
    (r"hi|hello|hey",   ["Hello! How are you?", "Hi there! What's on your mind?"]),
    (r"my name is (.*)", ["Nice to meet you, {0}!"]),
    (r"i am (.*)",      ["Why are you {0}?", "How long have you been {0}?"]),
    (r"i feel (.*)",    ["Why do you feel {0}?", "Do you often feel {0}?"]),
    (r"i need (.*)",    ["Why do you need {0}?", "Would {0} really help you?"]),
    (r".*sorry.*",      ["No problem, no need to apologize!"]),
    (r".*help.*",       ["I'm here to help. What do you need?"]),
    (r".*",             ["Please tell me more.", "I see... go on.", "Why do you say that?"]),
]

def reply(text):
    for pattern, answers in rules:
        match = re.match(pattern, text)
        if match:
            return random.choice(answers).format(*match.groups())

print("ELIZA: Hi! I'm Eliza. Type 'bye' to exit.")
while True:
    text = input("You: ").lower().strip()
    if text in ("bye", "quit", "exit"):
        print("ELIZA: Goodbye! Have a great day!")
        break
    print("ELIZA:", reply(text))
