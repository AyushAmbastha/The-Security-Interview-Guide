def  emojiConverter(message):
    words = message.split(" ")
    emojis = {
    ":)" : "😀",
    ":(" : "😞",
    "lol" : "😂",
    "sick":"😨",
    "happy": "😀",
    "mermaid": "🧜‍"
    }
    outcome = " "
    for word in words:
        outcome += emojis.get(word, word) + " "
    return outcome

message = "I am sad :("
print(emojiConverter(message))