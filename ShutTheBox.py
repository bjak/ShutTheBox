#!usr/bin/python

#This is an attempt at making a shut the box game!

import sys
import pygame
import random

pygame.init()
size = width, height = 1200, 800

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0,255,0)
blue = (0, 0, 255)
turquoise = (0, 100, 155)

screen = pygame.display.set_mode(size)

pygame.display.set_caption('Shut the Box')

clock = pygame.time.Clock()

dice1 = pygame.image.load("dice1.png")
dice2 = pygame.image.load("dice2.png")
dice3 = pygame.image.load("dice3.png")
dice4 = pygame.image.load("dice4.png")
dice5 = pygame.image.load("dice5.png")
dice6 = pygame.image.load("dice6.png")
list = pygame.image.load("list.jpg")
red_x = pygame.image.load("red_x.png")

complete = False

print("This is a Dice Rolling Program")
print("Try and shut the box!")

roll_total = 0
dice_total = 0

def dice_roller():

        global number1, number2, total, number, roll_total, dice_total
        screen.blit(list, (400,100))
        pygame.display.flip()

        print("Press Enter to Roll when you are ready...")
        roll = input()
        number1 = random.randint(1,6)
        number2 = random.randint(1,6)
        number = number1 + number2

        print("Your first dice roll is...", number1)
        print("Your second dice roll is...", number2)

        if number1 == 1:

                screen.blit(dice1, (350,500))
                pygame.display.flip()                

        if number1 == 2:

                screen.blit(dice2, (350,500))
                pygame.display.flip()

        if number1 == 3:

                screen.blit(dice3, (350,500))
                pygame.display.flip()

        if number1 == 4:

                screen.blit(dice4, (350, 500))
                pygame.display.flip()

        if number1 == 5:

                screen.blit(dice5, (350,500))
                pygame.display.flip()

        if number1 == 6:

                screen.blit(dice6, (350,500))
                pygame.display.flip()

        if number2 == 1:

                screen.blit(dice1, (650,500))
                pygame.display.flip()

        if number2 == 2:

                screen.blit(dice2, (650,500))
                pygame.display.flip()

        if number2 == 3:

                screen.blit(dice3, (650,500))
                pygame.display.flip()

        if number2 == 4:

                screen.blit(dice4, (650,500))
                pygame.display.flip()

        if number2 == 5:

                screen.blit(dice5, (650,500))
                pygame.display.flip()

        if number2 == 6:

                screen.blit(dice6, (650,500))
                pygame.display.flip()

        roll_total += 1
        dice_total += number
        
def dice_score():

        global number, dice_total
        
        # number = number1 + number2

        # dice_total = [total]

        if number == 2:

                #total += number
                screen.blit(red_x, (530, 120))
                pygame.display.flip()

        if number == 3:

   #            total += number
                screen.blit(red_x, (640, 120))
                pygame.display.flip()

        if number == 4:

                screen.blit(red_x, (750, 120))
                pygame.display.flip()

        if number == 5:

 #               total += number
                screen.blit(red_x, (420, 220))
                pygame.display.flip()

        if number == 6:

 #              total += number
                screen.blit(red_x, (530, 220))
                pygame.display.flip()

        if number == 7:

 #            total += number
                screen.blit(red_x, (640, 220))
                pygame.display.flip()

        if number == 8:

 #               total += number
                screen.blit(red_x, (750, 220))
                pygame.display.flip()

        if number == 9:

 #               total += number
                screen.blit(red_x, (420, 330))
                pygame.display.flip()

        if number == 10:
                
 #               total += number
                screen.blit(red_x, (530, 330))
                pygame.display.flip()

        if number == 11:

 #               total += number
                screen.blit(red_x, (640, 330))
                pygame.display.flip()

        if number == 12:

 #               total += number
                screen.blit(red_x, (750, 330))
                pygame.display.flip()

        print("Your Total is...", dice_total)

#def shut_the_box():

 #       box = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#        for number in box:

#                box.remove(number)

#        print(dice_total)

def game():                      
    while not complete:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    complete = True

            screen.fill(white)
            dice_roller()
            dice_score()
     #       shut_the_box()
            print ("You have rolled", roll_total, "times!")
            print ("Roll again!")

            pygame.display.update()
            clock.tick(60)

    pygame.quit()
    quit()
