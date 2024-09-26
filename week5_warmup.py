# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
text= "abracadabra"
print(text[4])

# b. Retrieve the second to last character.
print(text[9])

# c. Find the first occurrence of the letter 'c'.
substring = text.find("c")
print(substring)
subtring = text[4]
print(substring)

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
text2 = "abcdefghijklmnopqrstuvwxyz"

# a. Extract the letters 'hij'.
substring = text2.find("hij")
print(substring)
substring = text2[8:10]
print(substring)

# b. Extract every second letter starting from 'a' to 'm'.
print(text2[0:-1:2])

# c. Reverse the entire string using slicing.
print(text2[-3])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
text3 = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
substring = text3.find("John F. Kennedy")
print (substring)
substring = text3[83:]
print(substring)

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
text4= "Python is fun. Fun is good. Good is subjective"

# a. Extract the word 'subjective' without knowing its exact position.
substring = text4.find("subjective")
print(substring)
substring = text4[36:47]
print(substring)

# b. Extract every third word.
print(text4[0:-1:3])

# c. Reverse the positions of the words, but keep the characters in each word in the same order.
print(text4[::-1]) # print "evitcejbus si dooG .doog si nuF .nuf si nohtyP"

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
text5= "MAY THE FORCE BE WITH YOU."
print(text5.lower())

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],


# a. Convert the list into a single string.
word_list = ["Make", "haste", "slowly."]
joined_list = " " .join(word_list)    
print(joined_list) # prints Make haste slowly. (A space between each word)

# b. Now, split the string at every occurrence of the letter 'a'.
sentence2 = "Make haste slowly."
split_sentence=sentence2.split()
print(split_sentence) # prints ['Make', 'haste', 'slowly.']


# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
sentence= "Life is what happens when you are busy making other plans."
new_sentence = sentence.replace("busy", "distracted")
print(new_sentence)

# b. Replace "plans" with "mistakes".
sentence3= sentence.replace("plans", "mistakes")
print(sentence3)


# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
repetition = "Iteration" * 7
print(repetition)

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
poem = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
print(poem.find("moonlight"))

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
line= "Supercalifragilisticexpialidocious"
alphabet = str("a", "b", "c", "d", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z")
counter = line.count(alphabet)
print("Number of characters in Supercalifragilisticexpialidocious is: " + str(counter))

# b. Count the number of times the letter 'i' appears in the same word/phrase.
counter2 = line.count('i')
print("Count of i in Supercalifragilisticexpialidocious is : " + str(counter2))   # prints out that there is 7 "i's"
