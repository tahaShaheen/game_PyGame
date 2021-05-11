import os
import pygame
from pygame import image
import random

pygame.init()

run = True

x = 50
y = 425
characterWidth = 24  # width of sprites in pixels
characterHeight = 32  # height of sprites in pixels
vel = 5

screenWidth = characterWidth * 15
screenHeight = characterHeight * 15

left, right, up, down, attack = False, False, False, False, False
fight = False

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("First game")

clock = pygame.time.Clock()

walkCount = 0

columnsOfGerms = 5 # keep this an odd numbers
rowsOfGerms = 5 # keep this an odd number

totalGerms = columnsOfGerms * rowsOfGerms - 1 # because Samurai takes one space

samuraiSpriteCount = 4
germSpriteCount = 3

samuraiWalkUp = [
    image.load(os.path.join('sprites/samurai', 'tile000.png')),
    image.load(os.path.join('sprites/samurai', 'tile001.png')),
    image.load(os.path.join('sprites/samurai', 'tile002.png')),
    image.load(os.path.join('sprites/samurai', 'tile001.png'))
]

samuraiWalkDown = [
    image.load(os.path.join('sprites/samurai', 'tile024.png')),
    image.load(os.path.join('sprites/samurai', 'tile025.png')),
    image.load(os.path.join('sprites/samurai', 'tile026.png')),
    image.load(os.path.join('sprites/samurai', 'tile025.png'))
]

samuraiWalkRight = [
    image.load(os.path.join('sprites/samurai', 'tile012.png')),
    image.load(os.path.join('sprites/samurai', 'tile013.png')),
    image.load(os.path.join('sprites/samurai', 'tile014.png')),
    image.load(os.path.join('sprites/samurai', 'tile013.png'))
]

samuraiWalkLeft = [
    image.load(os.path.join('sprites/samurai', 'tile036.png')),
    image.load(os.path.join('sprites/samurai', 'tile037.png')),
    image.load(os.path.join('sprites/samurai', 'tile038.png')),
    image.load(os.path.join('sprites/samurai', 'tile037.png'))
]

samuraiAttackUp = [
    image.load(os.path.join('sprites/samurai', 'tile075.png')),
    image.load(os.path.join('sprites/samurai', 'tile087.png')),
    image.load(os.path.join('sprites/samurai', 'tile051.png')),
    image.load(os.path.join('sprites/samurai', 'tile063.png'))
]

samuraiAttackDown = [
    image.load(os.path.join('sprites/samurai', 'tile021.png')),
    image.load(os.path.join('sprites/samurai', 'tile027.png')),
    image.load(os.path.join('sprites/samurai', 'tile048.png')),
    image.load(os.path.join('sprites/samurai', 'tile072.png'))
]

samuraiAttackLeft = [
    image.load(os.path.join('sprites/samurai', 'tile040.png')),
    image.load(os.path.join('sprites/samurai', 'tile054.png')),
    image.load(os.path.join('sprites/samurai', 'tile078.png')),
    image.load(os.path.join('sprites/samurai', 'tile040.png'))
]

samuraiAttackRight = [
    image.load(os.path.join('sprites/samurai', 'tile015.png')),
    image.load(os.path.join('sprites/samurai', 'tile057.png')),
    image.load(os.path.join('sprites/samurai', 'tile069.png')),
    image.load(os.path.join('sprites/samurai', 'tile083.png'))
]

samuraiWaiting = [
    image.load(os.path.join('sprites/samurai', 'tile030.png')),
    image.load(os.path.join('sprites/samurai', 'tile031.png')),
    image.load(os.path.join('sprites/samurai', 'tile032.png')),
    image.load(os.path.join('sprites/samurai', 'tile031.png'))
]

germ1RightFacing = [
    image.load(os.path.join('sprites/germs', 'tile009.png')),
    image.load(os.path.join('sprites/germs', 'tile010.png')),
    image.load(os.path.join('sprites/germs', 'tile011.png'))
]

germ2RightFacing = [
    image.load(os.path.join('sprites/germs', 'tile021.png')),
    image.load(os.path.join('sprites/germs', 'tile022.png')),
    image.load(os.path.join('sprites/germs', 'tile023.png'))
]

germ3RightFacing = [
    image.load(os.path.join('sprites/germs', 'tile060.png')),
    image.load(os.path.join('sprites/germs', 'tile061.png')),
    image.load(os.path.join('sprites/germs', 'tile062.png'))
]

germ4RightFacing = [
    image.load(os.path.join('sprites/germs', 'tile066.png')),
    image.load(os.path.join('sprites/germs', 'tile067.png')),
    image.load(os.path.join('sprites/germs', 'tile068.png'))
]

germ5RightFacing = [
    image.load(os.path.join('sprites/germs', 'tile057.png')),
    image.load(os.path.join('sprites/germs', 'tile058.png')),
    image.load(os.path.join('sprites/germs', 'tile059.png'))
]

