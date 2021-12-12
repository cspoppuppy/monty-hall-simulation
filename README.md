# Monty Hall - Python Simulation

Monty Hall Problem: [link](https://en.wikipedia.org/wiki/Monty_Hall_problem)

*Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?*


### Simulation
---
- Using a list of 3 numbers represnts 2 goats and 1 car behind 3 doors
  - 0 represents goat, there are two 0s in the list
  - 1 represents car, there is one 1 in the list
  - 3 items are shuffled randomly for each run, represents the unknown behind the 3 doors

- Randomly choose a number between 0 - 2 (Python list index starts at 0) represents the door which the player has chosen

- Find the item in the list according to the chosen index from previous step. If the item is 1, the player wins a car with the original choice. Otherwise, the player wins a car by switching the choice


### Conclusion
---
Simulate the game multiple times
- probability of winning with the original choice = (number of games that the player wins with the original choice) / total number of games
- probability of winning by switching choice = 1 - probability of winning with the original choice


### How to run
---
- `pip install numpy`
- `python monty_hall.py`