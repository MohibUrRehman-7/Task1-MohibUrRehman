while True:
    user_input= input("Type here:")
    Input=user_input.lower().strip()
    if Input == 'exit':
        print("Bye!👋")
        break
    else:

        responses={
        'hi' : 'hello👋 ' ,
        'hey' : 'hi , what\'s up👋' ,
        'how are you' : 'i\'m fine👌' , 
        'good morning' : 'Have you done your breakfast?😁' ,
        'good night' : 'Have you done your dinner?😁',
        'no' : 'That is not nice!😒' , 
        'yes' : 'Nice !<3❤️',
        'what is your name' : 'I\'m your chatbot friend'
        }
        reply= responses.get(Input,"I dont Understand")
       
        print(reply)