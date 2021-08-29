from numpy import random
from gtts import gTTS
import os

# Default numbers for practice = 5.
numbers = random.randint(100, size=(5)) 

string = "   ".join([str(i) for i in numbers])

# Space to prevents the audio file from an abrupt end.
string = string + " " 

# Default language = French.
language = 'fr' 

# Speed can be adjusted via 'slow' parameter.
output = gTTS(text = string, lang= language, slow=False) 

output.save("lesnombresenfrancaisfast.mp3")
os.system("start lesnombresenfrancaisfast.mp3")

print(numbers)


