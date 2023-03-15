from collections import OrderedDict, Counter


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        sorted_players = sorted(self.standings.items(), key=lambda x: x[1], reverse=True)
        rankings = []
        current_rank = 1
        for i, (player, score) in enumerate(sorted_players):
            if i == 0:
                rankings.append((player, current_rank))
            elif score == sorted_players[i - 1][1]:
                rankings.append((player, current_rank))
            else:
                current_rank = i + 1
                rankings.append((player, current_rank))
        return rankings

    def player_ranks(self, rank):
        sorted_players = sorted(self.standings.items(), key=lambda x: (-x[1]['score'], x[0]))

        return sorted_players[rank - 1][0] if 1 <= rank <= len(sorted_players) else None


