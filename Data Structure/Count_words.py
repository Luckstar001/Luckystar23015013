def count_words(input_string):
    input_string = input_string.lower()
    words_list = input_string.split()
    word_counts = {}
    for word in words_list:
        cleaned_word = word.strip(".,!?")
        if cleaned_word:
            word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1
    return word_counts
user_input = input("Enter a sentence or paragraph: ")
result = count_words(user_input)
for word, count in result.items():
    print(f"{word}: {count}")
