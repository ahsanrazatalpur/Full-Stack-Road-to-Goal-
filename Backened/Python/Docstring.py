# DocString in Python
# DocString help to understand function (Description) , class def and its totally change to comments

def Square(number):
    '''Take a number , return the square of number ''' #This is docString (tell us the input expectation and what will be output)
    print(number ** 2)
Square(5)
print(Square.__doc__) # way to print DocString (it doesnot ignore like comments)

# DocString is a special type of  String above the function Defination 
# changing the commnets can't effect the program but changing the DocString may effect the program
# DocString just write below the function declaration if we write or print another line there docString will be None

