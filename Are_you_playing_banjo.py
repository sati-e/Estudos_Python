    # Create a function which answers the question "Are you playing banjo?".
    # If your name starts with the letter "R" or lower case "r", you are playing banjo!

    # The function takes a name as its only argument, and returns one of the following strings:

    # name + " plays banjo"
    # name + " does not play banjo"

    # Names given are always valid strings.

    def are_you_playing_banjo(name):
        first_letter = name[0]
        if first_letter.lower() == 'r':
            print(name, "plays banjo")
            return name + "plays banjo"
        else:
            print(name, "does not play banjo")
            return name + "does not play banjo"


    if __name__ == '__main__':
        name = input("Name: ")
        are_you_playing_banjo(name)