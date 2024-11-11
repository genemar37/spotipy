from .user import User


class Premium(User):
	def __init__(self, name, email, registration_date, password):
		super().__init__(name, email, registration_date, password)


	def show_user_info(self):
	# Shows user information
		print("\nUser Premium information: ")
		super().show_user_info()