germ1LeftFacing = [
    image.load(os.path.join('sprites/germs', 'tile033.png')),
    image.load(os.path.join('sprites/germs', 'tile034.png')),
    image.load(os.path.join('sprites/germs', 'tile035.png'))
]

germ2LeftFacing = [
    image.load(os.path.join('sprites/germs', 'tile045.png')),
    image.load(os.path.join('sprites/germs', 'tile046.png')),
    image.load(os.path.join('sprites/germs', 'tile047.png'))
]

germ3LeftFacing = [
    image.load(os.path.join('sprites/germs', 'tile084.png')),
    image.load(os.path.join('sprites/germs', 'tile085.png')),
    image.load(os.path.join('sprites/germs', 'tile086.png'))
]

germ4LeftFacing = [
    image.load(os.path.join('sprites/germs', 'tile090.png')),
    image.load(os.path.join('sprites/germs', 'tile091.png')),
    image.load(os.path.join('sprites/germs', 'tile092.png'))
]

germ5LeftFacing = [
    image.load(os.path.join('sprites/germs', 'tile081.png')),
    image.load(os.path.join('sprites/germs', 'tile082.png')),
    image.load(os.path.join('sprites/germs', 'tile083.png'))
]

germ1Downfacing = [
    image.load(os.path.join('sprites/germs', 'tile027.png')),
    image.load(os.path.join('sprites/germs', 'tile028.png')),
    image.load(os.path.join('sprites/germs', 'tile029.png'))
]

germ2Downfacing = [
    image.load(os.path.join('sprites/germs', 'tile030.png')),
    image.load(os.path.join('sprites/germs', 'tile031.png')),
    image.load(os.path.join('sprites/germs', 'tile032.png'))
]

germ1UpFacing = [
    image.load(os.path.join('sprites/germs', 'tile003.png')),
    image.load(os.path.join('sprites/germs', 'tile004.png')),
    image.load(os.path.join('sprites/germs', 'tile005.png'))
]

germ2UpFacing = [
    image.load(os.path.join('sprites/germs', 'tile006.png')),
    image.load(os.path.join('sprites/germs', 'tile007.png')),
    image.load(os.path.join('sprites/germs', 'tile008.png'))
]

emptyTile = [
    image.load(os.path.join('sprites/germs', 'tile080.png'))
]

samuraiStance = [
    samuraiAttackDown,
    samuraiAttackLeft,
    samuraiAttackRight,
    samuraiAttackUp
]

germsRightFacing = [
    germ1RightFacing,
    germ2RightFacing,
    germ3RightFacing,
    germ4RightFacing,
    germ5RightFacing
]

germsLeftFacing = [
    germ1LeftFacing,
    germ2LeftFacing,
    germ3LeftFacing,
    germ4LeftFacing,
    germ5LeftFacing
]

germsDownFacing = [
    germ1Downfacing,
    germ2Downfacing
]

germsUpFacing = [
    germ1UpFacing,
    germ2UpFacing
]

widthSpacing = characterWidth // 14
heightSpacing = characterHeight // 14

initialPlacement = [characterWidth * 5 + widthSpacing *
                    5, characterHeight * 5 + heightSpacing * 5]

samuraiPlacement = tuple([initialPlacement[0] + characterWidth * 2 +
                          widthSpacing * 2, initialPlacement[1] + characterHeight * 2 + heightSpacing * 2])


germsLeftOfSamurai = []
germsRightOfSamurai = []
germsAboveSamurai = []
germsBelowSamurai = []

