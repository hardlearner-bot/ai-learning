#读取文本文件，统计词频，打印前五名

def count_words(filename):
    word_freq = {}

    with open(filename) as f:
        text = f.read()

    print(text)
    words = text.split()
    print(words)

    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else: word_freq[word] = 1

    sorted_words = sorted(word_freq.items(), key=lambda s : s[1], reverse=True)

    print("打印出现次数最多的前五个单词")
    for word, count in sorted_words[:5]:
        print(f"{word}: {count}")

count_words("test.txt")



