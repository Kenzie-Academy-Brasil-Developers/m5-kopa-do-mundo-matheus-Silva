class NegativeTitlesError(Exception):
    def __init__(self, message: str):
        self.message = message


class InvalidYearCupError(Exception):
    def __init__(self, message: str):
        self.message = message


class ImpossibleTitlesError(Exception):
    def __init__(self, message: str):
        self.message = message


def data_processing(data: dict):
    if data["title"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    year_cup = int(data["first_cup"][0:4])

    if (year_cup - 1930) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")

    if year_cup > 2020:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
