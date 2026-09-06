#Kevin and Stuart want to play the 'The Minion Game'.


"""Game Rules
Both players are given the same string,S .
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.  """

#Scoring
#A player gets +1 point for each occurrence of the substring in the string S .

#For Example:
#String S = BANANA
#Kevin's vowel beginning word = ANA
#Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.


#Your task is to determine the winner of the game and their score.
#Function Description
#Complete the minion_game in the editor below.
#minion_game has the following parameters:
#string string: the string to analyze

#Prints
#string: the winner's name and score, separated by a space on one line, or Draw if there is no winner

#Input Format

#A single line of input containing the string s .
#Note: The string s will contain only uppercase letters:[A-Z] .

#Constraints
#0<len(s)<=10^6


"""def minion_game(string):
    vowels = set('AEIOU')
    n = len(string)
    kevin = 0
    stuart = 0
    for i in range(n):
        # A substring starting at index i contributes (n - i) substrings
        # (one of each length from 1 to n-i). Award them to the right player
        # based on the starting letter.
        if string[i] in vowels:
            kevin += (n - i)
        else:
            stuart += (n - i)
    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif stuart > kevin:
        print(f"Stuart {stuart}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input().strip()
    minion_game(s)"""


def minion_game(string):
    vowels = set('AEIOU')
    n = len(string)
    kevin = 0
    stuart = 0
    for i in range(n):
        if string[i] in vowels:
            kevin += (n - i)
        else:
            stuart += (n - i)
    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif stuart > kevin:
        print(f"Stuart {stuart}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input().strip()
    minion_game(s)





#ye mere ko nhi aata aabhi too par baad ka pata nhi 
