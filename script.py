from graph_search import *
from vc_metro import *
from vc_landmarks import *
from landmark_choices import *

landmark_string = ''

def skyroute():
	greet()

def greet():
	print("Hi there and welcome to SkyRoute!")
	print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

def new_route(start_point=None, end_point=None):
	pass

def set_start_and_end(start_point, end_point):
	if start_point:
		change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
		if change_point == 'b':
			start_point, end_point = get_start(), get_end()
		elif change_point == 'o':
			start_point = get_start()
		elif change_point == 'd':
			end_point = get_end()
		else:
			print("Oops, that isn't 'o', 'd', or 'b'...")
			set_start_and_end(start_point, end_point)
	else:
		start_point, end_point = get_start(), get_end()

	return start_point, end_point

def get_start():
	start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
	if start_point_letter in landmark_choices:
		return landmark_choices[start_point_letter]
	else:
		print("Sorry, that's not a landmark we have data on. Let's try this again...")
		get_start()

def get_end():
	end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
	if end_point_letter in landmark_choices:
		return landmark_choices[end_point_letter]
	else:
		print("Sorry, that's not a landmark we have data on. Let's try this again...")
		get_end()

#skyroute()
print(set_start_and_end(None, None))
