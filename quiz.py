l=["kajal",3,89,"jha",67,9.5,"age",6.5,6]
for item in l:
    if (type(item)==int or type(item)==float) and item>6:  #here we can also use  if item.isnumeric()
        print(item)



