### Towers of hanoi

This is a naive implementation of Tower of Hanoi with variable number of pegs and variable number of plates.  It uses a 
simple breadth first, and stops once there is only one plate left on the initial peg and one peg free, since symmetry will clearly 
allow to find a full solution from this by simply renumbering the pegs, and then running the moves backwards. 

Finding the moves needed to solve the case of 4 pegs and 8 plates is done by 
````
import hanoi
result=hanoi.find_moves(4,8)
````
This will return a dictionary with number of pegs and plates, along with the list of moves.

To run through the moves with a simple graphical representation use
````
hanoi.run_moves(result)
````
which will give a graphical representation along the lines of 
````
        |                |                |                |        
        |                |                |                |        
        |                |                |                |        
        |                |                |                |        
        |                |                |                |        
        |                #                |                |        
        |               ###           #########            |        
        |              #####         ###########           |        
 ###############      #######       #############          |        
press key to see next move
>>> 
````