import uuid

class Candidate:
    __id = None
    __first_name = ""
    __last_name = ""

    def __init__(self, first_name, last_name):
        self.__id = uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name


    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def id(self):
        return self.__id


    def serialize(self):
        return {
                "first_name": self.__first_name,
                "last_name": self.__last_name,
                "id": self.__id
                }
