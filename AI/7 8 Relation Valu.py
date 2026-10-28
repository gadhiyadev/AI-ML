# Facts
father_facts = [
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'd'),
    ('b', 'e'),
    ('c', 'f')
]

def brother():
    res = []
    for z1, x in father_facts:
        for z2, y in father_facts:
            if z1 == z2 and x != y:
                if (x, y) not in res:
                    res.append((x, y))
    return res

def cousin():
    res = []
    bros = brother()
    for z1, x in father_facts:
        for z2, y in father_facts:
            if z1 != z2 and (z1, z2) in bros:
                if (x, y) not in res:
                    res.append((x, y))
    return res

def grandson():
    res = []
    for y, z in father_facts:
        for z_val, x in father_facts:
            if z == z_val:
                if (x, y) not in res:
                    res.append((x, y))
    return res

def descendent():
    res = []
    for y, x in father_facts:
        if (x, y) not in res:
            res.append((x, y))

    added = True
    while added:
        added = False
        for z, x in father_facts:
            for z_val, y in list(res):
                if z == z_val and (x, y) not in res:
                    res.append((x, y))
                    added = True
    return res

def print_prolog_output(query, pairs):
    print(f"?- {query}.")
    for i, (x, y) in enumerate(pairs):
        terminator = " ;" if i < len(pairs) - 1 else "."
        print(f"X = {x}, Y = {y}{terminator}")
    print()

if __name__ == "__main__":
    print("\n--- Family Tree Relationship Queries ---\n")
    print("Facts (Father -> Child):", father_facts)
    print()

    print_prolog_output("brother(X, Y)", brother())
    print_prolog_output("cousin(X, Y)", cousin())
    print_prolog_output("grandson(X, Y)", grandson())
    print_prolog_output("descendent(X, Y)", descendent())
