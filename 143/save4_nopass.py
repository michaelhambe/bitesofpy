NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}

def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    name = str(name.lower())
    dicts = [group1, group2, group3]
    age = 0
    for d in dicts:
        if name in d.keys():
            age = d[name]
    if age != 0:
        return age
    else:
        return "Not found"