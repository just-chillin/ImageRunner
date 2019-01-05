print("Welcome to ImageRunner")
Loop_var = True
while Loop_var:
    print("Please enter the file path ")
    Path_var = input()
    print("Please enter the programming language ")
    Lang_var = input()
    #This is where the program runs
    print('Would you like to input another file? (Yes, Y, y, or No, N, n)')
    x = input()
    if(x == 'No' or x == 'N' or x == 'n'):
        Loop_var = False
