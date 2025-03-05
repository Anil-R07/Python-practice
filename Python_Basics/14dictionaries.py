tata_ipl = {
    "RCB" : "Kohli",
    "MI" : "Rohith",
    "SRH" : "Dhawan",
    "LSG" : "Rahul",
    "GT" : "Gill"
}

print(tata_ipl)
print(tata_ipl["RCB"])
print(tata_ipl.get("MI"))
print(tata_ipl.get("Kohli", "Not found"))

#Adding new element to dictionary
tata_ipl["KKR"] = "Shreyas"
print(tata_ipl)

#removing an element from dictionary
tata_ipl.pop("SRH")
print(tata_ipl)

del tata_ipl["KKR"]
print(tata_ipl)

#modifying an value of an elemet 
tata_ipl["MI"] = "Hardik"
print(tata_ipl)

#Dictionary methods
print(tata_ipl.keys())
print(tata_ipl.values())
print(tata_ipl.items())

new_team = {"PSK" : "Maxwell"}
tata_ipl.update(new_team)
print(tata_ipl)