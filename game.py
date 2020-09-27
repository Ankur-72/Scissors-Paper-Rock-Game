import random
import tkinter

stats = []

def getWinner():
	if random.random() <= (1/3):
		throw = "rock"
	elif (1/3) < random.random() <= (2/3):
		throw = "scissors"
	else:
		throw = "paper"

	if (throw == "scissors" and call == "rock") or (throw == "paper" and call == "scissors") or (throw == "rock" and call == "paper"):
		stats.append("W")
		result = "You won!"

	elif throw == call:
		stats.append("D")
		result = "It's a draw!"

	else:
		stats.append("L")
		result = "You lost!"

	global output
	output.config(text = "Computer chose: " + throw + "\n" + result)


def passScissor():
	getWinner("scissors")

def passRock():
	getWinner("rock")

def passPaper():
	getWinner("paper")

root = tkinter.Tk()

scissors = tkinter.Button(root,text = "Scissors", bg= "aqua", padx = 50, pady = 50, command = passScissor, fg = "green", width= 20)
paper = tkinter.Button(root, text = "Paper",  bg = "red", padx = 50, pady = 50, command = passPaper, fg = "blue",  width= 20)
rock = tkinter.Button(root, text = "Rock", bg = "orange", padx = 50, pady = 50, command = passRock, fg = "black", width = 20)
decision = tkinter.Label(root, text = "What's your choice?", width = 20)

scissors.pack(side = "left")
paper.pack(side = "left")
rock.pack(side = "left")
decision.pack(side = "right")

root.mainloop()