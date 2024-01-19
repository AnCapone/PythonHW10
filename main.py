# Завдання 1: Створіть клас "Місто". Необхідно зберігати в полях класу: назву міста, назву регіону, назву країни,
# кількість жителів міста, поштовий індекс міста, телефонний код міста. Реалізуйте доступ до окремих полів (Інкапсуляція).
import re


class City:
    __city_name = "no name"
    __region_name = "no region"
    __state = "no state"
    __population = 0
    __post_code = "00000"
    __phone_code = "00000"

    def __init__(self, city_name, region_name, state, post_code, phone_code, population=10000):
        self.city_name = city_name
        self.region_name = region_name
        self.state = state
        self.post_code = post_code
        self.phone_code = phone_code
        self.population = population

    @property
    def city_name(self):
        return str.title(self.__city_name)

    @city_name.setter
    def city_name(self, city_name):
        if re.fullmatch(r'\b\w{2,}\b', city_name):
            self.__city_name = city_name

    @property
    def region_name(self):
        return str.title(self.__region_name)

    @region_name.setter
    def region_name(self, region_name):
        if len(region_name) > 2:
            self.__region_name = region_name

    @property
    def state(self):
        return str.title(self.__state)

    @state.setter
    def state(self, state):
        if len(state) > 2:
            self.__state = state

    @property
    def post_code(self):
        return self.__post_code

    @post_code.setter
    def post_code(self, post_code):
        if re.fullmatch(r'\b\d{5}\b', post_code):
            self.__post_code = post_code

    @property
    def phone_code(self):
        return self.__phone_code

    @phone_code.setter
    def phone_code(self, phone_code):
        if re.fullmatch(r'\b\d{3,5}\b', phone_code):
            self.__phone_code = phone_code

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        try:
            if int(population) > 0:
                self.__population = int(population)
        except ValueError as e:
            print("Entered value of population is incorrect. Will be used default value!")

    def show_info(self):
        print(
            f"City {self.city_name} in {self.region_name} region in {self.state}. {self.population} peoples live here. "
            f"Post code of city {self.post_code}. Phone code: {self.phone_code}")


# Завдання 2: Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни, назву континенту, кількість
# жителів країни, телефонний код країни, назву столиці, назву міст країни. Реалізуйте доступ до окремих полів.
class State:
    __name = "Atlantida"
    __continent = "Utopia island"
    __phone_code = "+000"
    __capital = "Shambala"
    __population = 100

    def __init__(self, name, continent, phone_code, capital, cities: list[City] = None):
        self.name = name
        self.continent = continent
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities
        self.__calculate_population()

    @property
    def name(self):
        return str.title(self.__name)

    @name.setter
    def name(self, name):
        if re.fullmatch(r'\b\w{2,}\b', name):
            self.__name = name

    @property
    def continent(self):
        return str.title(self.__continent)

    @continent.setter
    def continent(self, continent):
        if re.fullmatch(r'\b\w{2,}\b', continent):
            self.__continent = continent

    @property
    def phone_code(self):
        return self.__phone_code

    @phone_code.setter
    def phone_code(self, phone_code):
        if re.fullmatch(r'\+?\d{1,3}', phone_code):
            self.__phone_code = phone_code

    @property
    def capital(self):
        return str.title(self.__capital)

    @capital.setter
    def capital(self, capital):
        if re.fullmatch(r'\b\w{2,}\b', capital):
            self.__capital = capital

    def show_cities(self):
        print(f"{len(self.cities)} cities in {self.name}")
        for city in self.cities:
            city.show_info()

    def add_city(self, city: City):
        if isinstance(city, City):
            self.cities.append(city)
            self.__calculate_population()
            return

        raise Exception("fProvided value with incorrect type for city: {type(city)}")

    def __calculate_population(self):
        self.__population = 0
        for city in self.cities:
            self.__population += city.population

    @property
    def population(self):
        return self.__population

    def about_state(self):
        print(f"{self.name} is a country in {self.continent}. {self.capital} is a capital of {self.name}. Phone code: "
              f"{self.phone_code}")
        self.show_cities()
        print(f"Population of {self.name} {self.population}")
        print()

try:
    cities: list[City] = [City("kyiv", "kyiv", "Ukraine", "01000", "044", 2952301),
                          City("Kramatorsk", "Donetsk", "Ukraine", "84300", "06264", 147145),
                          City("Berdychiv", "Zhytomyr", "Ukraine", "13300", "04143", 73046)]
    ukraine = State("Ukraine", "Europe", "+38", "Kyiv", cities)
    ukraine.about_state()
    ukraine.add_city(City("Uman", "Cherkasy", "Ukraine", "20300", "04744", 81525))
    ukraine.about_state()
except Exception as error:
    print(error)