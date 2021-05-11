import os
import pygame
from pygame import image
import random

pygame.init()

run = True

# These are the only numbers that should be edited
# ====================================================
columnsOfGerms = 5  # keep this an odd number for nice look
rowsOfGerms = 5  # keep this an odd number for nice look
samuraiDelay = 2  # The samurai animation is delayed compared to germ animation
# ====================================================

x = 50
y = 425
characterWidth = 24  # width of sprites in pixels
characterHeight = 32  # height of sprites in pixels
vel = 5

screenWidth = characterWidth * columnsOfGerms * 3  # To leave gap above and below
screenHeight = characterHeight * rowsOfGerms * \
    3  # To leave a gap on both sides of screen

# How much space to leave horizontally between characters
widthSpacing = characterWidth // ((columnsOfGerms * 3) - 1)
# How much space to leave vertically between characters
heightSpacing = characterHeight // ((rowsOfGerms * 3) - 1)

initialPlacement = [characterWidth * columnsOfGerms + widthSpacing *
                    columnsOfGerms, characterHeight * rowsOfGerms + heightSpacing * rowsOfGerms]  # Start charachater placement from this point

samuraiPlacement = tuple([initialPlacement[0] + (characterWidth + widthSpacing) * ((columnsOfGerms - 1) // 2),
                         initialPlacement[1] + (characterHeight + heightSpacing) * ((rowsOfGerms - 1) // 2)])

left, right, up, down, attack = False, False, False, False, False
fight = False

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("First game")

clock = pygame.time.Clock()

animationCount = 0

totalGerms = columnsOfGerms * rowsOfGerms - 1  # because Samurai takes one space

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

emptyTile = image.load(os.path.join('sprites/germs', 'tile080.png'))

samuraiAttackingStances = [
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

# randomly selecting the attacking direction of samurai
samuraiStance = random.choice(samuraiAttackingStances)

attackCount = 0
widthChange = 0
heightChange = 0

# contains all places where germs were but are now killed
placementsOfGermsKilled = [samuraiPlacement]

# contains all places where germs are still alive
placementsOfAliveGerms = []


def redrawGameWindow():

    global animationCount
    global attackCount
    global samuraiPlacement
    global samuraiStance
    global widthChange, heightChange
    global placementsOfAliveGerms, placementsOfGermsKilled

    # remove all previous renderings on screen, this happens every frame
    win.fill((0, 0, 0))

    if animationCount > 1000:  # this is just so this counter doesn't overflow
        animationCount = 0

    # Placing germs on screen
    for i in range(0, (columnsOfGerms - 1) // 2, 1):  # columns
        for j in range(0, rowsOfGerms, 1):  # rows

            placementOfGermOnLeftOfSamurai = tuple(
                [initialPlacement[0] + (characterWidth + widthSpacing) * i, initialPlacement[1] + (characterHeight + heightSpacing) * j])

            if placementOfGermOnLeftOfSamurai in placementsOfGermsKilled:
                # place an empty tile where the germ has been killed
                win.blit(emptyTile, placementOfGermOnLeftOfSamurai)

            else:
                win.blit(germsLeftOfSamurai[i + j][animationCount %
                         germSpriteCount], placementOfGermOnLeftOfSamurai)

                # keeping track of alive germ locations to guide samurai towards them
                if placementOfGermOnLeftOfSamurai not in placementsOfAliveGerms:
                    placementsOfAliveGerms.append(
                        placementOfGermOnLeftOfSamurai)

            placementOfGermOnRightOfSamurai = tuple(
                [initialPlacement[0] + (characterWidth + widthSpacing) * (columnsOfGerms - i - 1), initialPlacement[1] + (characterHeight + heightSpacing) * j])

            if placementOfGermOnRightOfSamurai in placementsOfGermsKilled:
                # place an empty tile where the germ has been killed
                win.blit(emptyTile, placementOfGermOnLeftOfSamurai)

            else:
                win.blit(germsRightOfSamurai[i + j][animationCount %
                         germSpriteCount], placementOfGermOnRightOfSamurai)

                # keeping track of alive germ locations to guide samurai towards them
                if placementOfGermOnRightOfSamurai not in placementsOfAliveGerms:
                    placementsOfAliveGerms.append(
                        placementOfGermOnRightOfSamurai)

    for i in range(0, (rowsOfGerms - 1)//2, 1):
        placementOfGermAboveSamurai = tuple(
            [initialPlacement[0] + (characterWidth + widthSpacing) * ((columnsOfGerms - 1) // 2), initialPlacement[1] + (characterHeight + heightSpacing) * i])

        if placementOfGermAboveSamurai in placementsOfGermsKilled:
            # place an empty tile where the germ has been killed
            win.blit(emptyTile, placementOfGermOnLeftOfSamurai)
        else:
            win.blit(germsAboveSamurai[i][animationCount %
                     germSpriteCount], placementOfGermAboveSamurai)

            if placementOfGermAboveSamurai not in placementsOfAliveGerms:
                placementsOfAliveGerms.append(placementOfGermAboveSamurai)

        placementOfGermBelowSamurai = tuple(
            [initialPlacement[0] + (characterWidth + widthSpacing) * ((columnsOfGerms - 1) // 2), initialPlacement[1] + (characterHeight + heightSpacing) * (rowsOfGerms - i - 1)])

        if placementOfGermBelowSamurai in placementsOfGermsKilled:
            # place an empty tile where the germ has been killed
            win.blit(emptyTile, placementOfGermOnLeftOfSamurai)
        else:
            win.blit(germsBelowSamurai[i][animationCount %
                     germSpriteCount], placementOfGermBelowSamurai)

            if placementOfGermBelowSamurai not in placementsOfAliveGerms:
                placementsOfAliveGerms.append(placementOfGermBelowSamurai)

    # samuraiStance = samuraiAttackDown  # delete this later - only for testing

    if not(fight):
        win.blit(samuraiWaiting[(animationCount//4) %
                 samuraiSpriteCount], samuraiPlacement)
    else:
        if left or right or up or down:
            attackCount += 1

        win.blit(samuraiStance[(
            animationCount//samuraiDelay) % samuraiSpriteCount], samuraiPlacement)
        # print(samuraiPlacement)

        if attackCount >= (4 * samuraiSpriteCount * samuraiDelay):
            attackCount = 0

            nextLocationHeightAddition = 0
            nextLocationWidthAddition = 0

            if samuraiStance == samuraiAttackDown:
                heightChange += 1
                print("down")
                nextLocationHeightAddition = 1

            elif samuraiStance == samuraiAttackUp:
                heightChange -= 1
                print("up")
                nextLocationHeightAddition = -1

            elif samuraiStance == samuraiAttackLeft:
                widthChange -= 1
                print("left")
                nextLocationWidthAddition = -1

            elif samuraiStance == samuraiAttackRight:
                widthChange += 1
                print("right")
                nextLocationWidthAddition = +1

            # making sure samurai does not go into the world beyond the germs
            if abs(widthChange) > (columnsOfGerms - 1) // 2:
                if widthChange < 0:
                    widthChange = -1 * (columnsOfGerms - 1) // 2
                else:
                    widthChange = (columnsOfGerms - 1) // 2

            if abs(heightChange) > (rowsOfGerms - 1) // 2:
                if heightChange < 0:
                    heightChange = -1 * (rowsOfGerms - 1) // 2
                else:
                    heightChange = (rowsOfGerms - 1) // 2

            # updating where the samurai is now
            samuraiPlacement = tuple([initialPlacement[0] + (characterWidth + widthSpacing) * (((columnsOfGerms - 1) // 2) + widthChange),
                                      initialPlacement[1] + (characterHeight + heightSpacing) * (((rowsOfGerms - 1) // 2) + heightChange)])

            if samuraiPlacement not in placementsOfGermsKilled:  # make sure not to add the same entry again
                placementsOfGermsKilled.append(samuraiPlacement)
                placementsOfAliveGerms.remove(samuraiPlacement)

            loacationInFrontOfSamurai = tuple(
                [initialPlacement[0] + (characterWidth + widthSpacing) * (((columnsOfGerms - 1) // 2) + widthChange + nextLocationWidthAddition),
                 initialPlacement[1] + (characterHeight + heightSpacing) * (((rowsOfGerms - 1) // 2) + heightChange + nextLocationHeightAddition)])

            if loacationInFrontOfSamurai not in placementsOfAliveGerms:
                # randomly changing the attacking direction of samurai
                samuraiStance = random.choice(samuraiAttackingStances)

    animationCount += 1  # this helps with the animations

    # print(len(placementsOfAliveGerms))

    pygame.display.update()  # update screen


while run:
    # game runs at 18 frames per second, increasing this number will make animations faster
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
        animationCount = 0

    redrawGameWindow()


pygame.quit()
