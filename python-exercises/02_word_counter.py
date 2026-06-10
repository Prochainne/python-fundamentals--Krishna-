def analyze_text(text):
    char_count = 0
    word_count = 0
    unique_words = 0
    char_count=len(text)
    word_count=len(text.split())
    unique_words=len(set(text.split()))
    return {
        "Character Count": char_count,
        "Word Count": word_count,
        "No. of Unique Words": unique_words
    }
with open("sample.txt", "r") as file:
    content = file.read()
    results = analyze_text(content)
    print(results)