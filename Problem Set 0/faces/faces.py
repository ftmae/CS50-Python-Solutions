def convert (user_input):
    return user_input.replace(':)','🙂').replace(':(','🙁')
def main():
    user_input=input('How are you feeling? (Express with emoticons)')
    if not user_input:
        print("You didn't say how you're feeling :(")
    else:
        print(convert(user_input))

main()

