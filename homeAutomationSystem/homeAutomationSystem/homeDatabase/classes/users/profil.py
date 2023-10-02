class Profil:
    """
        class representing an profil
            Attributes:
                id
                first name
                lastname
                gender
                date of birth
            Property:
            method:
                serialize
    """

    def __init__(self, id, firstName, lastName, gender, dateOfBirth):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.dateOfBirth = dateOfBirth


    def serialize(self):
        data = []

        data['id'] = self.id
        data['firstName'] = self.firstName
        data['lastName'] = self.lastName
        data['gender'] = self.gender
        data['dateOfBirth'] = self.dateOfBirth

        return data