# Randomly deciding germ sprites and generating the right number of germs
for germ in range(0, ((columnsOfGerms - 1) // 2) * rowsOfGerms, 1):
    germsLeftOfSamurai.append(random.choice(germsRightFacing))

for germ in range(0, ((columnsOfGerms - 1) // 2) * rowsOfGerms, 1):
    germsRightOfSamurai.append(random.choice(germsLeftFacing))

for germ in range(0, ((rowsOfGerms - 1) // 2), 1):
    germsAboveSamurai.append(random.choice(germsDownFacing))

for germ in range(0, ((rowsOfGerms - 1) // 2), 1):
    germsBelowSamurai.append(random.choice(germsUpFacing))

samuraiStance = random.choice(samuraiStance)

attackCount = 0
widthChange = 0
heightChange = 0

def redrawGameWindow():

    global walkCount
    global attackCount
    global samuraiPlacement
    global samuraiStance
    global widthChange, heightChange

    win.fill((0, 0, 0))

    if walkCount > 1000:
        walkCount = 0

    # Placing germs on screen

    i = 0
    for germ in germsLeftOfSamurai:
        if i < 5:
            win.blit(germ[walkCount % germSpriteCount], tuple(
                [initialPlacement[0], initialPlacement[1] + characterHeight * i + heightSpacing * i]))
        else:
            win.blit(germ[walkCount % germSpriteCount], tuple([initialPlacement[0] + characterWidth + widthSpacing,
                     initialPlacement[1] + characterHeight * (i - 5) + heightSpacing * (i - 5)]))
        i += 1

    i = 0
    for germ in germsRightOfSamurai:
        if i < 5:
            win.blit(germ[walkCount % germSpriteCount], tuple([initialPlacement[0] + characterWidth * 3 +
                     widthSpacing * 3, initialPlacement[1] + characterHeight * i + heightSpacing * i]))
        else:
            win.blit(germ[walkCount % germSpriteCount], tuple([initialPlacement[0] + characterWidth * 4 + widthSpacing *
                     4, initialPlacement[1] + characterHeight * (i - 5) + heightSpacing * (i - 5)]))
        i += 1

    i = 0
    for germ in germsAboveSamurai:
        win.blit(germ[walkCount % germSpriteCount], tuple([initialPlacement[0] + characterWidth * 2 +
                                                           widthSpacing * 2, initialPlacement[1] + characterHeight * i + heightSpacing * i]))
        i += 1

    i = 0
    for germ in germsBelowSamurai:
        win.blit(germ[walkCount % germSpriteCount], tuple([initialPlacement[0] + characterWidth * 2 +
                                                           widthSpacing * 2, initialPlacement[1] + characterHeight * (i + 3) + heightSpacing * (i + 3)]))
        i += 1

    samuraiDelay = 2  # The samurai animation is delayed compared to germ animation

    samuraiStance = samuraiAttackUp

    if not(fight):
        win.blit(samuraiWaiting[(walkCount//4) %
                 samuraiSpriteCount], samuraiPlacement)
    else:
        if left or right or up or down:
            attackCount += 1

        win.blit(samuraiStance[(
            walkCount//samuraiDelay) % samuraiSpriteCount], samuraiPlacement)
        # print(samuraiPlacement)

        if attackCount >= (4 * samuraiSpriteCount * samuraiDelay):
            attackCount = 0

            if samuraiStance == samuraiAttackDown:
                # samuraiPlacement = tuple([initialPlacement[0] + characterWidth * 2 +
                #                  widthSpacing * 2, initialPlacement[1] + characterHeight * 3 + heightSpacing * 3])
                heightChange += 1
                print("down")

            elif samuraiStance == samuraiAttackUp:

                # samuraiPlacement = tuple([initialPlacement[0] + characterWidth * 2 +
                #                  widthSpacing * 2, initialPlacement[1] + characterHeight * 1 + heightSpacing * 1])
                heightChange -= 1
                print("up")

            elif samuraiStance == samuraiAttackLeft:
                # samuraiPlacement = tuple([initialPlacement[0] + characterWidth * 1 +
                #           widthSpacing * 1, initialPlacement[1] + characterHeight * 2 + heightSpacing * 2])
                widthChange -= 1
                print("left")

            elif samuraiStance == samuraiAttackRight:
                # samuraiPlacement = tuple([initialPlacement[0] + characterWidth * 3 +
                #           widthSpacing * 3, initialPlacement[1] + characterHeight * 2 + heightSpacing * 2])
                widthChange += 1
                print("right")

            if abs(widthChange) < 3 and abs(heightChange) < 3:
                samuraiPlacement = tuple([initialPlacement[0] + characterWidth * (2 + widthChange) +
                                          widthSpacing * (2 + widthChange), initialPlacement[1] + characterHeight * (2 + heightChange) + heightSpacing * (2 + heightChange)])

            # print(widthChange, heightChange)
            # print("new", samuraiPlacement)

    walkCount += 1

    # win.blit(germ4LeftFacing[1], tuple([initialPlacement[0], initialPlacement[1] + characterHeight + heightSpacing]))

    # if left or right or down or up:
    # win.blit(attackRight[walkCount//4], samuraiLocation)
    # walkCount += 1

    # pygame.draw.rect(win, (255,0,0), (x,y,width, height))
    pygame.display.update()


while run:
    clock.tick(18)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right, up, down = False, False, False
    elif keys[pygame.K_RIGHT] and x < 500 - vel - characterWidth:
        x += vel
        right = True
        left, up, down = False, False, False
    elif keys[pygame.K_UP] and y > vel:
        y -= vel
        up = True
        left, right, down = False, False, False
    elif keys[pygame.K_DOWN] and y < 500 - vel - characterHeight:
        y += vel
        down = True
        left, right, up = False, False, False
    elif keys[pygame.K_SPACE]:
        fight = not(fight)
    else:
        right, left, up, down = False, False, False, False
        walkCount = 0

    redrawGameWindow()


pygame.quit()
