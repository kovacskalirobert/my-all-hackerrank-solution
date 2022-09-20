
def minion_game(string):
    vowels = 'AEIOU'
    
    
    strl = len(string)

    kevin = int(sum(strl-i for i in range(strl) if string[i] in vowels))
    
    stuart = int(strl*(strl + 1)/2 - kevin)
    
    if kevin == stuart:
        print("Draw")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    elif stuart > kevin:
        print(f"Stuart {stuart}")


if __name__ == "__main__":
    s = "BANANA"
    minion_game(s)
    