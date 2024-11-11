from .user import User


class Free(User):
	def __init__(self, name, email, registration_date, password):
		super().__init__(name, email, registration_date, password)


	def show_user_info(self):
	# Shows user information
		print("\nUser Free information: ")
		super().show_user_info()