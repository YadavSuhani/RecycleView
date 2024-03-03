size = input("Is your item larger than a credit card? ")

if (size == 'No'):
    print("You cannot recycle it, it is too small to be processed")
else:
    mater = input("What material is your trash? ")
    if (mater == "Glass" or mater == "Aluminum/Tin"):
        print("If it is clean, then it is good to recycle!")
    elif (mater == "Paper/Cardboard"):
        paper = input("Is your item a cardboard box, shredded paper, or neither? ")
        if (paper == "Cardboard"):
            print("If it is dry, clean, and broken down, then it is good to recycle!")
        elif (paper == "Shredded"):
            print("Place the shreds into a paper bag, then you are good to recycle it!")
        else:
            print("If it is dry and clean, then it is good to recycle!")
    elif (mater == "Plastic"):
        cat = input("Which category best fits your object? ")
        if (cat == "Bag, film, or styrofoam"):
            print("This item cannot be recycled")
        elif (cat == "Bottle, jug, or container"):
            cap = input("Is there a cap? ")
            if (cap == "No"):
                print("If it is clean, then it is good to recycle!")
            else:
                cap_mat = input("Does the material of the cap match the material of the container? ")
                if (cap_mat == "Yes"):
                    print("If it is clean, then it is good to recycle with the cap!")
                else:
                    print("Remove the cap first and throw it out, it cannot be recycled. If the container itself is clean, you are good to recycle it!")
    
print("\nFor more information, visit https://www.indy.gov/activity/recycling-101")