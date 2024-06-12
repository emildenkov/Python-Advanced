def team_lineup(*players):
    countries_and_players = {}

    for player, country in players:
        if country not in countries_and_players:
            countries_and_players[country] = []

        countries_and_players[country].append(player)

    sorted_dictionary = dict(sorted(countries_and_players.items(), key=lambda x: (-len(x[1]), (x[0]))))

    result = ''
    for c, p in sorted_dictionary.items():
        result += f"{c}:\n"
        for n in p:
            result += f"  -{n}\n"

    return result.strip()


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
