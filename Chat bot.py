name = input("What's your name? ")
answer = input("How are you feeling today? ")
feeling_good = ["Good", "good", "ok", "Great", "great"]
feeling_bad = ["Bad", "bad", "not good"]

if answer == feeling_good:
    print("I'm happy to hear that", name)
elif answer == feeling_bad:
    print("I'm sorry to hear that", name)
else:
    print("Sorry could you tell me more")