import os
import time

from .exceptions import ArtistNotFoundError, SongNotFoundError


def clear_screen():
	os.system("clear")


class Song:
	def __init__(self, title, streams, duration):
		self.title = title
		self.streams = streams
		self.duration = duration


	def __str__(self):
		return (f"\nTitle: {self.title}"
				f"\nStreams: {self.streams:,d}"
				f"\nDuration: {self.duration}")


	# Class method to create instances of 'Song' from a data dictionary
	@classmethod
	def from_data(cls, data):
		return cls(
			title = data['title'],
			streams = data['streams'],
			duration = data['duration'])


	def display_all_songs(all_songs):
	# Shows all available songs
		print("\nThese are all the available songs:\n")
		for i, song in enumerate(all_songs, start=1):
			print(f"{i}. {song.title}")


	def show_song_info(artist):
	# Shows selected song information 

		while True:
			try:
				song_selection = int(input("\nEnter song number for details: "))
				if 1 <= song_selection <= len(artist.songs):
					selected_song = artist.songs[song_selection - 1]
					print(selected_song)
					break

				else:
					raise SongNotFoundError("The selected song does not exist. Select a valid song")

			except ValueError:
				print("Invalid input. Please enter a number")

			except SongNotFoundError as error:
				print(error)


	def manage_playback(user, all_songs):
	# Allows the user manage song playback
		clear_screen()
		Song.display_all_songs(all_songs)

		while True:
			try:
				song_choice = int(input("\nEnter the number of your song choice to play it: "))
				if 1 <= song_choice <= len(all_songs):
					chosen_song = all_songs[song_choice - 1]

					user.play(chosen_song) # Calls method 'play' from User

					while True:
						action = input("\nEnter 'p' to pause the song or 'm' to return to the menu: ").lower()
						
						if action == 'p':
							user.pause_song()
							break

						elif action == 'm':
							return
					
						else:
							print("Invalid option. Please enter 'p' to pause the song or 'm' to return to the menu")
			
			except ValueError:
				print("Invalid input. Please enter a number")


	def like_dislike_song(user, all_songs):
	# Allows the user to mark a song with 'like' or 'dislike'
		clear_screen()
		Song.display_all_songs(all_songs)

		while True:
			try:
				song_choice = int(input("\nEnter the number of your song choice: "))
				if 1 <= song_choice <= len(all_songs):
					chosen_song = all_songs[song_choice - 1]

					print(f"\nYou select '{chosen_song.title}'")
					action = input("\nEnter 'l' to like, 'd' to dislike or 'm' to return to the menu: ").lower()

					if action == 'l':
						user.like_song(chosen_song)
						time.sleep(2)
						clear_screen()
						Song.display_all_songs(all_songs)	

					elif action == 'd':
						user.dislike_song(chosen_song)
						time.sleep(2)
						clear_screen()
						Song.display_all_songs(all_songs)

					elif action == 'm':
						return

					else:
						print("Invalid option. Please enter 'l' to like or 'd' to dislike, or 'm' to the menu")

				else:
					raise SongNotFoundError("The selected song does not exist. Select a valid song")
					
			except ValueError:
				print("Invalid input. Please enter a number.")

			except SongNotFoundError as error:
				print(error)