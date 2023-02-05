#TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
with open("./Input/Names/invited_names.txt") as names_file:
    list_name = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
        letter_contents = letter_file.read()
        for name in list_name:
            strip_name=name.strip()
            new_letter = letter_contents.replace(PLACEHOLDER, strip_name)
            #Dibaca dahulu sebelum direplace, kalau tidak nanti error
            with open(f"./Output/ReadyToSend/letter_for_{strip_name}.txt", mode="w") as completed_letter:
                completed_letter.write(new_letter)


#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp


#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
