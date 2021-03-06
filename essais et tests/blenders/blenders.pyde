# Des réglages pour la fenêtre, pour le fond
size(int(displayWidth*0.45),displayHeight-100,P2D)
frame.setLocation(displayWidth-int(displayWidth*0.45), 0)
randomSeed(millis())
blendMode(BLEND)
background(255)
imageMode(CENTER)
noStroke()

# Des couleurs sympas
noir = color(0, 0, 0)
blanc = color(255, 255, 255)
rouge = color(255, 0, 0)
vert = color(0, 255, 0)
bleu = color(0, 0, 255)
violet = color(116,49,193)
vertsapin = color(7,131,16)
orange = color(255, 150, 60)

# Des modes de remix

def remixdoux ():
    blendMode(EXCLUSION)

def remixcool ():
    blendMode(SUBTRACT)

def remixpop ():
    blendMode(MULTIPLY)

def remixzero ():
    blendMode(BLEND)


# Des déplacements simples
def aumilieu():
    resetMatrix()
    translate (width/2, height/2)
    
def remonte ():
    translate (0, -40)
    
def monte ():
    remonte()
    
def plushaut ():
    remonte()
    
def descend ():
    translate (0, 40)
    
def plusbas ():
    descend()
    
def agauche ():
    translate (-40, 0)
    
def adroite ():
    translate (40, 0)
    
def pluspetit():
    scale(0.5)
    
def plusgrand():
    scale(2)
    
def retourne():
    scale(-1, 0)
    
def audepart():
    resetMatrix()

# Des formes de base
def cercle(rayon):
    ellipse(0,0,rayon,rayon)
    
def carre(largeur):
    rect(0,0,largeur,largeur)
    
def hexagone(taille = 20):
    pushMatrix()
    translate (taille, taille)
    beginShape()
    stroke(0,0)
    for i in range (6):
        x = cos( i * THIRD_PI ) * taille
        y = sin( i * THIRD_PI ) * taille
        vertex( x, y )
    endShape()
    popMatrix()
    
def octogone(taille = 20):
    pushMatrix()
    translate (taille, taille)
    beginShape()
    stroke(0,0)
    for i in range (8):
        x = cos( i * PI/4 ) * taille
        y = sin( i * PI/4 ) * taille
        vertex( x, y )
    endShape()
    popMatrix()

p5triangle = triangle

def triangle(taille = 20):
    pushMatrix()
    translate (taille, taille)
    p5triangle(taille, 0, 0, taille, -taille, 0)
    popMatrix()
    
    
# Des morceaux de peintures
tampon_kupka = loadImage("kupka.jpg")

def kupka(taille = 20):
    pushMatrix()
    scale(taille/40.0)
    image(tampon_kupka, 0,0)
    popMatrix()

tampon_valensi = loadImage("valensi.jpg")

def valensi(taille = 20):
    pushMatrix()
    scale(taille/40.0)
    image(tampon_valensi, 0,0)
    popMatrix()

tampons_stanton = [loadImage("stanton%d.png" % i) for i in range(14)]

def stanton(taille = 20):
    from random import choice
    pushMatrix()
    scale(taille/40.0)
    image(choice(tampons_stanton), 0,0)
    popMatrix()


# Des opérations magiques

def antonio(couleur):
    for n in range(30):
        pushMatrix()
        scale(1 + (random(10)-5)/20.0)
        translate(random(width), random(height))
        for i in range(110,10,-20):
            fill(couleur)
            cercle(i)
            fill(255)
            cercle(i-12)
        fill(couleur)
        cercle(10)
        popMatrix()    
        
def splash(forme = None, fois = None):
    if fois is None:
        fois = 30
    for n in range(fois):
        pushMatrix()
        scale(1 + (random(10)-5)/20.0)
        translate(random(width-n*3), random(height-n*3))
        forme(n*3)
        popMatrix()
    
def zoom(forme, fois = 30):
    for n in range(fois):
        pushMatrix()
        translate(10*n, 10*n)
        forme(n*10)
        popMatrix()

def spirale(forme, fois = 500):
    pushMatrix()
    translate(width/2, height/2)
    for n in range(fois):
        rotate (0.1)
        translate(n/10+5, 0)
        forme(20)
    popMatrix()
    
def moulin(forme, fois = 10):
    for n in range(fois):
        pushMatrix()
        scale(1 + (random(10)-5)/20.0)
        translate(random(width), random(height))
        for tour in range (120):
            rotate (radians(tour*3))
            pushMatrix()
            translate(-20,-20)
            forme(40)
            popMatrix()
        popMatrix() 

def tourbillon(forme, fois = 500, nbras = 3):
    pushMatrix()
    for n in range(fois):
        for bras in range(nbras):
            rotate(2*PI/nbras)
            pushMatrix()
            rotate(0.1 * n)
            translate(3 * n, 0)
            forme()
            popMatrix()
    popMatrix()
    
    
# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# Au dessus ce sont les définitions de nos formes      
  
  
# Copiez les noms de vos formes en dessous de cette ligne        
# v v v v v v v v v v v v v v v v v v v v v v v v v v v v


aumilieu()
plusbas()
plusbas()

fill(orange)
spirale(hexagone, 1000)

agauche()
fill(vert)
spirale(cercle, 1000)

plusbas()
fill(rouge)
spirale(carre, 1000)

remixdoux()
audepart()

plushaut()
plushaut()
plushaut()
plushaut()
plushaut()
plushaut()
plushaut()
plushaut()
plushaut()
plushaut()
plushaut()
plushaut()
plushaut()
plushaut()
fill(orange)
spirale(hexagone, 1000)

adroite()
fill(vert)
spirale(cercle, 1000)

adroite()
fill(rouge)
spirale(carre, 1000)

# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# Ici c'est la fin... 
