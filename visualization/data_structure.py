import json
import os
import pprint

with open(os.path.join("data", "0021500226.json"), "r") as f:
    raw_data = json.load(f)

# for key_1, value_1 in raw_data.items():
#     print(key_1)

# first closure
# print(raw_data['gameid'])   # game id: 0021500226
# print(raw_data['gamedate']) # game date: 2015-11-25
# print(raw_data['events']) # event list and trajectories

for event in raw_data['events']:
    # for key_2, value_2 in event.items():
    #     print(key_2)
    
    # pprint.pprint(event['eventId']) # event id: '1'
    # pprint.pprint(event['visitor']) # visitor dictionary(same as home)
    # pprint.pprint(event['home'])    # home dictionary
    # print(event['moments'])         # a list of players' positions of each moment (25 frames per second)
    """
    {
        'abbreviation': 'LAC' # Team's abbreviation
        'name': 'Los Angeles Clippers' # Team's complete name
        'teamid': 1610612746 # Team's ID
        'players': [
            {
                'firstname': 'Lance' # player's first name
                'lastname': 'Stephenson' # player's last name
                'playerid': 202362 # player id
                'position': 'F-G' # player's position
                'jersey': '1' # player's jersey number
            }
            ...
        ] # list of player info
    }
    """

    # moment = event['moments'][0]
    # print(moment) # (list) position info at the moment
    """
    moment[0]: 1             # quarter
    moment[1]: 1448509261039 # timestamp (not meaningful)
    moment[2]: 718.05        # seconds left for the quarter (game clock)
    moment[3]: 22.12         # seconds left for the offensive possession (shot clock)
    moment[4]: None          #not sure what it is (always None)
    moment[5]: 11 positions of the ball and players (list)
        [
            [-1, -1, 71.30798, 18.17903, 5.52651]           # ball position, always at the first (-1, -1, x_coordinate, y_coordinate, radius)
            [1610612746, 200755, 52.00702, 38.5344, 0.0]    # player postion (team_id, player_id, x_coordinate, y_coordinate, -1) 
            ...
        ]
    """

    # avoid all of the events
    break



##############################################################
"""
final data structure:
{
    'gameid': '0021500226',
    'gamedate': '2015-11-25',
    'events': [
        {
            'eventId': '1',
            'visitor': ..., # same as 'home'
            'home': {
                        'abbreviation': 'LAC', 
                        'name': 'Los Angeles Clippers',
                        'teamid': 1610612746,
                        'players': [
                            {
                                'firstname': 'Lance',
                                'lastname': 'Stephenson',
                                'playerid': 202362,
                                'position': 'F-G',
                                'jersey': '1'
                            }
                            ...
                        ] # list of player info
                    }
            
            'moments': [
                            1,             
                            1448509261039, 
                            718.05,        
                            22.12,         
                            None,        
                            [
                                [-1, -1, 71.30798, 18.17903, 5.52651],           
                                [1610612746, 200755, 52.00702, 38.5344, 0.0]    
                                ...
                            ]
                        ]
            ]
        },
        ...
    ]
}
"""