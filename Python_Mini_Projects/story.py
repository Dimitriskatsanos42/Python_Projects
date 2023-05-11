import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago',' 22th Jul']

name = ['Giannis', 'Maria','Dimitra', 'Marios', 'Kostas']

residence = ['Barcelona','Athens', 'Germany', 'USA', 'England']

went = ['cinema', 'university','football', 'school', 'tennis']

happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']

print( random.choice(when) + ', ' + random.choice(name) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
