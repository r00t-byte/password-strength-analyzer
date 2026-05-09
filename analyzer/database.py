# ==========================================
#          PASSWORD DATABASE MODULE
# ==========================================

DATABASE_FILE = "data/old_passwords.txt"


# ==========================================
#        CHECK PASSWORD REUSE
# ==========================================

def password_used_before(hashed_password):

    try:

        with open(DATABASE_FILE, "r") as file:

            passwords = file.read().splitlines()

            return hashed_password in passwords

    except FileNotFoundError:

        return False


# ==========================================
#          SAVE PASSWORD HASH
# ==========================================

def save_password(hashed_password):

    try:

        with open(DATABASE_FILE, "r") as file:

            passwords = file.read().splitlines()

    except FileNotFoundError:

        passwords = []

    # ==========================================
    #      PREVENT DUPLICATE PASSWORD HASH
    # ==========================================

    if hashed_password not in passwords:

        with open(DATABASE_FILE, "a") as file:

            file.write(hashed_password + "\n")