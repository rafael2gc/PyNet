aliens = []
for alien_number in range(30):
    #print(alien_number)
    new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'
for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number opf Aliens: {len(aliens)}")

