class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    # class attribute
    location = 'England'

    def __init__(self, name, birthyear, sex):
        self._name = name  #todo why _name? not just name?
        self.birthyear = birthyear
        self.sex = sex

    def says(self, words):
        return f"{self._name} says {words}"


class Pupil(CastleKilmereMember):
    """
    Create a Castle Kilmere Pupil
    """

    def __init__(self, name, birthyear, sex, house, start_year, pet=None):
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


bromley = CastleKilmereMember('Bromley Huckabee', '1959', 'male')
cleon = Pupil(name='Cleon Bery',
              birthyear=2008,
              sex='male',
              house='House of Courage',
              start_year=2018,
              pet=('Cotton', 'owl'))

print(bromley.says("Hello"))
print(cleon)
print(cleon.location)
print(cleon.birthyear, cleon.start_year)
print(CastleKilmereMember.location)

