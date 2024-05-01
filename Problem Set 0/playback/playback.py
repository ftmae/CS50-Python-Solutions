def slowdown(formatted):
    return formatted.replace(' ','...')
def main():
    user_input=input("What's on your mind? ")
    if not user_input:
        print('You responded with silence.')
    else:
        print(slowdown(user_input))
main()

