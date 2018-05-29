

import pprint
odds = (1,3,5,7,9)
evens = (0,2,4,6,8)

mydict = {"name": "Marvin",
          "age": 43,
          "street": "100 Karian Court",
          "city": "Oxford",
          "state": "AL",
          "kids": [{"name": "Sara"}, {"name": "Sam"}]
          }

firstnumber = int(input("Enter first number: "))
secondnumber = int(input("Enter second number: "))



def listoddeven(start, stop):
  oddlist = []
  for x in range(start, stop):
    if str(x)[-1] in str(odds):
      oddlist.append(x)

  evenlist = []
  for x in range(start, stop):
    if str(x)[-1] in str(evens):
      evenlist.append(x)

  print(oddlist)
  print()
  print(evenlist)

  return oddlist


returned_object = listoddeven(firstnumber, secondnumber)

pprint.pprint(mydict)


print (returned_object)

print("Kids: ")
print("-" * 60)
for i in mydict["kids"]:
  print(i["name"])





