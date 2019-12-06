while True:
    x = input("字符串：")
    y = input("要找的字符：")
    r = x.find(y,0,len(x)) 
    if r>=0:
        print("have in")
        print(r)
    else:
       print("not ther")
    x = ""
    y = ""
    r = -1
