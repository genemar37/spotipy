import os


def clear_screen():
	os.system("clear")


class User:
	def __init__(self, name, email, registration_date, password):
		self.name = name
		self.email = email
		self.registration_date = registration_date
		self.password = password
		self.current_song = None  # Current song playing
		self.is_playing = False  # Indicates if a song is currently playing
		self.liked_songs = []  # List of songs marked with 'like' by the user
		self.disliked_songs = []  # List of songs marked with 'like' by the user


	@property
	def password(self):
		return self._password
	

	@password.setter
	def password(self, value):
		if len(value) == 6:
			self._password = value
			
		else:
			raise ValueError("Password must have 6 characters")


	def __str__(self):
		return (f"\nName: {self.name}" 
				f"\nEmail: {self.email}"
				f"\nRegistration date: {self.registration_date}")


	def play(self, song):
		# Plays a song
		if self.is_playing:
			print("A song is already playing")
		else:
			self.current_song = song
			self.is_playing = True
			print(f"Now playing: '{self.current_song.title}'")


	def pause_song(self):
		# Pause current song
		if self.is_playing:
			print(f"Paused: '{self.current_song.title}'")
			self.is_playing = False
		

	def like_song(self, song):
		# Mark a song with 'like'
		if song not in self.liked_songs:
			self.liked_songs.append(song)

			if song in self.disliked_songs:
				self.disliked_songs.remove(song)

			print(f"\nYou liked '{song.title}' ♥")

		else:
			print(f"\nYou already liked '{song.title}'")


	def dislike_song(self, song):
		# Mark a song with 'dislike'
		if song in self.liked_songs:
			if song not in self.disliked_songs:
				self.disliked_songs.append(song)

				if song in self.liked_songs:
					self.liked_songs.remove(song)

				print(f"\nYou disliked '{song.title}' 👎")
		else:
			print(f"\nYou need to like the song '{song.title}' before you can dislike it")


	def show_user_info(user):
	# Shows user information
		print(user)