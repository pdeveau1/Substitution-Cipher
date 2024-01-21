import random
import string

ABC = list(string.ascii_lowercase)

class Substitution_Cipher:
    def __init__(self):
        self.text = ""
        self.author = ""
        self.code = []
        self.encoded_text = ""

    def get_text(self):
        file = open("text.txt", "r")
        lines = file.readlines()  
        num_lines = len(lines)
        line_num = random.randint(0, (num_lines - 1))
        line = lines[line_num]
        line = line.split('-')
        self.text = line[0]
        self.author = line[1]

    def generate_code(self):
        abc = ABC
        random.shuffle(abc)
        self.code = abc

    def encode(self):
        encoded_text = list(self.text)
        for i in range(len(self.text)):
            if (self.text[i]).isalpha():
                pos = ord((self.text[i]).lower()) - ord('a')
                encoded_text[i] = self.code[pos]
            else:
                encoded_text[i] = self.text[i]
        self.encoded_text = ''.join(encoded_text)

    def check_anser(self, answer):
        while(answer != self.text):
            answer = input("Guess again")
        print("You got the quote by {} right!".format(self.author))
