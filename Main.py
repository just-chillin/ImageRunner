import json
def main():
    print("Welcome to ImageRunner")
    Loop = True
    First_prompt = True
    while Loop:
        Incor = True
        while First_prompt:
            #loop runs at least once and requests 2 inputs from the user
            result = input("Please enter the file path and the programming language separated by a comma\n").split(",")
            print(len(result))
            if(len(result) < 2):
                print("Missing one of the inputs")
            elif(len(result) > 2):
                print("Too many inputs")
            else:
                First_prompt = False
        #after confirming the user gave 2 inputs they are stored
        path = result[0]
        lang = result[1]
        #OCR_main()

        #This loop runs to ensure the user enters a correct value to the question
        while(Incor):
            #prompts the user to run the program again or exits
            x = input('Would you like to input another file? (Yes, yes, Y, y, or No, no, N, n)\n')
            if (x == 'Yes' or x == 'Y' or x == 'y' or x == 'yes'):
                First_prompt = True
                Incor = False
            if(x == 'No' or x == 'N' or x == 'n' or x == 'no'):
                Loop = False
                Incor = False

    print("You've reached the end of the program!")

if __name__ == "__main__":
    main()
