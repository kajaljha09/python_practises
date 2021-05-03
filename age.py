age=int(input("Write ur age here"))
if age>7 and age <100:
   if age<18:
       print("u are not eligible to get the license")

   elif age==18:
       print("u will be physically examined")
   else:
       print("u are eligible to get the license ")
else:
    print("invalid")


