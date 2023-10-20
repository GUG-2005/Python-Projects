change = "[name]"

with open("./Input/Names/invited_names.txt") as name:
    name_list = name.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    lett_content = letter.read()
    for i in name_list:
        new_letter = lett_content.replace(change, i)
        i = i.strip("\n")
        with open(f"./Output/ReadyToSend/{i}.txt", "w") as file:
            file.write(new_letter)
