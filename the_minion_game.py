

data = set()


def minion_game(string):
    for i in range(len(string)):
        row = string[i]
        for j in range(len(string)):
            col = string[j]

            data.add(string[i: (j + 1)])

    data.remove("")

    #  print(data, len(data))

    vowels = []
    consonants = []
    game = dict()

    for item in data:
        if item[0] in "AEIOU":
            vowels.append(item)
        else:
            consonants.append(item)

    kevin_score = 0
    for vowel in vowels:
        # print(vowel)
        indices = [index for index in range(
            len(string)) if string.startswith(vowel, index)]
        kevin_score += len(indices)
    # print(kevin_score)

    stuart_score = 0
    for consonant in consonants:
        # print(vowel)
        indices = [index for index in range(
            len(string)) if string.startswith(consonant, index)]
        stuart_score += len(indices)
    # print(stuart_score)

    if kevin_score == stuart_score:
        print("Draw")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")


if __name__ == "__main__":
    s = "BANANA"
    minion_game(s)
