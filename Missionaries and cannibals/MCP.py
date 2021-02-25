# -*- coding: utf-8 -*-
"""
Created on Tue Feb 1 13:08:11 2021
@author: AshwinBalaji
"""
class Position():
	def __init__(self, leftCannibal, leftMissionary, boat, rightCannibal, rightMissionary):
		self.leftCannibal = leftCannibal
		self.leftMissionary = leftMissionary
		self.boat = boat
		self.rightCannibal = rightCannibal
		self.rightMissionary = rightMissionary
		self.parent = None

	def check_goal(self):
		if (self.leftCannibal == 0 and self.leftMissionary == 0):
			return True
		else:
			return False

	def check_valid(self):
		if (self.leftMissionary >= 0 and self.rightMissionary >= 0 and self.leftCannibal >= 0 and self.rightCannibal >= 0 and 
           (self.leftMissionary == 0 or self.leftMissionary >= self.leftCannibal) and 
           (self.rightMissionary == 0 or self.rightMissionary >= self.rightCannibal)):
			return True
		else:
			return False

	def __eq__(self, other):
		return (self.leftCannibal == other.leftCannibal and self.leftMissionary == other.leftMissionary and 
                self.boat == other.boat and self.rightCannibal == other.rightCannibal and 
                self.rightMissionary == other.rightMissionary)

	def __hash__(self):
		return hash((self.leftCannibal, self.leftMissionary, self.boat, self.rightCannibal, self.rightMissionary))

def movement(current_state):
	children = [];
	if (current_state.boat == 'L'):
		next_state = Position(current_state.leftCannibal, current_state.leftMissionary - 2, 'R',
                                  current_state.rightCannibal, current_state.rightMissionary + 2)
		## Two missionaries cross left to right.
		if (next_state.check_valid()):
			next_state.parent = current_state
			children.append(next_state)
		next_state = Position(current_state.leftCannibal - 2, current_state.leftMissionary, 'R',
                                  current_state.rightCannibal + 2, current_state.rightMissionary)
		## Two cannibals cross left to right.
		if (next_state.check_valid()):
			next_state.parent = current_state
			children.append(next_state)
		next_state = Position(current_state.leftCannibal - 1, current_state.leftMissionary - 1, 'R',
                                  current_state.rightCannibal + 1, current_state.rightMissionary + 1)
		## One missionary and one cannibal cross left to right.
		if (next_state.check_valid()):
			next_state.parent = current_state
			children.append(next_state)
		next_state = Position(current_state.leftCannibal, current_state.leftMissionary - 1, 'R',
                                  current_state.rightCannibal, current_state.rightMissionary + 1)
		## One missionary crosses left to right.
		if (next_state.check_valid()):
			next_state.parent = current_state
			children.append(next_state)
		next_state = Position(current_state.leftCannibal - 1, current_state.leftMissionary, 'R',
                                  current_state.rightCannibal + 1, current_state.rightMissionary)
		## One cannibal crosses left to right.
		if (next_state.check_valid()):
			next_state.parent = current_state
			children.append(next_state)
	else:
		next_state = Position(current_state.leftCannibal, current_state.leftMissionary + 2, 'L',
                                  current_state.rightCannibal, current_state.rightMissionary - 2)
		## Two missionaries cross right to left.
		if (next_state.check_valid()):
			next_state.parent = current_state
			children.append(next_state)
		next_state = Position(current_state.leftCannibal + 2, current_state.leftMissionary, 'L',
                                  current_state.rightCannibal - 2, current_state.rightMissionary)
		## Two cannibals cross right to left.
		if (next_state.check_valid()):
			next_state.parent = current_state
			children.append(next_state)
		next_state = Position(current_state.leftCannibal + 1, current_state.leftMissionary + 1, 'L',
                                  current_state.rightCannibal - 1, current_state.rightMissionary - 1)
		## One missionary and one cannibal cross right to left.
		if (next_state.check_valid()):
			next_state.parent = current_state
			children.append(next_state)
		next_state = Position(current_state.leftCannibal, current_state.leftMissionary + 1, 'L',
                                  current_state.rightCannibal, current_state.rightMissionary - 1)
		## One missionary crosses right to left.
		if (next_state.check_valid()):
			next_state.parent = current_state
			children.append(next_state)
		next_state = Position(current_state.leftCannibal + 1, current_state.leftMissionary, 'L',
                                  current_state.rightCannibal - 1, current_state.rightMissionary)
		## One cannibal crosses right to left.
		if (next_state.check_valid()):
			next_state.parent = current_state
			children.append(next_state)
	return children

def bfs():
	initial_state = Position(3,3,'L',0,0)
	if initial_state.check_goal():
		return initial_state
	current = list()
	visited = set()
	current.append(initial_state)
	while current:
		state = current.pop(0)
		if state.check_goal():
			return state
		visited.add(state)
		children = movement(state)
		for child in children:
			if (child not in visited) or (child not in current):
				current.append(child)
	return None

def display_result(result):
		path = []
		path.append(result)
		parent = result.parent
		while parent:
			path.append(parent)
			parent = parent.parent

		for t in range(len(path)):
			state = path[len(path) - t - 1]
			print ("| " + str(state.leftCannibal) + " Cannibal" + " , " + str(state.leftMissionary) \
                              + " Missionary" + " |" + "\t  " + state.boat + "\t" + "| " + str(state.rightCannibal) + " Cannibal" + " , " + \
                              str(state.rightMissionary) + " Missionary" + " |")

def main():
	result = bfs()
	print ("\n\t\tMissionaries and Cannibals Problem\n")
	print ("|  #Cannibal ,  #Missionary |\t Boat \t|  #Cannibal ,  #Missionary |\n")
	display_result(result)

if __name__ == "__main__":
    main()