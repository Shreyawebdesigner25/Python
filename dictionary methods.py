a = {
    "name": "pninfosys",
    "college": "RJIT",
    "mark": [1,2,3,4],
    "education": {'ram': 'MCA'},
    1 : 2
}

# print(a.keys())
# print(type(a.keys()))
# print(list(a.keys()))
# print(a.values())
# print(a.items())

# update dictionary
# print(a)

updatedict ={
    "branch":"it",
    "salary": 5000,
}
a.update(updatedict)##update the dictionary
print(a)


###get method

# print(a.get("abc"))