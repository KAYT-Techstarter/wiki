import hashlib

# Simulierte Datenbank
users = []


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def login(musername, mpassword):
    print(f"My Username: {musername} Password: {mpassword}")
    user = None
    hashed_password = hash_password(mpassword)
    for u in users:
        if u["username"] == musername and u["password"] == hashed_password:
            user = u

    return user


def signup(musername, mpassword):
    new_user_id = len(users) + 1
    hashed_password = hash_password(mpassword)
    users.append(
        {"id": new_user_id, "username": musername, "password": hashed_password}
    )


username = input("Wie lautet dein login Name: ")
password = input("Wie lautet dein password: ")

signup(username, password)
current_user = login(username, password)

print(f"My Logged in user with {username} and {password} is {current_user}")
# ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae --> test123
# d9b5f58f0b38198293971865a14074f59eba3e82595becbe86ae51f1d9f1f65e --> Test123
# ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae
# daef4953b9783365cad6615223720506cc46c5167cd16ab500fa597aa08ff964eb24fb19687f34d7665f778fcb6c5358fc0a5b81e1662cf90f73a2671c53f991 sha512

