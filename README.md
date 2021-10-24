## Interactive Trajectory Retrieval and Visualization in Basketball Games

### Preprocess

1. cd to `preprocess`/

2. Follow the steps in `*.ipynb`

### Trajectory Similarity

1. cd to `similarity`/
2. change the path and choose the method to calculate trajectory similarity
3. Currently dtw, edit distance, freshet distance, LCSS, RNN, SAX(Symbolic
   Aggregate approXimation) are supported

### Visualization

1. cd to `visualization/`

2. change `data_path` of the `Event` object in `visualization/game/EventTurn.py` 

3. change `game_id` and ` event_id` in the main function of`visualization/game/EventTurn.py` to change the round to visualize

4. run `python visualization/game/EventTurn.py` 

5. In `visualization/game/EventTurn.py`, the code wrapped by the comments `"check terminal event"` will pause the gif and output event information when there is an important event taking place in the round. Comment the code if you want to get rid of this feature.

   

<img src="example.gif" width="500" alt="visualization example">

