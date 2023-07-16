class Base:
    """ This class will be the “base” of all other classes in this project.
    It's goals is to manage all "id" attribute of future classes. """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
