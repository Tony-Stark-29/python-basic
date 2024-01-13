

#creating list by list() - list method

list1=list();
    
print("list1 - ",list1);

#creating list by [] - Square Brackets

list2=[];
print("list2 - ",list2);


#length of list by len() method
fruits = ['banana', 'orange', 'mango', 'lemon']
print("The list contains ",len(fruits)," fruits")
print()

#Accessing the elements in lists by indexing (list start with index 0)
print("Accessing the elements in lists by indexing")
print(fruits.index(fruits[0])," - ",fruits[0]);
print(fruits.index(fruits[1])," - ",fruits[1]);
print(fruits.index(fruits[2])," - ",fruits[2]);
print(fruits.index(fruits[3])," - ",fruits[3]);
print()
#Accessing the elements in lists by negative indexing (list negative index with -1)
print("Accessing the elements in lists by negative indexing")
print(fruits.index(fruits[-1])," - ",fruits[-1]);
print(fruits.index(fruits[-2])," - ",fruits[-2]);
print(fruits.index(fruits[-3])," - ",fruits[-3]);
print(fruits.index(fruits[-4])," - ",fruits[-4]);
print()

print("Unpacking list")
fruit_1,fruit_2,fruit_3,fruit_4=fruits;
print(fruit_1);
print(fruit_2);
print(fruit_3);
print(fruit_4);

fruit_1,fruit_2,*remaining=fruits;
print(fruit_1);
print(fruit_2);
print(remaining);
 