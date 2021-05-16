

def funargs(normal, *argsrohan, **kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")



har = ["Kajal", "Rohan", "Skillf", "Uma",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan": "Monitor", "Kajal": "Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam": "Cook"}
funargs(normal, *har, **kw)
