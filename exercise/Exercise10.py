import sys
sys.path.append("/home/lautaro/Documentos/Proyectos/Practica 2")
from src import Dic_rounds_10 as d
from src.operations_10 import *
final_rounds = {}
for num_round, data_round in enumerate(d.rounds, start=1):
    for player,stat in data_round.items():
        data_round[player]['score'] = calculator_score(stat)
        if player not in final_rounds:
            final_rounds[player]= {'kills': 0, 'assists':0, 'deaths':0, 'MVP':0, 'score': 0}
        final_rounds = accumulate_rounds(final_rounds, player, stat)
    final_rounds, best_player = mvp_player(data_round, final_rounds)
    rounds_played(final_rounds, best_player,num_round)