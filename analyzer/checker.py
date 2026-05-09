# ==========================================
#          PASSWORD CHECKER MODULE
# ==========================================

import re

from zxcvbn import zxcvbn

from analyzer.database import (
    password_used_before,
    save_password
)

from analyzer.utils import hash_password


class PasswordStrengthAnalyzer:

    # ==========================================
    #          ANALYZE PASSWORD
    # ==========================================

    def analyze(self, password):

        result = zxcvbn(password)

        score = result["score"]

        feedback = []

        # ==========================================
        #          CUSTOM SECURITY CHECKS
        # ==========================================

        # ---------- LENGTH CHECK ----------

        if len(password) < 8:

            feedback.append(
                "Use at least 8 characters"
            )

        elif len(password) < 12:

            feedback.append(
                "Use 12+ characters for stronger security"
            )

        # ---------- UPPERCASE CHECK ----------

        if not re.search(r"[A-Z]", password):

            feedback.append(
                "Add at least 1 uppercase letter"
            )

        # ---------- LOWERCASE CHECK ----------

        if not re.search(r"[a-z]", password):

            feedback.append(
                "Add at least 1 lowercase letter"
            )

        # ---------- NUMBER CHECK ----------

        if not re.search(r"\d", password):

            feedback.append(
                "Add at least 1 number"
            )

        # ---------- SPECIAL CHARACTER CHECK ----------

        if not re.search(
            r"[!@#$%^&*()_+=\-{}[\]:;<>,.?/]",
            password
        ):

            feedback.append(
                "Add at least 1 special character"
            )

        # ---------- COMMON PASSWORD CHECK ----------

        warning = result["feedback"]["warning"]

        if warning:

            feedback.append(warning)

        # ==========================================
        #       PASSWORD REUSE DETECTION
        # ==========================================

        hashed_password = hash_password(password)

        password_reused = False

        if password_used_before(hashed_password):

            password_reused = True

        # ==========================================
        #          SAVE PASSWORD HASH
        # ==========================================

        save_password(hashed_password)

        # ==========================================
        #            RETURN RESULT
        # ==========================================

        return {
            "strength": self.get_strength(score),
            "score": score,
            "feedback": list(set(feedback)),
            "password_reused": password_reused
        }

    # ==========================================
    #          GET STRENGTH LEVEL
    # ==========================================

    def get_strength(self, score):

        levels = {
            0: "Very Weak",
            1: "Weak",
            2: "Moderate",
            3: "Strong",
            4: "Very Strong"
        }

        return levels.get(score, "Unknown")