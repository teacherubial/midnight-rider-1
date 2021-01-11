# main.py
# Midnight Rider
# A text-based adventure game.
# Gamespot gives it 9 out of 10.

import random
import sys
import textwrap
import time


INTRODUCTION = """
WELCOME TO MIDNIGHT RIDER

WE'VE STOLEN A CAR. WE NEED TO GET IT HOME.
THE CAR IS SPECIAL.

THAT'S WHY THE GOVERNMENT WANTS IT.

WE CAN'T LET THEM HAVE IT.

ONE GOAL: SURVIVAL... and THE CAR
REACH THE END BEFORE THE MAN GON GETCHU.

------
"""

WIN = """
YOU PRESSED THE BUTTON TO OPEN THE GATE.
THIS ISN'T THE FIRST TIME YOU'VE DONE THIS.
YOU CAN TIME IT PERFECTLY SO THAT YOU
SLIDE THE CAR IN AS THE GATES CLOSE.

YOU KNOW YOU DID THE RIGHT THING.
THE GOVERNMENT WOULD HAVE TORN THE CAR APART,
ANALYSING IT, TESTING IT, THEN DESTROYING IT.

THEY DON'T KNOW ITS SECRETS...
THAT IT HOLDS THE KEY TO DIFFERENT WORLDS.

AS YOU STEP OUT OF THE VEHICLE, FIDO RUNS
UP TO YOU.
"THANK YOU FOR SAVING ME," HE SAYS.

AS YOU TAKE A COUPLE OF STEPS AWAY FROM THE CAR,
IT MAKES A STRANGE NOISE.

BEFORE YOUR EYES, IT SHIFTS ITS SHAPE.
YOU'VE SEEN IT BEFORE, BUT ONLY ON TV.

"BUMBLEBEE...?"



----GAME OVER----
"""

LOSE_HUNGER = """

YOUR STOMACH IS EMPTY.
WHO KNEW THAT WHAT THE DOCTOR SAID WAS TRUE,
THAT HUMAN/ROBOT HYBRIDS WOULD NEED
TOFU TO SUSTAIN THEMSELVES.

YOUR ROBOT SYSTEMS START TO SHUT DOWN.
YOUR HUMAN EYES CLOSE.

THE LAST THING THAT YOU HEAR ARE SIRENS.
THEY GOTCHU. THEY GOT THE CAR.
WE FAILED...



----GAME OVER----
"""

LOSE_AGENTS = """

THE AGENTS HAVE CLOSED IN ON YOU.
THERE ARE AT LEAST 20 CARS SURROUNDING YOU.
THE LEAD CAR BUMPS YOUR PASSENGER SIDE.
YOU MANAGE TO CORRECT YOUR STEERING
TO KEEP YOU FROM CRASHING.

YOU DIDN'T SEE THE AGENT'S CAR BESIDE YOU.
THE DRIVER BUMPS YOUR CAR.
AND THAT'S IT.

YOU SPIN UNCONTROLLABLY.
THE CAR FLIPS OVER AT LEAST TWO TIMES.
OR MORE... YOU SEEM TO HAVE LOST COUNT.

SIRENS.

"ARE THEY ALIVE?" THEY SAY AS YOU HEAR
FOOTSTEPS GETTING CLOSER.
"DOESN'T MATTER, ALL WE WANTED WAS THE CAR.

YOU SEE A DOG SLOWLY STEP OUT OF THE
OVERTURNED CAR.

"YOU WILL NEVER STOP THE REVOLUTION,"
THE DOG SEEMS TO SAY TO THE OFFICERS.

IT WAS IN THE CAR THE WHOLE TIME.

YOU DRIFT OFF INTO UNCONSCIOUSNESS.


----GAME OVER----
"""

LOSE_FUEL = """

YOUR CAR SPUTTERS AND SEEMS TO LET OUT
A BIG SIGH. THERE'S NO MORE FUEL LEFT.

THE COPS SURROUND YOU AND THEY STEP
OUT OF THEIR CARS. THE LEAD AGENT
RIPS THE DOOR OPEN AND THROWS YOU OUT
OF THE CAR.

"WE FINALLY GOT IT."

YOU FAILED.


----GAME OVER----
"""

CHOICES = """
    ----
    A. Eat a piece of tofu.
    B. Continue ahead at a moderate speed.
    C. Speed ahead at full throttle.
    D. Stop to refuel. (NO FOOD AVAILABLE)
    E. Status Check
    Q. QUIT
    ----
"""


