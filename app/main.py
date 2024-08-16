class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_cars: list[Car]) -> float:
        income = 0
        for car in list_cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        part_1 = car.comfort_class * (self.clean_power - car.clean_mark)
        part_2 = self.average_rating / self.distance_from_city_center
        cost = part_1 * part_2
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, single_rate: int) -> None:
        part_1 = self.average_rating * self.count_of_ratings + single_rate
        part_2 = self.count_of_ratings + 1
        self.average_rating = round(part_1 / part_2, 1)
        self.count_of_ratings += 1
