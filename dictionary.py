# dictionaries are used to store data value in key:value pairs.
# dictionaries is a collection of key value pairs.

a = {
    "name" : "pninfosys gwalior",
    "college": "RJIT",
    # college" : "itm" , duplicates not allowed
     2 : [1,2,3,4,5,(2,3,4)],#list
     4 : ("ram","mohit"),
     "education" : {'ram' : 'MCA'}
    }

    print(a)
    #print(type(a["education"])) #key
    #print (a[2][2])
    #print(a["education"["ram"]])
    # we can update tuple in a dictionary ....
    print(a)
    a[4] = (40,50,60,47,89)
    print(type(a[4]))
    print(a)
    