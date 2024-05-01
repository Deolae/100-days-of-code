# Open files for the text and the names
with open("Input/Letters/starting_letter.txt", mode="r") as startingTxt:
    with open("Input/Names/invited_names.txt", mode="r") as namesTxt:
        # Read the names text
        invited_names = namesTxt.readlines()

    # Read the starting text
    startingTxt = startingTxt.read().strip()

    # Loop over names
    for name in invited_names:
        # Strip spaces from name
        name = name.strip()
        # Replace the "[name]" in the text letter with the actual name
        finalTxt = startingTxt.replace("[name]", name)
        # Write a new letter with each name
        with open(f"Output/ReadyToSend/{name}.txt", mode="w") as namesfile:
            namesfile.write(finalTxt)
