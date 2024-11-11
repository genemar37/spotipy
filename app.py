import os

from models.artist import Artist
from models.data import data
from models.free import Free
from models.playlist import Playlist
from models.premium import Premium
from models.song import Song
from models.user import User
from utils.dataframe import view_data_from_df


def clear_screen():
	os.system("clear")


def menu():
	print("\n♪ Welcome to Spotipy! ♪")
	print("\n1. Select artist")
	print("\n2. Create playlist")
	print("\n3. Play/Pause song")
	print("\n4. Like/Dislike song")
	print("\n5. View user information")
	print("\n6. View all songs information")
	print("\n7. Exit")


def main():

		try:

			user_free = Free("John Doe", "john.doe@example.com", "2024-09-11", "123456")

			user_premium = Premium("Jane Doe", "jane.doe@example.com", "2024-10-01", "abcdef")

			artists = [Artist.from_data(artist) for artist in data]

			all_songs = [song for artist in artists for song in artist.songs]


			while True:

				input("\nPress Enter to continue... ")
				clear_screen()
				menu()

				menu_selection = input("\nEnter selection by number: ")
				if menu_selection == "1":
					Artist.show_artist_info(artists)

				elif menu_selection == "2":
				
					user_type = input("\nSelect your account type (Free/Premium - F/P): ").lower()
					if user_type == "f":
						Playlist.create_playlist(all_songs, user_free)

					elif user_type == "p":
						Playlist.create_playlist(all_songs, user_premium)
						
					else:
						print("Invalid account type selected.")

				elif menu_selection == "3":
					Song.manage_playback(user_free, all_songs)
					
				elif menu_selection == "4":
					Song.like_dislike_song(user_premium, all_songs)

				elif menu_selection == "5":
					user_free.show_user_info()
					user_premium.show_user_info()
				
				elif menu_selection == "6":
					view_data_from_df()

				elif menu_selection == "7":
					print(f"\nThanks for using Spotipy! ♪")
					break

				else:
					print("Invalid option. Please select a valid option from the menu")

		except ValueError as error:
				print(error)

						
if __name__ == '__main__':
	main()