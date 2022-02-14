from itertools import product
import pyfiglet
from termcolor import colored
import random as r

List = ['3-d', '5lineoblique', 'acrobatic', 'avatar', 'banner', 'banner3',
        'barbwire', 'big', 'doh', 'doom', 'epic', 'graffiti',
        'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'nipples',
        'ntgreek', 'ogre', 'slant', 'smisome1', 'smkeyboard', 'smslant', 'stellar', 'starwars']
Color = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
Style = ['bold', 'dark', 'concealed']

L = r.randint(0, 26)
C = r.randint(0, 6)
S = r.randint(0, 2)
result = pyfiglet.figlet_format("Wordlister", font = List[L]  )
result = colored(result, Color[C] , attrs=[Style[S]])
print(result)

x = int(input("Minimum Number: "))
y = int(input("Maximum Number: "))
letters = input("Enter the characterss(without any gap): ")
name = input("Name of file: ")


def allwords(chars, length):
    for letters in product(chars, repeat=length):
        yield ''.join(letters)


def main():
    letters
    file = open("" + name + ".txt", "w")
    for wordlen in range(x, y + 1):
        for word in allwords(letters, wordlen):
            file.write(word + '\n')
            word = ''
    file.close()
    print("\n" + "Word list generated...")


main()
