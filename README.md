# itp_final
Final project proposal:
Due date: 26 July 2018
Deliverable:
* Team members

Changxuan Wu 
Shuyang Deng

* Problem description
Elimination Jewels

It is a game where you try to eliminate the jewels by moving one of them so that more than three jewels of same color
are aligned in a line. 

* Core idea: 
The main challenge would be the building of the UI

* Pseudocode
```
1. Based on user input, generate a randomalized game board
2. When user click on first jewel, highlight it.
3. If the user did not click on jewels surrunding the first one, 
	show warning and restart from 2
4. Else try to replace the first jewel with the second, decide whether it is a succesful move 
5.	if it is
6.		replace them, 
7.		eliminate aligned jewel, 
8.		make the jewels above the eliminated ones fall 
9.		add new jewels to the top
10.		add some points for the move to player score
11.		return to step 2
12.	else
13.		report failure 
14.		return to step 2
15. There should be a timer and user should finished the task in time. 
```
* Expected input

Dimensions of the canvas. （Or difficulties ）

* Expected output

player's happy
