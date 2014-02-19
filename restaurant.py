class Restaurant(object):
    """
    Represents a place that serves food.
    """
    def __init__(self, p_name, p_owner, p_chef):
        self.name = p_name
        self.owner = p_owner
        self.chef = p_chef

    def display(self):
        """Display the restaurant."""
        print self.name

    def is_yummy(self):
        """
        returns true if yummy, otherwise false
        """
        return False

    # define a method is_yummy
    # that returns a boolean value of yummyness
    # for now it should always return False

    def __str__(self):
        return (str(self.name) + ' (Owner: ' + str(self.owner)
                + ', Chef: ' + str(self.chef) + ')')


# class Restaurant(object):
#     """
#     Represents a place that serves food.
#     """
#     def __init__(self, name):
#         self.name = name
#
#     def display(self):
#         """Display the restaurant."""
#         print self.name
#
#     def is_yummy(self):
#         """
#         returns true if yummy, otherwise false
#         """
#         return False
