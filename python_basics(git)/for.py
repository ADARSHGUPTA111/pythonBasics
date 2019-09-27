ninjas=['ryan','adarsh','sumit','suraj',34]

for ninja in ninjas:
	print(ninja)

print("\n")

for ninja in ninjas[1:3]:
	print(ninja)
print("\n")

for ninja in ninjas:
	if ninja =='sumit':
		print(" You such a loser! ")
		break
	else:
		print("You guys are good")