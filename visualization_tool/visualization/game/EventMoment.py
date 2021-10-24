import sys
sys.path.append("visualization")

from game.Constant import Constant
from game.Ball import Ball
from game.Player import Player
from game.Team import Team

class EventMoment():
    def __init__(self, metadata, moment, player_to_jersey):
        self.quarter = metadata['period']
        self.game_clock = moment['game_clock']
        self.shot_clock = moment['shot_clock']
        self.ball_status = moment['ball_status']
        self.event_player = moment['event_player']

        # Ball info
        self.ball = Ball(moment['ball_position'])

        # Player info
        self.players = {}
        for item in moment['player_position']:
            jersey = player_to_jersey[item[1]]
            color = Team.color_dict[item[0]][0]
            self.players[item[1]] = Player(item[1:], jersey, color)
        
        # Team info
        home_team = metadata['home']['teamid']
        visitor_team = metadata['visitor']['teamid']
        self.teams = (Team(visitor_team), Team(home_team))

    
    def undate_position(self, moment):
        # update clock
        self.game_clock = float(moment['game_clock'])
        self.shot_clock = 0 if moment['shot_clock'] == None else float(moment['shot_clock'])
        self.ball_status = moment['ball_status'] 
        self.event_player = moment['event_player'] if moment['event_player'] is not None else -1

        # update ball position
        self.ball.update_position(moment['ball_position'])

        # update players position
        for player in moment['player_position']:
            self.players[player[1]].update_position((player[2], player[3])) 

