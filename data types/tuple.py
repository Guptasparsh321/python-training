mytupple=(1,2,3)

#using len function 
print(len(mytupple))

#accessing the tupple items
print(mytupple[2])

#since tupples are immutable ,we have to convert it into list to make changes
y=list(mytupple)
y.append(4)
newtupple=tuple(y)
print(newtupple)

# similarly we can do more methods for changing the tupple by converting it into list.

#but we can add two tupples together
mytupple+=newtupple
print(mytupple)

#looping through the tupple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)