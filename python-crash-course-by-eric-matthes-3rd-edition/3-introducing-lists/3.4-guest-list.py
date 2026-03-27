from random import randrange

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
table_guests_limit = 12
print(f"\n\nA bigger table with {table_guests_limit} seats had been found. We can invite more people!")

new_guests_list = ['Sam','Haiden','Silver','Chris','Riley','Jackie','Willy','Ali','Skye','Cory']
table_seating_position = ['Beginning', 'Middle', 'Ending']

while len(primary_invitation_list) < table_guests_limit:
  random_guest = new_guests_list.pop(randrange(len(new_guests_list) - 1))
  print(f"{random_guest.capitalize()} has been randomly selected to join the {event_name}!")
  primary_invitation_list.append(random_guest)
  print(f"Adjusted list of invitations: {primary_invitation_list}")
  
print_invitation_message(primary_invitation_list)