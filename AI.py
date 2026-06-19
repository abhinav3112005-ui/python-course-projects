# #to create a conversational AI Aassistant using python's core logic-strings,functions,dictionaries and loops
# import datetime
# import time
# name=input("enter a nname:")
# presentHour=datetime.datetime.now().hour

# if 5 <= presentHour <=11:
#     print("goof morning",name)
# else:
#     print("good night",name)
    



print("welcome to the AI based chatbot")
print("you can ask me basic questions,type 'bye' to exit")


#chatbot memory[dictionary of mresponses]

responses={
    "hello":"hi, welcome how can i help you!!!",
    "how are you": "i'm fine arigato",
    "who are you": "i a ai chatbot and finder",
    "motivate me" : "be the green lantern light",
    "happy":"gotcha"
    
    
}
#method of func
def getresponseBot(userquestion):
    userquestion=userquestion.lower()
    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]
        
    return "i am not able to file thatv yet"    



#take user input
while True:
   userinput=input("please ask your question:")
   
   if "bye" in userinput.lower():
        print("goodbye")
        break

   
   
   reply=getresponseBot(userinput)
   print("bot response",reply)

