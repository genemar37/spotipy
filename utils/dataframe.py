import pandas as pd

from data.data import data


def view_data_from_df():
	songs_data = []

	for artist in data:
		for song in artist["songs"]:
			
			song_info = {
			"Title": song["title"],
			"Artist": artist["name"],
			"Streams": song["streams"],
			"Duration": song["duration"]
			}

			songs_data.append(song_info)

	
	songs_df = pd.DataFrame(songs_data)
	# Each dictionary in "song_data" becomes a row, and the dictionary keys become the column names
	songs_df.index = range(1, len(songs_df) + 1)
	print(songs_df)