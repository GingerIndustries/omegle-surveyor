from python_omegle.interestschat import InterestsChat
from python_omegle.randomchat import RandomChat
from python_omegle.chatevent import ChatEvent
from datetime import datetime
import random
from time import sleep
from better_profanity import profanity

words = ["banana", "tomato", "lever", "imbecile", "python", "phlegm", "encoding", "spaghet", "strftime", "apple", "appleapple", "printhead", "lcd", "ironing", "markup", "pango", "pi", "linux", "debian", "chatevent", "__init__", "segfault"]

cats = 0
dogs = 0
intro = 0
middle = 0
extro = 0
books = []
while True:
	print("Cats:", cats, "Dogs:", dogs, "Intro:", intro, "Middle:", middle, "Extro:", extro, "Books: ", books) 
	chat = InterestsChat(["computers", "programming", "python", "gtk", "minecraft", "linux", "raspberry pi", "legit human", "puzzled", "software", "coding", "helpful", "bored"])
	#chat = RandomChat()
	chat.start()
	print("Initiated chat, waiting to connect...")
	while True:
		event, argument = chat.get_event()
		if event == ChatEvent.CHAT_READY:
			print("Connected. Interests:", argument)
			break
	choice = random.choice(words)
	chat.send("Connection successful! Connected at " + datetime.now().strftime("%I:%M %P %-d/%-m/%Y"))
	sleep(0.5)
	chat.send("You're talking to Omegle Surveyor, a bot designed to ask questions of the people of Omegle, in the interest of science. To confirm your humanity, please type '" + choice + "'. (If you want no part in this, type 'nope' and I'll leave you alone.)")
	chat.send("BE CAREFUL NOT TO ADD SPACES TO THE PASSWORD")
	print("Password: " + choice)
	if choice == "lcd":
		chat.send("NOTE: That's an L, not an I")
	event = None
	arg = None
	while True:
		event, arg = chat.get_event()
		if event == ChatEvent.GOT_MESSAGE:
			print("Got message: " + arg)
			if arg.lower() == choice:
				break
			elif arg.lower() == "nope":
				chat.send("Ok, bye!")
				chat.disconnect()
				break
		elif event == ChatEvent.CHAT_ENDED:
			print("Chat ended. ;-;")
			break
	if event == ChatEvent.CHAT_ENDED:
		continue
	elif arg.lower() == "nope":
		continue
	print("success")
	chat.send("Ok, thanks. First question: Cats or dogs? Or both? ('skip' is a valid answer for all of these)")
	while True:
		event, arg = chat.get_event()
		if event == ChatEvent.GOT_MESSAGE:
			arg = arg.lower()
			print("Got message: " + arg)
			if arg == "cats":
				cats += 1
				break
			elif arg == "dogs":
				dogs += 1
				break
			elif arg == "skip":
				break
		elif event == ChatEvent.CHAT_ENDED:
			print("Chat ended. ;-;")
			chat.disconnect()
			break
	if event == ChatEvent.CHAT_ENDED:
		continue
	print("question 1 done")
	chat.send("Ok. Next, do you think of yourself as introverted, extoverted, or in-the-middle?")
	while True:
		event, arg = chat.get_event()
		if event == ChatEvent.GOT_MESSAGE:
			arg = arg.lower()
			print("Got message: " + arg)
			if arg == "introverted":
				intro += 1
				break
			elif arg == "extroverted":
				extro += 1
				break
			elif arg == "in-the-middle" or arg == "middle" or arg == "in the middle":
				middle += 1
				break
			elif arg.lower() == "skip":
				break
		elif event == ChatEvent.CHAT_ENDED:
			print("Chat ended. ;-;")
			chat.disconnect()
			break
	if event == ChatEvent.CHAT_ENDED:
		continue
	print("question 2 done")
	chat.send("Final question! About how big is the thickest book you own? (You can answer with any valid string - no sneaky \\n's, please!)")
	while True:
		event, arg = chat.get_event()
		if event == ChatEvent.GOT_MESSAGE:
			print("Got message: " + arg)
			if arg.lower() == "skip":
				break
			else:
				if profanity.contains_profanity(arg):
					chat.send("Watch your language!")
				else:
					books.append(arg)
					break
		elif event == ChatEvent.CHAT_ENDED:
			print("Chat ended. ;-;")
			chat.disconnect()
			break
	if event == ChatEvent.CHAT_ENDED:
		continue
	chat.send("Got it. Thanks for participating.")
	sleep(1)
	chat.send("Oh, and have a nice day! - GingerIndustries")
	sleep(0.5)
	chat.disconnect()
	print("done")
