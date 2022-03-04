capacity = (12,8,5) 
x = capacity[0]
y = capacity[1]
z = capacity[2]
open = {}
ans = []
def states(state):
	jug1 = state[0]
	jug2 = state[1]
	jug3 = state[2]
	if(jug1==6 and jug2==6):
		ans.append(state)
		return True
	if((jug1,jug2,jug3) in open):
		return False
	open[(jug1,jug2,jug3)] = 1
	if(jug1>0):
		if(jug1+jug2<=y):
			if( states((0,jug1+jug2,jug3)) ):
				ans.append(state)
				return True
		else:
			if( states((jug1-(y-jug2), y, jug3)) ):
				ans.append(state)
				return True
	
		if(jug1+jug3<=z):
			if( states((0,jug2,jug1+jug3)) ):
				ans.append(state)
				return True
		else:
			if( states((jug1-(z-jug3), jug2, z)) ):
				ans.append(state)
				return True
	if(jug2>0):
		
		if(jug1+jug2<=x):
			if( states((jug1+jug2, 0,jug3)) ):
				ans.append(state)
				return True
		else:
			if( states((x, jug2-(x-jug1), jug3)) ):
				ans.append(state)
				return True
		if(jug2+jug3<=z):
			if( states((jug1, 0, jug2+jug3)) ):
				ans.append(state)
				return True
		else:
			if( states((jug1, jug2-(z-jug3), z)) ):
				ans.append(state)
				return True
	if(jug3>0):
		if(jug1+jug3<=x):
			if( states((jug1+jug3, jug2, 0)) ):
				ans.append(state)
				return True
		else:
			if( states((x, jug2, jug3-(x-jug1))) ):
				ans.append(state)
				return True
		
		if(jug2+jug3<=y):
			if( states((jug1, jug2+jug3, 0)) ):
				ans.append(state)
				return True
		else:
			if( states((jug1, y, jug3-(y-jug2))) ):
				ans.append(state)
				return True

	return False

initial_state = (12,0,0)
print("INITIAL STATE")
states(initial_state)
ans.reverse()
for i in ans:
	print(i)

