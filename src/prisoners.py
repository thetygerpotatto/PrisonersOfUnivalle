# prisoners.py

# Import necessary libraries
import os
import sys
from Simulator import Simulator
from prisonerClasses import *
# Define main program logic
def main():
    p1 = tit_for_that()
    p2 = steve()
    sim = Simulator(p1, p2, 200)
    sim.simulate()
    with open("data.csv", "w") as f:
        f.write("tit_for_that;steve\n")
        for i in sim.results:
            f.write(i[0].__str__()+";")
            f.write(i[1].__str__()+"\n")

# Entry point of the program
if __name__ == "__main__":
    # Call the main function
    main()

