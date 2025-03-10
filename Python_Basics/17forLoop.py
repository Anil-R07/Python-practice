
ipl = ["RCB", "MI", "SRH", "GT", "PBKS","CSK", "RR", "LSG"]

for teams in ipl:
    print(teams)

#range function ---> range(start, stop, step)
for i in range(1,11):
    print(i)

for i in range(2,21,2): 
    print(i)

#looping over string 
team = "ROYAL CHALLENGERS BENGALURU"
for letter in team:
    print(letter)

#nested loops (print tables)
for i in range (2,6):
    for j in range (1,11):
        print(f"{i} X {j} = {i*j}")
    print()

#break in loop 
for team in ipl:
    if team == "CSK":
        print(f"found fixing team {team}")
        break
    print(team)

#continue in loop 
for tata in ipl:
    if tata == "CSK":
        continue
    print(tata)

#using Enumerate 
for list, team in enumerate(ipl):
    print(f"team {list+1}: {team}")