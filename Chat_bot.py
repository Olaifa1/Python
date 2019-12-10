my_dict = {"hello!": "Hi",
           "howdy?": "I'm fine",
           "how is your family today?": "They doing well. Thanks Waliu.",
           "what is land mass of nigeria?": "The land mass of Nigeria is 923,774 sq km, Waliu",
           "how many countries are in africa?":  "There are 54 of them.",
           "default": "Don't get you, Sir."
           }

             
while True:
    respondent = input("Say what is in your mind: ").lower()
    if respondent == "Quit":
        print("Quit!")
        break
    if respondent in my_dict:
        print(my_dict[respondent])
        print(" ")

    else:
        print(my_dict["default"])
              
        print(" ")
        
