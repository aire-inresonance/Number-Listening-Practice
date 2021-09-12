from numpy import random
from gtts import gTTS
import os
import collections
# Default numbers for practice = 5.
number_of_numbers = 5

answer = random.randint(100, size=(number_of_numbers)) 

string = "  ".join([str(i) for i in answer])


# Default language = French.
language = 'fr' 

# Speed can be adjusted via 'slow' parameter.
output = gTTS(text = string, lang= language, slow=False) 

output.save("lesnombresenfrancaisfast.mp3")
os.system("start lesnombresenfrancaisfast.mp3")



guess = []
# Guessing input 
for ii in range (0, number_of_numbers):
    guess_num = int(input("Insert each number, end with SPACE: "))
    guess.append(guess_num)

# Output
if collections.Counter(guess) == collections.Counter(answer):
    print("Correct!")
else:
    print("False!")

print('Your guess:', guess)
print('The answer', list(answer))



