from time import sleep

def Dosomething(name, surname):
  for i in name:
    for e in surname:
      print(f"{i}:{e}")


DoSomething(input("Enter Player Name :"), input("Enter Player Surname:"))
