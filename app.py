import datetime


class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    # class attribute
    location = 'England'

    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name  # todo why _name? not just name?
        self.birthyear = birthyear
        self.sex = sex

    def says(self, words):
        return f"{self._name} says {words}"

    @staticmethod
    def school_headmaster():
        return CastleKilmereMember('Redmond Dalodore', 1939, 'male')

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})"


class Pupil(CastleKilmereMember):
    """
    Create a Castle Kilmere Pupil
    """

    def __init__(self, name: str, birthyear: int, sex: str, house: str, start_year: int, pet: tuple = None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year

        if pet is not None:
            self.pet_name, self.pet_type = pet  # pet is a list so this assigns variables

        self._elms = {
            'Broomstick Flying': False,
            'Art': False,
            'Magical Theory': False,
            'Foreign Magical Systems': False,
            'Charms': False,
            'Defence Against Dark Magic': False,
            'Divination': False,
            'Herbology': False,
            'History of Magic': False,
            'Potions': False,
            'Transfiguration': False}
        # todo why _elms not elms ?

    @staticmethod
    def passed(grade):
        """
        Given a grade, determine if an exam was passed
        :param grade: the grade achieved by the pupil
        :return: True if grade was enough to pass or else False
        Returns False if grade not found
        """
        grades = {
            'O': True,
            'Ordinary': True,
            'P': True,
            'Passed': True,
            'A': True,
            'Acceptable': True,
            'P': False,
            'Poor': False,
            'H': False,
            'Horrible': False,
        }
        return grades.get(grade, False)

    @property
    def elms(self):
        return self._elms

    @elms.setter
    def elms(self, subject_and_grade):

        try:
            subject, grade = subject_and_grade
        except ValueError:
            raise ValueError("Pass an iterable with two items: subject and grade")

        passed = self.passed(grade)

        if passed:
            self._elms[subject] = True
        else:
            print('The exam was not passed so no ELM was awarded!')

    @elms.deleter
    def elms(self):
        print("Caution, you are deleting this students' ELM's! "
              "You should only do that if she/he dropped out of school without passing any exam!")
        del self._elms

    @classmethod
    def cleon(cls):
        return cls('Cleon Bery', 2008, 'male', 'House of Courage', 2018, ('Cotton', 'owl'))

    @classmethod
    def flynn(cls):
        return cls('Flynn Gibbs', 2008, 'male', 'House of Courage', 2018, ('Twiggles', 'owl'))

    @classmethod
    def cassidy(cls):
        return cls('Cassidy Ambergem', 2007, 'female', 'House of Courage', 2018, ('Ramses', 'cat'))

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self._name}, birthyear: {self.birthyear}, house: {self.house})")


class Professor(CastleKilmereMember):
    """
    Creates a Castle Kilmere professor
    """

    def __init__(self, name: str, birthyear: int, sex: str, subject: str, house=None):
        # todo why no function annotation for hourse=none?
        super().__init__(name, birthyear, sex)
        self.subject = subject
        if house is not None:
            self.house = house

    @classmethod
    def mirren(cls):
        return cls('Miranda Mirren', 1963, 'female', 'Transfiguration', 'House of Courage')

    @classmethod
    def blade(cls):
        return cls('Blade Bardock', 1988, 'male', 'Potions', 'House of Ambition')

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, subject: {self.subject})")


class Ghost(CastleKilmereMember):
    """
    Creates a Castle Kilmere ghost
    """

    def __init__(self, name: str, birthyear: int, sex: str, year_of_death: int, house=None):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death

        if house is not None:
            self.house = house

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, year of death: {self.year_of_death})")


if __name__ == "__main__":
    bromley = CastleKilmereMember('Bromley Huckabee', '1959', 'male')

    mirren = Professor.mirren()
    blade = Professor.blade()
    cleon = Pupil.cleon()
    flynn = Pupil.flynn()
    cassidy = Pupil.cassidy()


# cleon = Pupil(name='Cleon Bery',
#               birthyear=2008,
#               sex='male',
#               house='House of Courage',
#               start_year=2018,
#               pet=('Cotton', 'owl'))

print(bromley.says("Hello"))
print(cleon.pet_name, cleon.pet_type)

print(cleon.location)
print(cleon.birthyear, cleon.start_year)
print(CastleKilmereMember.location)
print(bromley)
print(cleon.age)

