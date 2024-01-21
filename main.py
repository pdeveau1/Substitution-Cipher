from substitution_cipher import Substitution_Cipher
def main():
    sc = Substitution_Cipher()
    sc.get_text()
    sc.generate_code()
    sc.encode()
    print(sc.encoded_text)

if __name__=="__main__":
    main()