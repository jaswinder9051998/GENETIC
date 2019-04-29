![Alt Text](https://media.giphy.com/media/65K6DdexY8CuvBRVWV/giphy.gif)

# GENETIC
This project involves the implementation of genetic algorithm in a user directed sandbox. 
## INTUITION
The basic intuition of the genetic algorithm is that every entity of the population (corresponding to a certain generation) has "genes".
The best of the entities in the population have a higher probability to pass down their genes to the next generation.
We use "fitness" as a criteria to decide how suited an entity is to pass down its genes.  
## ENVIRONMENT
### Element of population (balls)
The blue colored balls compose our population, which spawns at the top-center of the game-window display.
The balls have a fixed parameter "velocity" ( v ) with which the balls can jump on the canvas of pygame.
Although actual displacement of the ball depends upon the "angle" (0 to 360) of the ball.
* displacement
  * horizontal = v Cos(angle)
  * vertical = v Sin(angle)
Since our ball has a fixed number of "moves" to reach its goal, the ball has "moves" number of angles, implemented as a list.
This list forms the gene for out enitiy.
### Hurdles
* A fixed square shaped hurdle can be created using a single left click on the window
* User specified horizontal hurdle.
  * first left click defines the top-leftmost vertex
  * second left click defines the bottom-rightmost vertex




## OUTLINE
The list of *"angles of motion"* is our gene for entities. 
The goal for the population is to reach the black box (destination) in a certain number of moves without running into user generated obstacles. 
We use the square of inverse of the distance between the ball and the destination as our "fitness" function.
After fulfillment of moves of a certain population, a mating pool is created with elements of the population.
All the balls which ran into hurdles are not included in the mating pool.
The next population is created using the mating of entities in the mating pool.


## Libraries used
* pygame - for construction of enviroment
