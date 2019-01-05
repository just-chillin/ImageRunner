def main():
    print("Welcome to ImageRunner")
    Loop_var = True
    while Loop_var:
        path, lang = input("Please enter the file path and the programming language separated by a comma \n").split(",")
        print(path, lang)
        #OCR_main()




        print('Would you like to input another file? (Yes, Y, y, or No, N, n)')
        x = input()
        if(x == 'No' or x == 'N' or x == 'n'):
            Loop_var = False


if __name__ == "__main__":
    main()
