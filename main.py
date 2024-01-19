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
        return self.__city_name

    @city_name.setter
    def city_name(self, city_name):
        if re.fullmatch(r'\b\w{2,}\b', name):
            self.__city_name = city_name

    @property
    def region_name(self):
        return self.__region_name

    @region_name.setter
    def region_name(self, region_name):
        if len(region_name) > 2:
            self.__region_name = region_name

    @property
    def state(self):
        return self.__state

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
        if population > 0:
            self.__population = int(population)

    def show_info(self):
        print(f"City {self.city_name} in {self.region_name} region in {self.state}. {self.population} peoples live here."
              f"Post code of city {self.post_code}. Phone code: {self.phone_code}")

# class State:
#     __state_name = "no name"