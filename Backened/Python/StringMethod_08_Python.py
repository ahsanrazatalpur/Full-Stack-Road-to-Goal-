# String are imutable (non-changable)
# every method in string will not change the real string it make its copies and than make change their
"""
# 1.     len(string)
name = "Ahsan Raza"
print(len(name)) # getting string length
#2.     string.upper()
name = "Ahsan Raza"
print(name.upper()) # to change string in uppercase

# 3.    string.lower()    
name = "Ahsan Raza"
print(name.lower()) # change string in lower case

#4 .   rstrip("symbol") to remove special symbol in the last of string only-----------------------------------------------
name = "Ahsan !!!!!"
print(name.rstrip('!'))

#5 .      .replace("old string or char" , "new string or char")
 name = "Ahsan Raza"
 new_name = name.replace("A" , "B") #-------------------------------------- number  ?
 print(new_name)  # here the char will be replaced

#6.   .split(" ")
name = "Ahsan Raza"
new_name = name.split("  ")
print(new_name) # both string seprate by space or giving string and make their list ny seprating comas --------------number?

#7 .     .capitalize()
name = "Ahsan Raza"
new_name =name.capitalize() # make tring first letter capital and all other lower case
print(new_name)

#Q .     center(number of spcace)
Intro  = "WElcome to python"
new_Intro = Intro.center(50) # center the string by giving 50 spaces

#9.     count()  count the string or char in string
name = 'Ahsan Raza'
new_name = name.count("a")
print(new_name)

#10 .   endswith(string)  tell us if string end with this strng if is the true else false
greet = "Hello, nice to meet you!"
new_greet = greet.endswith("!") 
new_greet = greet.endswith("!" ,0 ,10) # find last value by slicing  
    
# 11     .find() return index else  -1
intro = "welcome to my chanel"
new_intro = intro.find("my")  # first occurence of string
# 12       .index(string)  if find then return else throw exeption
name = "python"
new_name = name.index("t")  

#13         .isalnum()    # check if string is alpha numeric
seat = "seat123"
new_seat = seat.isalnum()
print(new_seat)  # if then true else false

# 14    isalpha  (alpha string if yes then true else false)
seat = "seatonetwothree"
new_seat = seat.isalpha()   #true
print(new_seat)  # if then true else false

#15         .islower()  characters are lower or not
language = 'java'
new_lan = language.lower()
print(new_lan)

 #16        .isprintable()  all character are printable expet line     \n \t etc 
str = "xyz"
print(str.printable()) #true

#17       isspace()   true only when we give white space
str = "    "
print(str.isspace()) # true
       
#18        .istitle()   true only if first letter of ech word is capital
intro = "My Name Is Ahsan" 
print(intro.istitle())  # True

#19    startwith()    check if string start with that string 
lang = "Python foe data science"
print(lang.startwith("Python")) # true

#20    swapcase()  change uppercase to lower lower to uppercase
str = "My name us ahsan raza"
print(str.swapcase())

#21       title()   make every first letter of string capital
str = "My name us ahsan raza"
print(str.title())

"""















