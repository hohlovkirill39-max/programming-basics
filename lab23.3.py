#!/usr/bin/python3
import string

path = "/usr/share/licenses/imhex/LICENSE"

with open(path, mode="r", encoding="utf-8") as file:
    text = file.read()

text = text.lower()

for ch in string.punctuation:
    text = text.replace(ch, " ")

words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("***" * 10)

for rank in range(1, 11):
    max_word = max(word_count, key=word_count.get)
    count = word_count[max_word]
    print(f"{rank:2d}. {max_word:<15} : {count}")
    del word_count[max_word]
