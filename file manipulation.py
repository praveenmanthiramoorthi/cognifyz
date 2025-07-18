with open(input(), 'r') as f:
    text = f.read().lower()

words = text.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

for word in sorted(count):
    print(word, count[word])
