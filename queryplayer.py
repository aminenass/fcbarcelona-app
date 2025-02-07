from collections import defaultdict
from models import Players


def get_players():

    players = Players.objects()

    grp_players = defaultdict(list)
    for player in players : 
        grp_players[player.position].append(player)
    return grp_players