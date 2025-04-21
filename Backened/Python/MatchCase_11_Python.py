marks = int(input("ENter an integer : "))
match marks:
    case 90 :
         if marks >= 90:
          print("Very Good Marvelous Marks :)")
    case 80:
      if marks >=70 and marks <=80:
         print("Marks are Good :)")
    case 60:
      if marks >= 60 and marks <= 69:
         print("Marks are just Okay ! ")
    case 50:
      if marks <=59:
         print("So poor marks try Again!")
    case _:
      print("Invalid  input")