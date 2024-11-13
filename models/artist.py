import os

from exceptions.exceptions import ArtistNotFoundError
from .song import Song


def clear_screen():
	os.system("clear")


class Artist():
	def __init__(self, name, email, registration_date, listeners, songs):
		self.name = name
		self.email = email
		self.registration_date = registration_date
		self.listeners = listeners
		self.songs = [Song.from_data(song) for song in songs]


	def __str__(self):
		songs_titles = ("\n".join(f"{i}. {song.title}" for i, song in enumerate(self.songs, start=1)))
		return (f"\nName: {self.name}" 
				f"\nEmail: {self.email}"
				f"\nRegistration date: {self.registration_date}"
				f"\n\nListeners: {self.listeners:,d}"
				f"\n\nSongs: \n{songs_titles}")
				

	# Class method to create instances of 'Artist' from a data dictionary
	@classmethod
	def from_data(cls, data):
		return cls(
			name = data['name'],
			email = data['email'],
			registration_date = data['registration_date'],
			listeners = data['listeners'],
			songs = data['songs'])


	def show_artist_info(artists):
	# Shows artist information and allows to select one
		clear_screen()
		print("\nArtist selection")
		for i, artist in enumerate(artists, start=1):
				print(f"\n{i}. {artist.name}")

		while True:
			
			try:

				artist_selection = int(input("\nEnter artist number: "))

				if 1 <= artist_selection <= len(artists):
					selected_artist = artists[artist_selection - 1]

					while True:
						clear_screen()
						print(selected_artist)

						Song.show_song_info(selected_artist)

						back_option = int(input("\nDo you want to return to the menu (1) or select another song? (2): "))

						if back_option == 1:
							clear_screen()
							return

						elif back_option == 2:
							clear_screen()
							continue

						else:
							raise IndexError ("Invalid option. Please enter '1' to return or '2' to continue")

				else:
					raise ArtistNotFoundError ("The selected artist does not exist. Select a valid artist")

			except ValueError:
				print("Invalid input. Please enter a number.")

			except IndexError as error:
				print(error)
				
			except ArtistNotFoundError as error:
				print(error)