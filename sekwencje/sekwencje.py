sentence = "Ala ma kota, a kot ma Ale."

#oczyść zdanie ze znaków interpunkcyjnych

sentence = sentence.replace(",", "")
sentence = sentence.replace(".", "")
print(sentence)

##zapisz wszytskie słowa w zdaniu w liscie words

words = sentence.split(" ")
print(words)