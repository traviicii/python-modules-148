

n = {
    "Travis": {"name": 'Travis Peck', "age": 32, "email": "travisp@codingtemple.com"},
    "Cole" : {"name": "Cole Eubanks", "age": 24, "email": "cole@email.com"},
    "Areiahna": {'name': "Areiahna Cooks", "age": 22, "email": "ac@email.com" },
    "Dare": {"name": "Dare Fatade", "age": 37, "email": "dt@email.com"}
}

tup = ("Travis", {"name": 'Travis Peck', "age": 32, "email": "travisp@codingtemple.com"})

def new_key(x):
    return x[1]['age']

stuff = sorted(n.items(), key=lambda x: x[1]['age'])
# print(stuff)
for name, details in stuff:
    print(name, details)



# abc_nums = [('a',1), ('b',2), ('c', 3)]
# sorted_stuff = sorted(abc_nums)
# print(sorted_stuff)