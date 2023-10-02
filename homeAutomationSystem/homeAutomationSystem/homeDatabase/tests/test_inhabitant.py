import sys

sys.path.append("..")

from homeDatabase.classes.users.inhabitant import *
from homeDatabase.classes.users.profil import *

class Test_inhabitant:

    inhabitant = Inhabitant(1, Profil( 1, "donovan","maurice", "m", "26/09/1994"), "user", "tetrew", "0000", "test@test.fr")


    def test_profilId_property(self):
        assert self.inhabitant.profilId == 1


    def test_lastName_property(self):
        assert self.inhabitant.lastName == "maurice"


    def test_firstName_property(self):
        assert self.inhabitant.firstName == "donovan"


    def test_gender_property(self):
        assert self.inhabitant.gender == "m"


    def test_dateOfBirth_property(self):
        assert self.inhabitant.dateOfBirth == "26/09/1994"