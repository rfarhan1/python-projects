class User:
    def __init__(self, user_id, user_name):
        print("new user being created.....")
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Rahman")
print(user_1.id)
print(user_1.username)
print(user_1.followers)

user_2 = User("002", "Farhana")
print(user_2.id)
print(user_2.username)
print(user_2.followers)

user_1.follow(user_2)

print(user_2.followers, user_2.following)
print(user_1.followers, user_1.following)
