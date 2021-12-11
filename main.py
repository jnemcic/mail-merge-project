# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", mode="r") as names:
    names_content = names.read()
    names_list = names_content.splitlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_template:
    template_letter_content = letter_template.read()
    for name in names_list:
        stripped_name = name.strip()
        with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as new_letter:
            new_letter.write(template_letter_content.replace(PLACEHOLDER, f"{stripped_name}"))


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
