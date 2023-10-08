age = input("Enter an age:")
agelist = []
people = 0
if int(age) < 0:
    print("Number of People Minimum age Maximum age\n 0")
else:
    agelist.append(int(age))
    people += 1

while True:
    age = input("Enter another age:")
    if int(age) < 0:
        break
    agelist.append(int(age))
    people += 1

minimumage = sorted(agelist)[0]
maximumage = sorted(agelist, reverse=True)[0]

print(f"Number of People Minimum age Maximum age")
print(f"{people}                 {minimumage}             {maximumage}")
