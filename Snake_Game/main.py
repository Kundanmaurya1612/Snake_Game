from snakeScreen import SnakeScreen
from snake import Snake
from turtle import Screen

screen = Screen()
snakeScreen = SnakeScreen()
tim = Snake()

screen.listen()
screen.onkey(tim.left,"a")
screen.onkey(tim.up,"w")
screen.onkey(tim.right,"d")
screen.onkey(tim.down,"s")


while True:
    snakeScreen.update()
    tim.move()
    
        
