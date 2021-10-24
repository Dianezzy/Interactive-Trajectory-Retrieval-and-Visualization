import os
import json
import sys
import time

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle, Rectangle, Arc

sys.path.append('visualization')

from game.Constant import Constant
from game.Team import Team
from game.EventMoment import EventMoment


class Event():
    data_path = "C:\\WuYihong\\Data\\nba_movement_data\\data\\clean_data"
    
    def __init__(self, game_id, event_id, start=0, end=100000):
        self.game_id = str(game_id)
        self.event_id = str(event_id)
        self.game_data_path = None
        self.metadata, self.movement = self.extract_metadata_and_movement(self.game_id, \
                                                             self.event_id, start, end)
        self.id_to_player_path = "visualization\\data\\player_info\\player_id_to_info.json"                                                     
        self.id_to_player_data = {}
        with open(self.id_to_player_path, "r") as f:
            self.id_to_player_data = json.load(f)

        self.visitor = self.metadata['visitor']['abbreviation']
        self.home = self.metadata['home']['abbreviation']
        self.event_description = "{} {} {}".format(self.id_to_player_data[self.metadata['terminal_player']]['first_name'], \
                        self.id_to_player_data[self.metadata['terminal_player']]['last_name'], self.metadata['event_result'])
        self.player_list = self.metadata['visitor']['players'] + self.metadata['home']['players']
        self.player_to_jersey = {player['playerid']: player['jersey'] for player in self.player_list}

        self.moment = EventMoment(self.metadata, self.movement[0], self.player_to_jersey)

        self.last_time = None

    def plot_events(self):
        fig = plt.figure(figsize=(4, 4), dpi=250)
        clock, play_ground, player_table = self.initialize(fig)
    
        # clock info and player info
        clock_info, player_circles, ball_circle, jerseys = self.plot_clock_and_ground(clock, play_ground)
        
        # table info
        self.plot_player_table(player_table)

        # animation
        # Writer = animation.writers['ffmpeg']
        # writer = Writer(fps=24, codec="h264", bitrate=-1, metadata=dict(dpi=300, artist='Me'))
        ani = animation.FuncAnimation(
                        fig, self.update_moment,
                        fargs=(clock_info, player_circles, ball_circle, jerseys),
                        frames=len(self.movement), interval=Constant.INTERVAL)

        # ani.save('Green_2pt.gif', writer='pillow', fps=24)
        plt.show()
        

    def initialize(self, fig):
        # clock region
        clock = fig.add_axes([0, 0.90, 1, 0.10]) 
        clock.axis('off')
        clock.grid(False)

        # playground region
        play_ground = fig.add_axes([0, 0.25, 1, 0.6])
        play_ground.axis('off')
        play_ground.grid(False)
        play_ground.set_xlim([Constant.X_MIN - Constant.BORDER, Constant.X_MAX + Constant.BORDER])
        play_ground.set_ylim([Constant.Y_MIN - Constant.BORDER, Constant.Y_MAX + Constant.BORDER])

        # player table region
        player_table = fig.add_axes([0, 0, 1, 0.25])
        player_table.axis('off')
        player_table.grid(False)

        return clock, play_ground, player_table


    def plot_clock_and_ground(self, clock, play_ground):
        start_moment = self.moment

        # clock info
        clock_info = clock.annotate("", xy=[0.5, 0.1], \
                                        color='black', horizontalalignment='center', \
                                        verticalalignment='center')
        
        # player info
        court = plt.imread(os.path.join("visualization", "image", "full_court.png"))
        play_ground.imshow(court, zorder=0, extent=[Constant.X_MIN, Constant.X_MAX,
                                                    Constant.Y_MIN, Constant.Y_MAX])
        jerseys = [play_ground.annotate("", xy=[0,0], color='white', fontweight='semibold', \
                                            horizontalalignment='center', verticalalignment='center') \
                                            for _ in range(10)]
        player_circles = [plt.Circle((0,0), Constant.CIRCLE_SIZE, color=player.color)
                          for player in start_moment.players.values()]
        ball_circle = plt.Circle((0,0), Constant.CIRCLE_SIZE, color=start_moment.ball.color)

        for circle in player_circles:
            play_ground.add_patch(circle)
        play_ground.add_patch(ball_circle)


        return clock_info, player_circles, ball_circle, jerseys
    

    def plot_player_table(self, player_table):
        start_moment = self.moment
        players = self.build_team_player_info()

        column_labels = ('Pos', 'No.', self.visitor, 'Pos', 'No.', self.home)
        column_colors = tuple([Team.team_dict[self.visitor]]*3 + [Team.team_dict[self.home]]*3)
        column_widths = [Constant.NUMBER_WIDTH, Constant.NUMBER_WIDTH, Constant.NAME_WIDTH] * 2
        cell_colors = [column_colors] * 5

        table = player_table.table(cellText=players, colLabels=column_labels, colColours=column_colors, \
                                   colWidths=column_widths, loc='center', cellColours=cell_colors, \
                                   fontsize=Constant.FONTSIZE, cellLoc='center', )
        for i in range(6):
            for j in range(6):
                table[(i, j)].get_text().set_color('white')
    

    def update_moment(self, index, clock_info, player_circles, ball_circle, jerseys):
        moment = self.moment

        '''
            check terminal event
        '''
        print(moment.ball.radius)
        if moment.ball_status in ["shot", "turnover", "s.foul", "get pass", "give pass", "foul"]:
            event_player_name = "{} {}".format(self.id_to_player_data[str(moment.event_player)]['first_name'], \
                            self.id_to_player_data[str(moment.event_player)]['last_name'])
            print(moment.ball_status, event_player_name)
            os.system("pause")
        if moment.ball_status == "passing":
            print(moment.ball_status)
        '''
            check terminal event
        '''
        
        self.moment.undate_position(self.movement[index])
        
        # set clock info
        event_player_name = "{} {}".format(self.id_to_player_data[str(moment.event_player)]['first_name'], \
                            self.id_to_player_data[str(moment.event_player)]['last_name'])
        clock_text = "{}\n Quarter {:d}   Game: {:02d}:{:02d}.{:02d}  Shot: {:03.1f}\nBall Status: {}\nEvent Player: {}".format(
                      self.event_description,
                      moment.quarter,
                      int(moment.game_clock) // 60,
                      int(moment.game_clock) % 60,
                      round((float(moment.game_clock) - int(moment.game_clock)) * 100), 
                      moment.shot_clock, 
                      moment.ball_status,
                      event_player_name)   
        clock_info.set_text(clock_text)

        # set player info
        for i, circle in enumerate(player_circles):
            players = list(moment.players.values())
            circle.center = players[i].x, players[i].y
            jerseys[i].set_text(players[i].jersey)
            jerseys[i].set_position(circle.center)
        
        ball_circle.center = moment.ball.x, moment.ball.y
        ball_circle.radius = moment.ball.radius / Constant.BALL_COEF
        self.last_time = time.time()


    def build_team_player_info(self):
        home_team = []
        visitor_team = []

        for playerid in self.moment.players.keys():
            for player in self.metadata['home']['players']:
                if str(player['playerid']) == str(playerid):
                    home_team.append([player['position'], player['jersey'], \
                         " ".join((player['firstname'], player['lastname']))])
            
            for player in self.metadata['visitor']['players']:
                if str(player['playerid']) == str(playerid):
                    visitor_team.append([player['position'], player['jersey'], \
                         " ".join((player['firstname'], player['lastname']))])
        
        return [visitor_team[i] + home_team[i] for i in range(len(home_team))]


    def extract_metadata_and_movement(self, game_id, event_id, start, end):
        if self.game_data_path != None:
            game_data_path = self.game_data_path
        else:
            game_data_path = None
            all_directories = os.listdir(Event.data_path)
            for directory in all_directories:
                if game_id in directory:
                    game_data_path = directory
                    break
            
            if game_data_path == None:
                return None, None
            self.game_data_path = game_data_path

        event_data_path = os.path.join(Event.data_path, game_data_path, event_id)
        metadata = self.extract_metadata(event_data_path, event_id)
        movement = self.extract_movement(event_data_path, event_id, start, end)

        return metadata, movement


    def extract_metadata(self, event_data_path, event_id):

        f = open(os.path.join(event_data_path, "metadata.json".format(event_id)), "r")
        metadata = json.load(f)
        f.close()

        return metadata


    def extract_movement(self, event_data_path, event_id, start, end):

        f = open(os.path.join(event_data_path, "movement_refined_shot_clock.json".format(event_id)), "r")
        # f = open(os.path.join(event_data_path, "movement.json".format(event_id)), "r")
        movement = json.load(f)

        # clip movement sequence
        start = max(start, 0)
        end = min(end, len(movement))
        movement = movement[start:end]
        f.close()

        return movement
        


if __name__ == '__main__':
    start_time = time.time()
    event = Event("0021500330", "30", 400)

    event.plot_events()
    # print("time:", time.time() - start_time)
    
