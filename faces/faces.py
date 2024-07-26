#Lets define main function
def main():
    #Taking input from the user
    chat = input()
    #using the convert fumction to change emoticon
    msg = convert(chat)
    print(msg)
#creating the convert function to replace emoticon to emojis
def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")
main()
