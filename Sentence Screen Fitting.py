def wordsTyping(sentence, row, col):
	full = ""
	for i in sentence:
		full += (i + " ")
	start = 0
	length = len(full)

	for i in range(row):
		start += col
		if(full[start % length] == " "):
			start += 1
		else:
			while(start > 0 and full[(start - 1)% length] != " "):
				start -= 1

	return int(start / length)

sentence = ["a", "bcd", "e"]
print(wordsTyping(sentence, 3, 6))