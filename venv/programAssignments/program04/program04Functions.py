####################################################################
# Developer: Julian Cotto
# Date: 9/18/2023
# File Name: program04Functions.py
# Description: This file contains the functions for program04.py
####################################################################

def intro():
   print("This is Program04 - Julian Cotto")
   print("================================\n")

   print("Requirement 2\n")
   print("This program provides concert seat assignments.\n")

def musicPref(customerData):
   genre = str(input("Please enter your musical genre preference from the following list\n"
                     "1. Classical\n"
                     "2. Country\n"
                     "3. Jazz\n"
                     "4. Pop\n"
                     "5. Rock\n"
                     "6. Rap\n"))
   customerData["genre"] = genre.lower()
   return customerData["genre"]

def collectData(customerData):
   customerData["firstName"] = input(str("Enter your first name:\n"))
   customerData["lastName"] = input(str("Enter your last name:\n"))
   return customerData

def membershipLvl(customerData):
   membership = str(input("Please enter your musical genre preference from the following list\n"
                          "1. Composer\n"
                          "2. Conductor\n"
                          "3. Musician\n"))
   customerData["membership"] = membership.lower()
   return customerData

def seatAssign(customerData):
   seat = str(input("Please enter your seating preference from the following list\n"
                    "1. Orchestra\n"
                    "2. Main\n"
                    "3. Balcony\n"))
   customerData["seat"] = seat.lower()
   return customerData

def filterCustomerData(customerData):
   if customerData['membership'] == "composer" and customerData["seat"] == "orchestra":
      print("You qualify for these are exceptional seats!")
   elif customerData['membership'] == "composer" and customerData["seat"] == "main":
      print("The seats in the main section are good seats.")
   elif customerData['membership'] ==  "composer" and customerData["seat"] == "balcony":
      print("Interesting, let us know if you want closer seats.")
   elif customerData['membership'] == "conductor" and customerData["seat"] == "orchestra":
      print("Member level of Composer required if you want to sit in the orchestra section.")
   elif customerData['membership'] == "conductor" and customerData["seat"] == "main":
      print("The seats in the main section are good seats.")
   elif customerData['membership'] == "conductor" and customerData["seat"] == "balcony":
      print("Interesting, let us know if you want closer seats.")
   elif customerData['membership'] == "musician" and customerData["seat"] == "orchestra":
      print("Member level of Composer required if you want to sit in the orchestra section.")
   elif customerData['membership'] == "musician" and customerData["seat"] == "main":
      print("Member level of Composer or Conductor required if you want to sit in the main section.")
   else:
      print("Your balcony seats are confirmed.")

def customerSurvey(customerData):
   print("Please take a moment to complete our survey.")
   print("Use number keys 1 through 5 to respond to the following statements.")
   print("(1 = strongly disagree; 5 = strongly agree)")
   q1 = int(input("The concert was wonderful.\n"))
   q2 = int(input("The food was fantastic.\n"))
   q3 = int(input("The seats were superb.\n"))
   score = (q1 + q2 + q3)

   if customerData["membership"] == "composer" and (score < 12 or q1 < 4 or q2 < 4 or q3 < 4):
      print("Dear Composer, Your survey score of", score, "was lower than we would like. "
                                                          "Please give us another opportunity soon.")
   elif customerData["membership"] == "composer":
      print("Thank you for being a Composer member and for having a good time!")

   elif customerData["membership"] == "conductor" and (score < 11 or q1 < 3 or q2 < 3 or q3 < 3):
      print("Dear Conductor, Your survey score of", score, "was lower than we would like. "
                                                           "The next time you attend we will be nicer.")
   elif customerData["membership"] == "conductor":
      print("Thank you for being a Conductor member and for having a good time!")

   elif customerData["membership"] == "musician" and (score < 10 or q1 < 2 or q2 < 2 or q3 < 2):
      print("Dear Musician, Your survey score of", score, "was lower than we would like. "
                                                          "You will have more fun next time.")
   else:
      print("Thank you for being a Musician member and for having a good time!")

def experience():
   print("Program04 was more involved than the previous exercises.\n"
         "Still with good logic, it was easy enough to complete.\n"
         "I really do enjoy working in python and dealing with data in python structure.\n")

def outro():
    print("Thank you for running Program 4 - Julian Cotto")
    input("\nPress Enter to Exit...")