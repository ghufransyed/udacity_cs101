# Please edit the Restaurant class in the file restaurant.py

from restaurant import Restaurant

# These are test cases

mcdowells = Restaurant("McDowell's Hamgurger Emporium")
mcdowells.is_yummy()


#class Restaurant(Restaurant):
    #def is_yummy(self):
        #return True
# my solution made a new class based on the old class
# and redefined the is_yummy attribute in the new class
# the 'correct' solution reassigns a new method to the object
# chez_bananas.is_yummy
# as he says in the feedback, this is a really bad idea
# (I assume it was done as a teaching exercise)


def really_yummy():
    return True

chez_bananas = Restaurant("Chez Bananas Crib of Contentment")
chez_bananas.is_yummy = really_yummy
chez_bananas.is_yummy()


#test case:
print "Test is:", chez_bananas.is_yummy() == True
