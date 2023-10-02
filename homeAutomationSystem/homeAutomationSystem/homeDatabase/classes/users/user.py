class User:
    '''
        class bringing all the information and functionality of an user

            attributes:
            	id: identifiant of the user
				profil: profil of the guest
                grade: grade of the user (user/admin)
                role: role of the user (inhabitant/guest)
                identifiant: identifiant of the user
                password: password of the user

            property:
                profilId: profil id of the user
                lastname: lastname of the user
                firstname: firstname of the user
                gender: gender of the user
                date of birth: date of birth of the user

            methods:
            	serialize (allows to transform the class in dict for json use)
    '''

    def __init__(self, id, profil, grade, role, identifiant, password, mail):
        """constructor of the class"""

        self.id = id
        self.profil = profil
        self.grade = grade
        self.role = role
        self.identifiant = identifiant
        self.password = password
        self.mail = mail
        
        
    @property
    def profilId(self):
        return self.profil.id

    @property
    def lastName(self):
        return self.profil.lastName

    @property
    def firstName(self):
        return self.profil.firstName

    @property
    def gender(self):
        return self.profil.gender

    @property
    def dateOfBirth(self):
        return self.profil.dateOfBirth


    def serialize(self):
        data = []

        data['id'] = self.id
        data['profil'] = self.profil.serialize()
        data["grade"] = self.grade
        data['role'] = self.role
        data['identifiant'] = self.identifiant
        data['password'] = self.password
        data['mail'] = self.mail

        return data