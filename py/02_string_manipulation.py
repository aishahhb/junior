#String Creation
single_qoute = 'Python' #Single Quote (one liner)
double_qoute = "Python" #Double Quote (one liner) -> always used this!!
triple_qoute = """"Multiple
line
string
to
count
""" #Triple Quote (multi liner)

#note: because not used single qoute because u need to add \ to declare the string
example = 'i don\' like this language'


#String indexing and slicing
#Indexing: number(position) for each character
#Slicing: grabbing multiple characters [start:stop:step]

text = "Python Programming"
print("First Character: ", text[0])
print("Last Character: ", text[-1])
print("Slice 0 to 5:"", ", text[0:6]) #0 is start, 6 is end
print("From start to 5: ", text[:6])
print("7 to end: ", text[7:])
print("Just random: ", text[6:-4])




#Exercise:
#1.Build  a  simple  text  analyzer  that  counts  words,  characters,  and sentences in a given text.
text = """Python is a powerful programming language. It's easy to learn
and versatile!You  can  use  Python  for  web  development,  data  science,  andautomation.
The syntax is clean and readable.This makes Python perfect for beginners and experts alike."""

# Count words (split by whitespace)
num_words = len(text.split())
print("Count words:", num_words)

# Count characters (including spaces)
num_characters = len(text)
print("Count characters:", num_characters)

# Count sentences 


