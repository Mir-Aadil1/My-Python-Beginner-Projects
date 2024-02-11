# String concatenation (aka how to put strings together)
# Suppose we want to create a string that says "subscribe to ___"


youtuber = 'Aadil Mir' # some string variable 


# a few ways to do this 

# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}") # this is the cleanest way 



adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so exited all the time because \  I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"


print(madlib)