"""
27 April 2018

Runs the algorithms to solve Amstelhaege.
"""

from randomalgorithm import RandomAlgorithm

def main():
    
    # Runs standard random placement algorithm.
    for i in range(10):
        RandomAlgorithm(60)
        
if __name__ == "__main__":
    main()