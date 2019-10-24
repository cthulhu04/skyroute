from graph_search import *
from vc_metro import *
from vc_landmarks import *
from landmark_choices import *

stations_under_constructions = ['Vancouver City Centre', 'Edmonds', 'Waterfront', 'Granville']

def skyroute():
	greet()
	show_landmarks()
	new_route()
	goodbye()

def greet():
	print("Hi there and welcome to SkyRoute!")
	print("We'll help you find the shortest route between any of Vancouver landmarks.")

def show_landmarks():
	see_landmarks = input("Would you like to see the list of landmarks? Enter y/n: ")
	if see_landmarks == 'y':
		for landmark in landmark_choices:
			print(landmark + ': ' + landmark_choices[landmark])

def new_route(start_point=None, end_point=None):
	start_point, end_point = set_start_and_end(start_point, end_point)
	shortest_route = get_route(start_point, end_point)
	if shortest_route:
		shortest_route_string = '\n'.join(shortest_route)
		print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
	else:
		print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))
	again = input("Would you like to see another route? Enter y/n: ")
	if again == 'y':
		show_landmarks()
		new_route(start_point, end_point)


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
		if start_point == end_point:
			print('Your origin and destination are the same! Please, pick another landmarks.')
			set_start_and_end(start_point, end_point)

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

def get_route(start_point, end_point):
	start_stations = vc_landmarks[start_point]
	end_stations = vc_landmarks[end_point]
	routes = []
	for start_station in start_stations:
		for end_station in end_stations:
			metro_system = update_metro_system(start_station, end_station)

			if not metro_system:
				return None 
			route = bfs(metro_system, start_station, end_station)
			if route:
				routes.append(route)

	return min(routes, key=len)

def update_metro_system(start_station, end_station):
	if stations_under_constructions:
		metro_system = get_active_stations()
		possible_route = dfs(metro_system, start_station, end_station)
		if not possible_route:
			return None
	else:
		return vc_metro

def get_active_stations():
	updated_metro = vc_metro
	for station in stations_under_constructions:
		for current_station, neighboring_stations in vc_metro.items():
			if current_station not in stations_under_constructions:
				updated_metro[current_station] -= set(stations_under_constructions)
			else:
				updated_metro[current_station] = set([])
	return updated_metro

def goodbye():
	print('Thanks for using SkyRoute!')

def add_or_remove_station():
	print('Would you like to add or remove station?', end=' ')
	choice = input('Please, enter "a" for adding and "r" for removing: ')
	if choice == 'a':
		add_station_under_construction()
	elif choice == 'r':
		remove_station_under_construction()
	else:
		print('The choice is invalid. Try again!')
		add_or_remove_station()

def add_station_under_construction():
	station = input('Please, enter the station which is under construction now: ')
	if is_valid_station(station):
		stations_under_constructions.append(station)
		again = input('Would you like to add another station? Enter y/n: ')
		if again == 'y':
			add_station_under_construction()
	else:
		print('It seems like this is not valid station. Please, try again!')
		add_station_under_construction()

def remove_station_under_construction():
	station = input('Please, enter the station which has been repared: ')
	if is_valid_station(station):
		stations_under_constructions.remove(station)
		again = input('Would you like to remove another station? Enter y/n: ')
		if again == 'y':
			remove_station_under_construction()
	else:
		print('It seems like this is not valid station. Please, try again!')
		remove_station_under_construction()


def is_valid_station(station):
	for landmark in vc_landmarks:
		for current_station in vc_landmarks[landmark]:
			if current_station == station:
				return True
	return False