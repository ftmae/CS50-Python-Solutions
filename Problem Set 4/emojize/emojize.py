import emoji

emoji_input = input("Input: ").strip()
if emoji_input:
    print("Output:", emoji.emojize(emoji_input, language="alias"))
else:
    print("No input provided.")
