def char_frequency(word: str) -> dict:
 
    freq = {}
    for ch in word:
        if ch.isalpha():  
            freq[ch] = freq.get(ch, 0) + 1
    return freq


text = input("Enter string: ")


words = text.replace(",", " ").split()

for word in words:
    result = char_frequency(word)
   
    formatted = ", ".join([f"{k}={v}" for k, v in result.items()])
    print(formatted)


