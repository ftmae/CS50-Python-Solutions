vowels = ['a','i','e','i','o','u','A','E','I','O','U']
def remove_vowels(user_input):
    return "".join(char for char in user_input if char not in vowels) # join takes in all items in an iterable and puts it in a string specified
def main():
    user_input = input("Input: ")
    print(f"Output: {remove_vowels(user_input)}")

main()
