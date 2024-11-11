import os
import random
import time

from .free import Free
from .premium import Premium
from .song import Song


def clear_screen():
	os.system("clear")


class Playlist:
	def __init__(self, title, songs):
		self.title = title
		self.songs = songs


	def __str__(self):
		songs_titles = "\n".join(f"{i}. {song.title}" for i, song in enumerate(self.songs, start=1))
		return (f"\nTitle: {self.title}"
				f"\n\nSongs:\n{songs_titles}")


	def play(self, all_songs, user):
		# Play playlist songs
		if not self.songs:
			print("The playlist is empty")
			return

		if isinstance(user, Free):
			remaining_songs = [song for song in all_songs if song not in self.songs]
	
			random_songs = random.sample(remaining_songs, 3) 
		
			combined_songs = random_songs + self.songs

			random.shuffle(combined_songs)
		
			#clear_screen()
			print(f"\nPlaying playlist User Free: '{self.title}'")
			for song in combined_songs:
				time.sleep(1)
				print(f"\nNow playing: {song.title} - {song.duration}")


		elif isinstance(user, Premium):			
			#clear_screen()
			print(f"\nPlaying playlist User Premium: '{self.title}'")
			for song in self.songs:
				time.sleep(1)
				print(f"\nNow playing: {song.title} - {song.duration}")


	@classmethod
	def from_songs(cls, title, songs):
		# Class method to create instance of 'Playlist' with title and a list songs
		return cls(title, songs)

	
	def add_song(self, song):
		# Add a song to the playlist
		if song not in self.songs:
			self.songs.append(song)
			print(f"\nSong '{song.title}' added to the playlist")
		else:
			print(f"Song '{song.title}' is already in the playlist")


	def remove_song(self, song):
		if not self.songs:
			print("The playlist is empty. There are no songs to remove.")
			return
		
		# Remove a song from the playlist
		if song in self.songs:
			self.songs.remove(song)
			print(f"\nSong '{song.title}' remove from the playlist")
		else:
			print(f"Song '{song.title}' is not in the playlist")


	def create_playlist(all_songs, user):
	# Allows to create a new playlist
		clear_screen()
		print("\nCreate playlist:")
		
		
		try:
			playlist_title = input("\nEnter playlist title: ")
			
			playlist = Playlist.from_songs(playlist_title, [])

			while True:
				time.sleep(2)
				clear_screen()
				print("\nSelect an option:")
				print("\n1. Add song")
				print("\n2. Remove song")
				print("\n3. View playlist")
				print("\n4. Play playlist")
				print("\n5. Return to menu")

				playlist_selection = int(input("\nEnter option number: "))

				if playlist_selection == 1:
					time.sleep(1)
					clear_screen()
					Song.display_all_songs(all_songs)

					song_number = int(input("\nWrite song number to add: "))
					if 1 <= song_number <= len(all_songs):
						song = all_songs[song_number - 1]
						playlist.add_song(song)
						
					else:
						print("Invalid song number")


				elif playlist_selection == 2:
					if not playlist.songs:
						print("\nThe playlist is empty. You cannot remove songs")
						
					else:
						print(playlist)
						song_number = int(input("\nWrite song number to remove: "))
						if 1 <= song_number <= len(playlist.songs):
							song = playlist.songs[song_number - 1]
							playlist.remove_song(song)
							
						else:
							print("Invalid song number")

				elif playlist_selection == 3:
					if not playlist.songs:
						print("\nThe playlist is empty. You cannot view playlist")

					else:
						print(playlist)

				elif playlist_selection == 4:
					playlist.play(all_songs, user) # Calls method 'play' from Playlist
					
				
				elif playlist_selection == 5:
					return

		except ValueError:
			print("Invalid input. Please enter a valid option")