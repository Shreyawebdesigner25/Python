# a = {
#     "name": "shreya",
#     "Branch": "EC",
#     "college": "MITS",
#     "mobile": 8989700679
# }

# try:
#     print(a["name"])
#     print(a.get("gender"))
# except Exception as e:
#     print(e)
#     pass

# print(a["branch"])


def poweroftwo(n):
    if n == 0:
        return 1
    else:
        power = poweroftwo(n-1)
        return power * 2