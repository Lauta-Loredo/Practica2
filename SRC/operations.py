def calculator_score(stat):
    """Calculando puntaje en base a sus stas

    Args:
        stat (dic): kills, assists, deaths

    Returns:
        Int: los puntos que obtuvo por sus stats
    """
    kills = stat['kills']
    assists = stat['assists']
    deaths = 1 if stat['deaths']  else 0
    return kills * 3 + assists - deaths * 1
        
def accumulate_rounds (final_rounds,player,stat):
    """Acumulo las rondas que se juegan
    Args:
        final_rounds (dic): donde se guardan las rondas
        player (key): Nombres de los jugadores
        stat (dic): kills, assists, deaths

    Returns:
        Dic: stats de los jugadores por rondas
    """
    final_rounds[player]['kills'] += stat['kills']
    final_rounds[player]['assists'] += stat['assists']
    final_rounds[player]['deaths'] += stat['deaths']
    final_rounds[player]['score'] += stat['score']
    return final_rounds


def mvp_player (player_list,data_round):
    """Averiguo quien fue el mejor por ronda

    Args:
        player (key): Nombres
        data_round (dic): kills, asists, deaths

    Returns:
        int: +1 al mejor jugador por ronda
    """
    max_score = 0
    best_player = None
    for player in data_round:
        score = data_round[player]['score']
        if score > max_score:
            max_score = score
            best_player = player
    return best_player

def rounds_played(final_rounds,best_player):
    """imprimo las rondas jugadas

    Args:
        final_rounds (dic): Rondas acumuladas
        best_player (string): El MVP por ronda
    """
    final_rounds = dict(sorted(final_rounds.items(), key = lambda item :  item[1]['score'], reverse=True))
    for stats in final_rounds:
        print(f' {stats}: Kills {final_rounds[stats]['kills']} / Assists {final_rounds[stats]['assists']} / Deaths {final_rounds[stats]['deaths']} / MVP {final_rounds[stats]['MVP']}/ Score {final_rounds[stats]['score']}')
    #print('--'*30)
    print()
    print(f' El MVP de la ronda fue : {best_player}')
    print('--'*30)