"""
29 April 2018.
"""

import helpers.findclosesthouse as fch
import matplotlib.pyplot as plt

def Output(plan):

    totalValue = 0

    print("Total houses placed:")
    print(len(plan.houses))

    # Total value of neighbourhood is calculated
    for house in plan.houses:

        totalValue += house.value(plan.houses)

    print("The total value of the neighbourhood:")
    print(totalValue)

    # Visualisation of the floor plan
    plt.figure()

    # These coordinates together plot the outline of the neighbourhood
    xlist = [0, plan.width, plan.width, 0, 0]
    ylist = [0, 0, plan.length, plan.length, 0]
    plt.plot(xlist, ylist)

    for pond in plan.ponds:

        # By plotting these lists, all corners will be connected by a line
        xlist = [pond.x1, pond.x2, pond.x2, pond.x1, pond.x1]
        ylist = [pond.y1, pond.y1, pond.y2, pond.y2, pond.y1]

        plt.plot(xlist, ylist)


    for house in plan.houses:

        # By plotting these lists, all corners will be connected by a line
        xlist = [house.x1, house.x2, house.x2, house.x1, house.x1]
        ylist = [house.y1, house.y1, house.y2, house.y2, house.y1]

        plt.plot(xlist, ylist)

    plt.show()
