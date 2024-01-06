aws =[]
for aw_number in range(30):
    new_aw = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aws.append(new_aw)

for aw in aws[2:5]:
    if aw['color'] == 'green':
        aw['color'] = 'yellow'
        aw['points'] = 10
        aw['speed'] = 'medium'
    elif aw['color'] == 'yellow':
        aw['color'] = 'red'
        aw['points'] = 15
        aw['speed'] = 'fast'
for aw in aws:
    print(aw)

#6.4.2




