guests=['Hailey Riddle', 'Rick Riddle', 'Joe Riddle']#guest list
name=guests[0].title()
print(f"{name}, please join us for dinner.")#invite first guest
name=guests[1].title()
print(f"{name}, please join us for dinner.")#invite second guest
name=guests[2].title()
print(f"{name}, please join us for dinner.")#invite third guest
print("\nGreat news! We found a bigger dinner table, so more guests can come!")#Inform guests of bigger table
guests.insert(0,'Linda Riddle') #add new guest at beginning of list
guests.insert(2,'Jim Turner') #add new guest in middle of list
guests.append('Kima Riddle') #add new guest at end of list
guests.sort() #sort guest list alphabetically
print(guests) #print sorted guest list
print(f"{guests[0]}, please join us for dinner.")#invite first guest
print(f"{guests[1]}, please join us for dinner.")#invite second guest
print(f"{guests[2]}, please join us for dinner.")#invite third guest
print(f"{guests[3]}, please join us for dinner.")#invite fourth guest
print(f"{guests[4]}, please join us for dinner.")#invite fifth guest
print(f"{guests[5]}, please join us for dinner.")#invite sixth guest