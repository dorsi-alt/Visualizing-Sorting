import pygame as py
import random
py.init()

windowWidth = 500
windowHeight = 500

window = py.display.set_mode((windowWidth,windowHeight))

squareWidth = 1

sortedItems = []

for i in range(0,windowWidth):
    
    newElement = random.randint(0,windowHeight)
    sortedItems.append(newElement)


init = True

def displayCurrent(items):
    for i in range(len(sortedItems)):
            py.draw.rect(window, (0,0,0), (0 + i, 0, squareWidth, sortedItems[i]))




if __name__ == '__main__':
    while init:
    
        execute = False
    
        keys = py.key.get_pressed()
    
        for event in py.event.get():
    
            if event.type == py.QUIT:
    
                run = False
    
        if keys[py.K_SPACE]:
            execute = True
    
        if execute == False:
    
            
            window.fill((255, 255, 255))
    
            displayCurrent(sortedItems)
    
            py.display.update()
    
        else:
    
            for i in range(len(sortedItems) - 1):

                for j in range(len(sortedItems) - i - 1):
    
                    if sortedItems[j] > sortedItems[j + 1]:
    
                        t = sortedItems[j]
                        sortedItems[j] = sortedItems[j + 1]
                        sortedItems[j + 1] = t
                    window.fill((255, 255, 255))
    
                    
                    displayCurrent(sortedItems)
                    
                    py.display.update()
    py.quit()

