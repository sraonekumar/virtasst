import random as r
def respond(command):
	responses = {
	"hello" : ["hello","hey..!","How are you"]
	}
	
	if command not in responses:
		return "Sorry..!"
	else:
		l = len(responses[command]) -1
		return 	responses[command][r.randint(0,l)]

print("I Am Your Virtual Assiant....")
print("How can i help you ?")
command  = ""
close = ["close","exit","logout","bye"]
while(True):
	command = input()
	if command in close:
		print("Good bye master")
		break
	else:
		print(respond(command))

