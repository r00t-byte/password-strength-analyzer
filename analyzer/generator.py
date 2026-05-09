# ==========================================
#        SMART PASSWORD GENERATOR
# ==========================================

import random
import re


# ==========================================
#       GENERATE SMART PASSWORD
# ==========================================

def generate_smart_password(base_password):

    password = base_password.strip()

    # ==========================================
    #      CAPITALIZE FIRST LETTER
    # ==========================================

    password = password.capitalize()

    # ==========================================
    #      SMART CHARACTER REPLACEMENTS
    # ==========================================

    replacements = {
        "a": "@",
        "e": "3",
        "i": "1",
        "o": "0",
        "s": "$"
    }

    improved = ""

    for index, char in enumerate(password):

        # Replace only some characters
        # to keep password readable

        if (
            char.lower() in replacements and
            random.choice([True, False])
        ):

            improved += replacements[char.lower()]

        else:
            improved += char

    # ==========================================
    #      ADD NUMBER IF MISSING
    # ==========================================

    if not re.search(r"\d", improved):

        improved += str(random.randint(10, 99))

    # ==========================================
    #      ADD SPECIAL CHARACTER
    # ==========================================

    if not re.search(r"[!@#$%^&*]", improved):

        improved += random.choice("!@#$%^&*")

    # ==========================================
    #      ADD SECURE RANDOM DIGITS
    # ==========================================

    improved += str(random.randint(1000, 999999))

    # ==========================================
    #      FINAL SYMBOL
    # ==========================================

    improved += random.choice("!@#$%^&*")

    return improved