import json


def prompt_user():
    # Prompt the user for a language
    print("Welcome to ImageRunner")
    path = input("Please enter the path to the image: ")
    language = input("Please enter the programming language: ")
    return path, language


def main():
    path, language = prompt_user()


if __name__ == '__main__':
    main()
