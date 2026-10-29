def participant_cost(attendee, food, transport):
    return attendee * (food + transport)
def event_cost(attendee, food, transport, venue):
    return participant_cost(attendee,food,transport) + venue
def budget_status(budget, total_cost):
    return "within budget" if total_cost <= budget else "over budget"
def event_summary(attendee, food, transport, venue, budget):
    total_cost = event_cost(attendee, food, transport, venue)
    status = budget_status(budget, total_cost)
    return f"Total cost for {attendee} attendees is {total_cost}. The event is {status}."
# A 
# normal case
people = participant_cost(10, 500, 200)
print(people)
#Zero attendee case 
people = participant_cost(0, 500, 200)
print(people)

# B 
# normal attendee cost plus venue
total = event_cost(10, 500, 200, 3000)
print(total)
# Zero attendee with a non-zero venue
total = event_cost(0, 500, 200, 3000)
print(total)
# C
# below budget case
status = budget_status(15000, 10000)
print(status)
#exactly equal to budget case
status = budget_status(10000, 10000)
print(status)
# over budget case
status = budget_status(5000, 10000)
print(status)
summary = event_summary(10, 500, 200, 3000, 10000)
print(summary)
total = event_cost(10, 800, 200, 5000)
status = budget_status(16000, total)
print(budget_summary("Study Day", total,status))