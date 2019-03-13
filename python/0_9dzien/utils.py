# nazwy top 500 filmów według Filmweb
# tylko filmy o pojedynczych słowach w nazwach
# tylko filmy bez polskich znaków
# "the" usunięte
HASLA = [
    "Nietykalni",
    "Siedem",
    "Pianista",
    "Incepcja",
    "Django",
    "Gladiator",
    "Whiplash",
    "Prestige",
    "Kasyno",
]

def szubienica(poziom):
    """Rysuje szubienicę i wisielca. Obsługuje do 9 poziomów.

    poziom: liczba od 1 do 9."""
    ascii_arts = [
        # 0:
        """
              
                     
                       
                       
                      
                       
              
          _______
        """,

        # 1:
        """
              
             |       
             |         
             |         
             |        
             |         
             |
          ___|___
        """,

        # 2:
        """
              
             |/      
             |         
             |         
             |        
             |         
             |
          ___|___
        """,

        # 3:
        """
              _______
             |/      
             |         
             |         
             |        
             |         
             |
          ___|___
        """,

        # 4:
        """
              _______
             |/      |
             |         
             |         
             |        
             |         
             |
          ___|___
        """,

        # 5:
        """
              _______
             |/      |
             |      (_)
             |         
             |        
             |         
             |
          ___|___
        """,

        # 6:
        """
              _______
             |/      |
             |      (_)
             |       | 
             |       |
             |         
             |
          ___|___
        """,

        # 7:
        """
              _______
             |/      |
             |      (_)
             |      \|/
             |       |
             |         
             |
          ___|___
        """,

        # 8:
        """
              _______
             |/      |
             |      (_)
             |      \|/
             |       |
             |      / \\
             |
          ___|___
        """,
    ]
    return ascii_arts[poziom - 1]


def maskowanie(haslo, literki):
    haslo_list = list(haslo)
    literki_lower = [c.lower() for c in literki]
    for k in range(len(haslo_list)):
        if (haslo_list[k]).lower() not in literki_lower:
            haslo_list[k] = '_'

    return "".join(haslo_list)
