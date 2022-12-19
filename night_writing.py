# Defines the alphabet for the chart to use
ALPHABET = 'abcdefghijklmnopqrstuvwxy'
# Parameters are row and col and returns the letter
def translate_char(row, col):
  # The formula used is 5 times the row-1 plus the col-1
  return ALPHABET[5*int(row)+int(col)-6]

# Used to translate a letter to row col format
def translate_letter(letter):
  # Obtains the position of the letter
  pos = ALPHABET.find(letter)
  # Does the inverse of the translate_char function
  return str(int(pos/5)+1) + str(pos%5+1)

# decodes the message 
def translate_message(s):
  decoded = ""
  i=0
  while i < len(s)-1:
    # this checks if there is a space, if there is, then its position will change to position + 1
    if s[i] == " ":
      decoded += " "
      i += 1
    # Otherwise, translate the next two numbers and increment twice
    else:
      decoded += translate_char(s[i],s[i+1])
      i += 2
  return decoded

def night_write(s):
  # This converts the string to lowercase
  s = s.lower()  
  encoded = ""
  # Goes through each letter and encodes it, or adds a space
  for i in range(len(s)):
    if s[i] == " ":
      encoded += " "
    else:
      encoded += translate_letter(s[i])
  return encoded

#Tests
print(translate_message("23115215 11 2243151145 445133331543 113414 1443243431 32354544 3521 5311451543"))
print(night_write("have a great summer and drink lots of water"))
