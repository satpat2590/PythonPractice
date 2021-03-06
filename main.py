

#/ WORKING ON NAMING CONVENTIONS, TYPE CONVERSIONS, TYPE DECLARATIONS, PRINTING, PRINTING CONCATENATIONS ----------
def practice1():
  print("\n ****CONVENTIONS, DECLARATIONS, AND CONCATENATION\n")
  name = "Satyam"
  age = "20"
  int_age = int(age) 
  int_age = str(int_age) 

  # + Can easily turn an int to a str and vice versa 

  print("\nThe name is " + name + " and the age is " + int_age) 

  # + Can concatenate the same as in Java and JavaScript programming

#---------------------------------------------------------


#/ INPUT STATEMENTS 
  print("\n ****INPUT STATEMENTS\n")

  example_input = input("\nWhat is your favorite ice cream flavour?\n ") 

  print("\n" + name + "'s favorite ice cream flavour is " + example_input)

  type_input = int(input("\nWhat is your favorite number? ")) 

  print("\n" + name + "'s favorite number is " + 
                                    str(type_input)) 

  # + I have learned that python uses unusual (Different from C/Rust/Clojure) naming and stylistic conventions, however the configurations and work-arounds are tremenedously easier than C. 



#---------------------------------------------------------


#/ WORKING ON METHODS FOR STRINGS 

def practice2():
  print("\n ****METHODS IN STRINGS\n")

  big_name = "\nMr. Witherspoon has multiple dogs in his house and they are quite big dogs who like to bite and act dog-like"

  print(big_name.replace("dog", "cat"))

  print("\n" + str(big_name.find("dog")))

  print(big_name.replace("dog", "lemur").upper()) 

  # + I have learned that you can use two methods side by side in Python by dividing them based on the separation based on periods. 

  final_boolean = "dog" in big_name

  print("\n" + str(final_boolean)) #Should return true

  final_boolean = "cat" in big_name 

  print("\n" + str(final_boolean)) #Should return false

#---------------------------------------------------------


#/ ARITHMETIC OPERATORS IN MATH

def practice3():
  print("\n ****ARITHMETIC OPERATORS IN MATH\n")
  print(10 + 3)
  print(10 / 3) #Returns a number that is the exact floating point equivalent to the operand 
  print(10 // 3) #Returns a number that is rounded to the decimal place (3 in this case)

  print(10 * 3) #This is considered to be 10 x 3
  print(10 ** 3) #This is 10 to the 3rd power

  y = 15 // 3

  x = 20 // 3

  print(y > x and x > y) #The "and" operator prints out true if both are true and false if either one is false



#/ EXERCISE (WEIGHT CONVERSION PROGRAM) 

def exercise1(): 
  print("\n ****WEIGHT EXERCISE PROBLEM\n")
  weight = 180 #In pounds
  print("Weight: " + str(weight)) 
  user = input("(K)gs or (L)bs: ")

  if user.upper() == 'L': 
    print("Weight in pounds: " + str(weight))
  elif user.upper() == "K": 
    print("Weight in kilograms: " + str(weight / 2.205))


 
#/ LISTS OF MULTIPLE VARIABLE INPUTS AND FOR LOOP, WHILE LOOP 

def practice4():
  print("\n ****LISTS WITH MANY INPUT OPTIONS AND LOOPS\n")

  empire = ["California", "Japan", "Canada", "Hawaii"] 

  for advance in range(0, len(empire), 2): #For loop that only prints out every other country from "empire"
    print(empire[advance]) 

  empire.append("Beijing") #Appends another element to the list 

  empire.insert(6, 45)

  print(empire[5])

  #Attempt to use a for loop to print out needed elements together on the same line
  list = []
  j = 0 
  for j in range(0, len(empire)):
    if empire[j] != "Canada":
      list.append(empire[j])

  print(list) #Printed a list without Canada, removed the element by creating a new list with the new values 



#/ TUPLES OF MANY INPUTS, MAINLY INTEGERS HOWEVER

def practice5():
  print("\n ****TUPLES\n") 

  tuple = (5, 7, 3, 1, 9, 10, 13, "California")

  print(tuple[7]) 

  tuple = (5, 7, 3, 5, 9, 10, 13, 7, 8, 12, 45, 2, 7, 12, 34, 87, 98, 1, 2, 5, 2, 7, 5, 2, 7, 8, 9, 7, 2, 4, 6, 7, 8, 9, True, 1, 2, 5, 7, "China") 

  print("How many sevens are in there? " + str(tuple.count(7))) #Line of code that correctly gives the number of occurences of 7 in the tuple "tuple" 

  print("\nWhere in the tuple is the number '87' located?\n At the value of:  " + str(tuple.index(87))) #Line of code that correctly gives the index of the specified value in the tuple "tuple" 
        
  print("\nWhere in the tuple is the string 'China' located?\n At the value of: " + str(tuple.index("China"))) #Line of code that returns a string's index from the tuple "tuple" 

  print("\nWhere in the tuple is the boolean 'True' located?\n At the value of: " + str(tuple.index(True))) #Line of code that returns a boolean's index from the tuple "tuple". Note that '1' refers to True whilst '0' refers to False



#/ ENUMERATING A LIST, CREATING A TUPLE, AND UNPACKING A TUPLE

def practice6(): 
  print("\n ****ENUMERATING AND UNPACKING LISTS AND TUPLES\n")

  list = ['a', 'b', 'c', 'u', 'i', 'q', 'a', 'f', 'h', 'l', 'w', 7, 9, 23, 'a', 'r', 't', 'y', 'z', 'x', 'v', 'n', 67, 89] 
  print("--------------------------------------------------------------------------")
  print("| Question Asked", "\t\t\t| 2nd Question Asked", "\t| Tuple Struct\t\t |")

  for index, tups in enumerate(list): 
    print("|---------------------------|-----------------------|--------------------|")

    print("| What is going on today?", "\t| Where am I?", "\t\t\t| " + str(index) + "\t\t\t\t     |") 

    print("| I am feeling quite lonely |", "I am in Bethlehem", "\t| " + str(tups) + "\t\t\t\t     |")



#/ FUNCTIONS IN PYTHON 

def practice7():
  print("\n ****ALL ABOUT FUNCTIONS AND USES\n")

  def argumentExample(fingers, touchback): 
    print(f"Here is what I need from you: {fingers} and also, I need ${touchback[3]} for the gym membership")

  
  argumentExample(["Socks", "Pants", "Shirts", "Baby Food", "Tortillas", "Milk", "Eggs", "Asparagus", "Low Sugar Orange Juice"], [75, 65, 34, 21, 32, 67, 87])
















def review():

  # practice1()
  # practice2()
  # practice3()
  # practice4()
  # practice5()
  # practice6()
  # exercise1()
  practice7()


review()