def type_text_output(string):
    for char in textwrap.dedent(string):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)


def main():
    # type_text_output(INTRODUCTION)

    # CONSTANTS
    MAX_FUEL_LEVEL = 50
    MAX_DISTANCE_TRAVELLED = 100
    MAX_TOFU = 3
    MAX_HUNGER = 50
    STARTING_AGENTS_DISTANCE = -20

    # Variables
    done = False

    kms_travelled = 0
    agents_distance = STARTING_AGENTS_DISTANCE
    turns = 0
    tofu = MAX_TOFU
    fuel = 1
    hunger = 0

    # MAIN LOOP
    while not done:
        # Random events
        # FIDO - refills your food (5%)
        if tofu < 3 and random.random() < 0.05:
            # refill tofu
            tofu = MAX_TOFU
            # player feedback
            print("******** You look at your tofu container.")
            print("******** It is filled magically.")
            print("******** \"You're welcome!'\", says a small voice.")
            print("******** The dog used its magic tofu cooking skills.")

        # END GAME
        # WIN - Travelled the Distance Req'd
        if kms_travelled > MAX_DISTANCE_TRAVELLED:
            time.sleep(2)
            type_text_output(WIN)
            break
        # LOSE - by hunger > MAX_HUNGER (50)
        elif hunger > MAX_HUNGER:
            time.sleep(2)
            type_text_output(LOSE_HUNGER)
            break
        # LOSE - agents reached you
        elif agents_distance >= 0:
            time.sleep(2)
            type_text_output(LOSE_AGENTS)
            break
        # LOSE - fuel runs out
        elif fuel <= 0:
            time.sleep(2)
            type_text_output(LOSE_FUEL)
            break

        # DISPLAY HUNGER
        if hunger > 40:
            print("******** Your stomach rumbles. You need to eat something soon.")
            time.sleep(1)
        elif hunger > 25:
            print("******** Your hunger is small but manageable.")
            time.sleep(1)

        # Present the user their choices
        print(CHOICES)

        user_choice = input("What do you want to do? ").lower().strip("!,.? ")

        if user_choice == "a":
            # EAT/HUNGER
            if tofu > 0:
                tofu -= 1
                hunger = 0
                print()
                print("-------- Mmmmm. Soybean goodness.")
                print("-------- Your hunger is sated.")
                print()
            else:
                print()
                print("-------- You have none left.")
                print()
        elif user_choice == "b":
            # SLOW
            players_distance_now = random.randrange(4, 12)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel
            fuel -= random.randrange(2, 7)

            # Player distance traveled
            kms_travelled += players_distance_now

            # Agents distance traveled
            agents_distance -= players_distance_now - agents_distance_now

            # Feedback to Player
            print()
            print(f"-------- You traveled {players_distance_now} kms.")
            print()
        elif user_choice == "c":
            # FAST
            players_distance_now = random.randrange(10, 16)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel
            fuel -= random.randrange(5, 11)

            # Player distance traveled
            kms_travelled += players_distance_now

            # Agents distance traveled
            agents_distance -= players_distance_now - agents_distance_now

            # Feedback to Player
            print()
            print("--------ZOOOOOOOM.")
            print(f"-------- You traveled {players_distance_now} kms.")
            print()
        elif user_choice == "d":
            # Refueling
            # Fill up the fuel tank
            fuel = MAX_FUEL_LEVEL

            # Consider the agents coming closer
            agents_distance += random.randrange(7, 15)

            # Give player feedback
            print()
            print("-------- You filled the fuel tank.")
            print("-------- The agents got closer...")
            print()
        elif user_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tkm travelled: {kms_travelled}")
            print(f"\tFuel remaining: {fuel} L")
            print(f"\tAgents are {abs(agents_distance)} kms behind.")
            print(f"\tYou have {tofu} tofu left.")
            print(f"\t--------\n")
        elif user_choice == "q":
            done = True
        else:
            print("\tPlease choose a valid choice.")

        # UPKEEP
        if user_choice in ["b", "c", "d"]:
            hunger += random.randrange(8, 18)
            turns += 1

        time.sleep(1.5)


    # Outro
    print()
    print("Thanks for playing. Play again soon!")
    print(f"You finished the game in {turns} turns.")


if __name__ == "__main__":
    main()
