from datetime import datetime

def chatbot():
    print("chatbot: Hello! whats your name?")
    name = input("you: ")
    print(f"chatbot: nice to meet you,{name}!")
    print("type 'help' to see commands or 'bye' to exit.\n")
    while True:
        user = input(f"{name}:").lower()
        if user == "hello":
           print("chatbot: Hello! How can I help you?")
        elif user == "how are you":
           print("  ChatBot: I'm doing great!")
        elif user == "your name":
           print("chatbot:your name is{name}.")
        elif user == "time":
           print("chatbot:",datetime.now().strftime("%h:%m:%s"))
        elif user =="date":
           print("chatbot:",datetime.now().strftime("%d-%m-5y"))
        elif user =="help":
           print("""
Available Commands:
hello
how are you
your name
my name
time
date
bye
""")
        elif user=="bye":
            print(f"chatbot:goodbye,{name}!")
            break
        else:
            print("chatbot:sorry,i dont understand that.")
chatbot()
                                            
        
