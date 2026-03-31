from random import randrange

# 3.5 Changing Guests List
primary_invitation_list = ['Tom', 'billy', 'James', 'oliver', 'Jimmy', 'nick']
secondary_invitation_list = ['Kevin', 'Bob', 'Stuart']
event_name = "Dinner"
event_time = "Today at 19.00"

def print_invitation_message(invitation_list = []):
  print(f"\nSending out invitations to {len(primary_invitation_list)} guest(s):")
  for invitee in invitation_list:
    print(f"\tHey {invitee}, come to the {event_name.lower()} {event_time.lower()}.")

primary_invitation_list = [invitee.capitalize() for invitee in primary_invitation_list]
primary_invitation_list.sort()

print_invitation_message(primary_invitation_list)
  
rejected_list = ['Billy', 'oliver', 'jimmy', 'Nick']
for index, rejected in enumerate(rejected_list):
  rejected = rejected.capitalize()
  print(f"\nUnfortunately, {rejected} has rejected the invitation.")
  primary_invitation_list.remove(rejected)
  if len(secondary_invitation_list) > 0:
    replacement = secondary_invitation_list.pop()
    print(f"Inviting {replacement} instead.")
    primary_invitation_list.append(replacement)
    primary_invitation_list.sort()
  else:
    print("The secondary invitation list is empty")
  print(f"Adjusted list of invitations: {primary_invitation_list}")
  
print_invitation_message(primary_invitation_list)


# 3.6 More Guests
# You just found a bigger dinner table, so now more space is available. Think of more quests to invite to dinner.
table_guests_limit = 12
print(f"\n\nA bigger table with {table_guests_limit} seats had been found. We can invite more people!")

new_guests_list = ['Sam','Haiden','Silver','Chris','Riley','Jackie','Willy','Ali','Skye','Cory']
table_seating_position = ['beginning', 'middle', 'ending']

while len(primary_invitation_list) < table_guests_limit:
  random_guest = new_guests_list.pop(randrange(len(new_guests_list)))
  random_position = table_seating_position[randrange(len(table_seating_position))]
  print(f"{random_guest.capitalize()} has been randomly selected to join the {event_name} at the {random_position} of the table!")
  if random_position == "beginning":
    print("Sitting the guest at the beggining of the table")
    primary_invitation_list.insert(0, random_guest)
  if random_position == "middle":
    table_middle = int(len(primary_invitation_list) / 2)
    print(f"Sitting the guest at the middle (position #{table_middle}) of the table")
    primary_invitation_list.insert(table_middle, random_guest)
  if random_position == "ending":
    print("Sitting the guest at the end of the table")
    primary_invitation_list.append(random_guest)
  
  print(f"Adjusted list of invitations: {primary_invitation_list}")
  
print_invitation_message(primary_invitation_list)

# 3.7 Shrinking Guests List
# You just found out that your new dinner table won't arrive in time for the dinner, and now you have space for only two guests.
print(f"\n\n\nUnfortunately we can invite only two people to the {event_name} :( \n")

while len(primary_invitation_list) > 2:
  rejected_guest = primary_invitation_list.pop()
  print(f"The invitation for {rejected_guest} has been rejected")

print("Send out the remaining invitation confirmations")
for guest in primary_invitation_list:
  print(f"Hey {guest}, you are still invited for the {event_name} at {event_time}") 

print("\nClean up the invitation list")
print(f"The invitation list before clean up: {primary_invitation_list}")
for index in range(len(primary_invitation_list)):
  del primary_invitation_list[index - 1]
  
print(f"The invitation list after clean up: {primary_invitation_list}")