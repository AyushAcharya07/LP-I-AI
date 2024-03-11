import random
name="Ash Chatbot"
weather=["Sunny","Cloudy","Humid","Thunderstorm"]
season=["Summer","Spring","Autumn","Winter"]
states_cnt=29

resp=[
	{"question":"hi","answer":"Hello!"},
	{"question":"what is your name","answer":"My Name is {0}".format(name)},
	{"question":"what is the weather today","answer":"The Weather today is {0}".format(random.choice(weather))},
	{"question":"how many states in india","answer":"The Number of States in India is {0}".format(states_cnt)},
	{"question":"what is the capital of india","answer":"The Capital of India is New Delhi"},
	{"question":"what is the capital of maharashtra","answer":"The Capital of India is Mumbai"},
	{"question":"this is which year","answer":"The Current Year is 2024"},
	{"question":"what is the smallest state in india","answer":"The Smallest State in India in Goa"},
	{"question":"what is the capital of india","answer":"The Capital of India is New Delhi"},
	{"question":"what is your work","answer":"I answer your Queries"},
	{"question":"who is the prime minister of india","answer":"The Prime Minsiter of India is Mr. Narendra Modi"},
	{"question":"what is the capital of india","answer":"The Capital of India is New Delhi"},
	{"question":"what is the current season","answer":"The Current Season in the Nation is {0}".format(random.choice(season))},
	{"question":"what is the capital of india","answer":"The Capital of India is New Delhi"}
]

ch=True
while ch:
	question=input("Enter your Message\t: ")
	if (question.lower()=="bye"):
		print("Answer\t: Bye!!")
		exit()
	flag=False
	for ans in resp:
		match=True
		for word in ans["question"].split():
			if word not in question.lower():
				match=False
		if match:
			print("Answer\t: ",ans["answer"])
			flag=True
			break
	
	if not flag:
		print("Answer\t: ","Sorry Cannot find an answer for it!!")
		ch=False
		
