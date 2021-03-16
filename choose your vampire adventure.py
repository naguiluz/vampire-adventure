answer = ""
while answer != "VICTORY":
answer = input("Would you like to play? (yes/no)")

if answer == "yes":

    answer = input("You find yourself at The Vampire's doorstep! A great door towers above you. It is time to decide. Will you enter? (yes/no)")

    if answer == "yes":

        answer = input("Bravery finds you even in the castle's shadow. You push the doors aside and stride in. A long hallway stretches into darkness to the left. A spiral staircase climbs ever higher to your right. Do you march left or right? (left/right)" )

        if answer == "left":

            answer = input("You walk forward into the growing darkness. Your footsteps echo as the light fades behind you. Before long you come face to face with The Vampire! Do you run or attack? (run/attack)")

            if answer == "attack":

                print("A fool's errand. You are quickly drained of every last drop of blood. DEATH...")

            elif answer == "run":

                print("A wise choice! You manage to slip from his grasp...for now.")
                answer = input("It's getting much colder. You see a fire burning in a room just down the hall, but you hear music coming from much deeper in the house. What do you investigate? (fire/music)")

                if answer == "fire":

                    print("It's much warmer in here. You sit in a cushioned chair to catch your breath and find it so relaxing you just might stay...until...DEATH...")

                elif answer == "music":

                    print("You walk deeper down the hall through countless chambers until you find her. An old woman playing the harp. She sounds so lovely.")
                    print("What would you like to hear, my dear? She asks in a quiet voice. We've got all the time in the world. You sit with her and listen until the end of your days...DEATH...")

        elif answer == "right":

            answer = input("You make your way up the creaky stairs step by step until you reach the next landing. A suit of armor stands at the top holding a great axe and a thick shield. Which do you take? (axe/shield)")

            if answer == "axe":

                print("The Vampire cackles. You turn to see him flying up the stairs towards you!")
                answer = input("Do you attack or run? (attack/run)")

                if answer == "attack":

                    print("You swing out, but your strength is no match for his! He bats the axe aside, and proceeds to drink until you wither away to dust...DEATH...")

                elif answer == "run":

                    print("Unsure of what direction to take he quickly catches you, and proceeds to drink until you wither away to dust...DEATH...")

            elif answer == "shield":

                print("The Vampire cackles. You turn to see him flying up the stairs towards you!")
                answer = input("Do you defend or run? (defend/run)")

                if answer == "defend":

                    print("He lunges for you, but you raise the shield and knock him back! He trips backwards down the stairs and falls. This old house has done him no favors as he falls and impales himself directly on the ornate decorations protruding from the banister.")
                    print("You've done it! The Vampire is dead! VICTORY!")
                    break

                if answer == "run":

                    print("Unsure of what direction to take he quickly catches you, and proceeds to drink until you wither away to dust...DEATH...")

    elif answer == "no":

        print("Not all have the heart of a lion. There is no cowardice in finding safety.")

    else:

        print("This is no time for indecision! You lose!")

else:
    print("Not everyone is ready for this adventure...")
