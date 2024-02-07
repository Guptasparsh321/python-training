# thid id the way to access set values
# myset = {1, 2, 3}
# for x in myset:
#   print(x)

  #you cannot change the items in the set, but you can add new items in them.

  # add method
#   myset.add(4)
#   print(myset)

#update method which is used to add one list to another
#   firstset={1,2,3,4,5}
#   secondset={6,7,8,9,10}
#   firstset.update(secondset)
#   print(firstset)

#for using the update method,the other ds should just be iterable doesnt matter whether it is a ist,tuple or set.
  
#removing the items from set.there are other methods such as pop,clear,del also which performs different functions.
#   firstset.remove(2)
#   print(firstset)

#join sets 
  
#there are various methods like union(),intersectton() etc.
  
set1={1,2,3}
set2={2,3,4}
set3=set1.union(set2)
set4=set1.intersection(set2)
print(set3)
print(set4)

#there are various methods like union,intersection,add,update 