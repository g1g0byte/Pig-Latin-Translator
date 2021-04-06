import re

vowels = 'aeiou'
ending_punctuation = ',.;:!?)'
starting_punctuation = '(#@'

def main():
	words = re.findall(r"[\w']+|[,.;:!?()#@]", text) # create array containing words and punctuation from the text
	translated_words = []
	for i,word in enumerate(words):
		if word[0].lower() in vowels:  # if first letter is a vowel than add 'way' to the end
			translated_words.append(word + "way ")

		elif word in starting_punctuation:
			translated_words.append(word)	# if it is a character like '(' for example then we do not want a space after it
		elif word in ending_punctuation:
			translated_words[i-1] = translated_words[i-1].rstrip()	# remove space before this punctuation by stripping the space of last element in the list
			translated_words.append(word + " ")
	
		elif word.isdigit():
			translated_words.append(word + " ")
		else:
			chars_to_delete = 0	# amount of characters to delete from beginning of string
			chars_to_add = []
			for char in word:
				if char in vowels:	# stop looping through consonant cluster once vowel is found
					break
				else:
					chars_to_delete += 1
					chars_to_add.append(char.lower())

			translated_words.append(word[chars_to_delete:] + "".join(chars_to_add) + "ay ")

			if word[0].isupper():	# check if the current word is and should be capitalised
				translated_words[i] = translated_words[i].capitalize()
	
	translated_text = "".join(translated_words)	# create translated text by combining all elements in the 'translated_words' list
	translated_text = translated_text.rstrip()
	write_file(translated_text)	# write the translated text to a txt file

def read_file():
	with open('text.txt', 'r') as file:
		text = file.read().replace('\n', '')
	return text

def write_file(translated_text):
	with open('translated_text.txt', 'w') as file:
		file.write(translated_text)

if __name__ == "__main__":
	text = read_file()
	main()
