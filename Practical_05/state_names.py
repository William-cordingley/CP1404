"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state: ")
state = state.upper()
while state != "":
    if state in STATE_NAMES:
        print(" {0:<3} is {1:<20}".format(state, STATE_NAMES[state]))
    else:
        print("Invalid short state")
    state = input("Enter short state: ")


for state in STATE_NAMES:
    print(" {0:<3} is {1:<20}".format(state, STATE_NAMES[state]))