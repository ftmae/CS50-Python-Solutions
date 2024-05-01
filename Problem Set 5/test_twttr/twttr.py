vowels = ['a','e','i','o','u','A','E','I','O','U']
def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")

def shorten(word):
    return "".join(char for char in word if char not in vowels)

if __name__ == "__main__":
    main()
