
# Vacuum Cleaner Problem

room = {'A': 'Dirty', 'B': 'Dirty'}
location = 'A'

while 'Dirty' in room.values():
    print("Vacuum is in Room", location)

    if room[location] == 'Dirty':
        print("Cleaning Room", location)
        room[location] = 'Clean'

    elif location == 'A':
        location = 'B'
    else:
        location = 'A'

print("All rooms are clean!")
print(room)
