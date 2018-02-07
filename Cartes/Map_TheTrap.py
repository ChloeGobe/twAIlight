from Map import Map


class MapTheTrap(Map):
    """

    Carte the Trap (donnée par le projet, par défaut dans la classe Carte
    __________________________________________________
    |    |    |    |    |    |    |    |    |    | 2H |
    __________________________________________________
    |    |    |    |    | 4W |    |    |    |    |    |
    __________________________________________________
    |    |    | 4H |    |    |    |    |    |    | 1H |
    __________________________________________________
    |    |    |    |    | 4V |    |    |    |    |    |
    __________________________________________________
    |    |    |    |    |    |    |    |    |    | 2H |
    __________________________________________________
    """


if __name__ == "__main__":
    carte = MapTheTrap()
    carte.print_map()