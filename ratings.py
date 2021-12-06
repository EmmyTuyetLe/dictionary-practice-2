"""Restaurant rating lister."""
import sys




def add_ratings(ratings):
  answer = input("c>Would you like to add another restaurant?").lower()
  

  if answer == "no" or answer == "n":
    print("Ok! See you next time!")
  elif answer == "yes" or answer == "y":
    restaurant = input("What is the name of the restaurant?")
    rating = input("what score would you like to give it?")
    while int(rating) <0 or int(rating) >5:
      rating = input("Please input a number between 1 and 5")
    ratings[restaurant.capitalize()] = rating
    user_choices()


ratings = {}
def get_ratings(ratings):
  
  text_file = open(sys.argv[1])
  print(text_file)
  
  for line in text_file:
    splits = line.split(":")
    ratings[splits[0]] = splits[1].strip("\n")
  restaurants = sorted(ratings.items())
  for rank in restaurants:
    print(f"{rank[0]} is rated at {rank[1]}.")
  user_choices()
#  for restaurant, rating in dict_items



def user_choices():
  answer = input("What would you like to do?: See Ratings, Add Restaurant, Quit> ").lower()
  if answer == "see ratings":
    get_ratings(ratings)
  elif answer == "add restaurant":
    add_ratings(ratings)
  return

user_choices()