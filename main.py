# ==========================================
#        PASSWORD STRENGTH ANALYZER
# ==========================================

import argparse

from analyzer.checker import PasswordStrengthAnalyzer
from analyzer.generator import generate_smart_password


# ==========================================
#               HELP MENU
# ==========================================

parser = argparse.ArgumentParser(
    description="Advanced Password Strength Analyzer"
)

parser.add_argument(
    "-v",
    "--version",
    action="store_true",
    help="Show tool version"
)

args = parser.parse_args()

if args.version:

    print("\nPassword Strength Analyzer v2.0\n")

    exit()


# ==========================================
#               MAIN PROGRAM
# ==========================================

analyzer = PasswordStrengthAnalyzer()

print("\n==========================================")
print("   PASSWORD STRENGTH ANALYZER ")
print("==========================================")


while True:

    try:

        print("\nType 'exit' or press CTRL + C to quit")

        password = input("\nEnter Password : ")

    except KeyboardInterrupt:

        print("\n==========================================")
        print("          TOOL CLOSED")
        print("==========================================\n")

        break

    # ==========================================
    #               EXIT TOOL
    # ==========================================

    if password.lower() == "exit":

        print("\n==========================================")
        print("          TOOL CLOSED")
        print("==========================================\n")

        break

    # ==========================================
    #           ANALYZE PASSWORD
    # ==========================================

    result = analyzer.analyze(password)

    print("\n==========================================")
    print("              ANALYSIS RESULT")
    print("==========================================")

    print(f"\nStrength : {result['strength']}")
    print(f"Score    : {result['score']}/4")

    # ==========================================
    #        PASSWORD REUSE WARNING
    # ==========================================

    if result["password_reused"]:

        RED = "\033[91m"
        RESET = "\033[0m"

        print(f"\n{RED}Password already used before!{RESET}")

    # ==========================================
    #              SUGGESTIONS
    # ==========================================

    if result["feedback"]:

        print("\nSuggestions :")

        for suggestion in result["feedback"]:

            print(f"- {suggestion}")

    else:

        print("\nExcellent Password!")

    # ==========================================
    #      SMART PASSWORD SUGGESTION
    # ==========================================

    print("\n==========================================")
    print("      SMART PASSWORD SUGGESTION")
    print("==========================================")

    print(generate_smart_password(password))