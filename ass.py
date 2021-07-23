  
import speech_recognition as sr
import pyttsx3
import random as r


menu = ['Americano:45', 'Black:44', 'Coffee:46', 'Cappuccino:46', 'Espresso:45', 'Latte:33',
'Macchiato:35', 'Mocha:37', 'Cold:40','Tea:40','Coffee:42', 'Variety:49', 'Affogato:41', 'Cold:31',
'Brew:48', 'Iced:33', 'Coffee:44', 'Mazagran:37', 'Iced:47', 'Latte:47', 'Nitro:38', 'Cold:39', 'Brew:31']

prices = {'Americano': 45, 'Black': 44, 'Coffee': 44,
          'Cappuccino': 46, 'Espresso': 45, 'Latte': 47,
          'Macchiato': 35, 'Mocha': 37, 'Cold': 39, 'Tea': 40,
          'Variety': 49,'Affogato': 41, 'Brew': 31, 'Iced': 47,
          'Mazagran': 37, 'Nitro': 38}

billStack = []

def pmenu():
    print("Items | Prices")
    for i in menu:
        p = i.index(":")
        print("{} | {} ".format(i[:p],i[p:]))

def gen_bill():
    print("Items | Prices")
    total = 0
    for i in billStack:
        q,i = map(str,i.split())
        b = prices[i]
        total += int(q)*b
        print(" {} | {} x {} = {}".format(i,q,b,int(q)*b))
    print("Total : {}".format(total))    
    
        
def take_order():
    print("Please tell order in this Quantiy item order Example  Cofee")
    talk("Please tell order in this Quantiy item order Example 1 Cofee")
    
    i = 1
    while(i):
        temp = input()
        if temp == "ok":
            break
        else:
            order = temp
            billStack.append(order)
    print(billStack)    
    

def respond(command):
	responses = {
	"hello" : ["hello","hey..!","Hola"] ,
        "who are you ": ["I Am Your Virtual Assiant  ","I Am vasst","You can call me vasst"]
	}
	
	if command not in responses:
		return "Sorry..!"
	else:
		l = len(responses[command]) -1
		return 	responses[command][r.randint(0,l)]


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = "Sorry! i Coundn't get you"
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


def run_vasst():
    close = ["close","exit","logout","bye"]
    command = take_command()
    print(" You : {}".format(command))
    if command in close:
        print(" Vasst : {}".format("Good bye..!"))
        return 0
    elif command == "list" :
        pmenu()
    elif "take order" in command :
        take_order()
    elif "bill please" in command :
        gen_bill()    
    else:
        response = respond(command)
        print(" Vasst : {}".format(response))
        talk(response)
    return 1    
  


print(" Vasst : {}".format("I Am Your Virtual Assiant.... to assit you in ordering food"))
print("How can i help you ?")

start = 1
while start:
    start = run_vasst()
" Americano Black Coffee Cappuccino Espresso Latte Macchiato Mocha Cold Coffee Variety Affogato Cold Brew Iced Coffee Mazagran Iced Latte Nitro Cold Brew "   


"""
output :
 Vasst : I Am Your Virtual Assiant.... to assit you in ordering food
How can i help you ?
listening...
 You : 1 order
 Vasst : Sorry..!
listening...
 You : Sorry! i Coundn't get you
 Vasst : Sorry..!
listening...
 You : take order
Please tell order in this Quantiy item order Example  Cofee
1 Coffee
1 Tea
ok
['1 Coffee', '1 Tea']
listening...
 You : bill please
Items | Prices
 Coffee | 1 x 44 = 44
 Tea | 1 x 40 = 40
Total : 84
listening...
 You : exit
 Vasst : Good bye..!
 
 """
