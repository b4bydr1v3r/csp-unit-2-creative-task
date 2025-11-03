from cmu_graphics import *

# background
app.background = 'Black'

# logo left
CircleL = Circle(100, 280, 30, fill=rgb(210, 255, 0))
PolyL1 = Polygon(100, 310, 200, 310, 210, 260, 100, 260, fill=rgb(210, 255, 0))
PolyL2 = Polygon(69.5, 280, 110, 90, 160, 90, 120, 280, fill=rgb(210, 255, 0))
TriangleL = Polygon(110, 90, 160, 90, 118, 50, fill=rgb(210, 255, 0))

# logo right
CircleR = Circle(300, 120, 30, fill=rgb(210, 255, 0))
PolyR1 = Polygon(300, 90, 200, 90, 175, 220, 218, 220, 232, 150, 300, 150, fill=rgb(210, 255, 0))
PolyR2 = Polygon(330.5, 121, 290, 310, 240, 310, 280, 120, fill=rgb(210, 255, 0))
TriangleR = Polygon(240, 310, 290, 310, 281, 350, fill=rgb(210, 255, 0))

# custom properties
TriangleL.verstappen = 0
TriangleR.verstappen = 0

pitStopLabels = []

# define a counter for centerY
centerY = -20

def onMousePress(mouseX, mouseY):
    # background changes
    if app.background == 'Black':
        app.background = 'Snow'
    elif app.background == 'Snow':
        app.background = rgb(140, 141, 146)
    elif app.background == rgb(140, 141, 146):
        app.background = rgb(255, 128, 0)
    else:
        app.background = 'Black'

    # logo changes
    if TriangleL.hits(mouseX, mouseY) or TriangleR.hits(mouseX, mouseY):
        TriangleL.verstappen += 1
        TriangleR.verstappen += 1

    # check counts explicitly
    total = TriangleL.verstappen + TriangleR.verstappen
    if total == 2:
        TriangleL.fill = rgb(161, 221, 237)
        TriangleR.fill = rgb(161, 221, 237)
    elif total == 4:
        TriangleL.fill = rgb(161, 221, 237)
        TriangleR.fill = rgb(161, 221, 237)
        PolyL2.fill = rgb(161, 221, 237)
        PolyR2.fill = rgb(161, 221, 237)
        CircleL.fill = rgb(161, 221, 237)
        CircleR.fill = rgb(161, 221, 237)
        PolyL1.fill = rgb(161, 221, 237)
        PolyR1.fill = rgb(161, 221, 237)
    elif total == 6:
        TriangleL.fill = rgb(210, 255, 0)
        TriangleR.fill = rgb(210, 255, 0)
        PolyL2.fill = rgb(210, 255, 0)
        PolyR2.fill = rgb(210, 255, 0)
        CircleL.fill = rgb(210, 255, 0)
        CircleR.fill = rgb(210, 255, 0)
        PolyL1.fill = rgb(210, 255, 0)
        PolyR1.fill = rgb(210, 255, 0)

def onMouseRelease(mouseX, mouseY):
    global centerY
    centerY += 20
    pitStop = Label("LET'S GO LANDO", 200, centerY, fill=rgb(255, 128, 0), bold=True, italic=True)
    pitStopLabels.append(pitStop)
    if app.background == rgb(255, 128, 0):
        for label in pitStopLabels:
            label.fill = rgb(140, 141, 146)
    else:
        for label in pitStopLabels:
            label.fill = rgb(255, 128, 0)



















cmu_graphics.run()