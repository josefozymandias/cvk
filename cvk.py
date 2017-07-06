print "+-------------------------+"
print "|                         |"
print "| Cannibal * Vegan * Kale |"
print "|                         |"
print "+-------------------------+"
print
print "Try to get everyone across without"
print "them eating eachother."
start = ['c','v','k']
end   = []
boat  = ' '
startside = 0
endside = 1
boatside = startside

def draw_scene():
    print
    for i in end: print " " + i,
    print
    if boatside == endside:
        print "  [" + boat + "]  "
    print "~~~~~~~"
    print "~~~~~~~"
    print "~~~~~~~"
    if boatside == startside:
        print "  [" + boat + "]  "
    for i in start: print " " + i,
    print

def load_boat(letter):
    global boat
    if boat == ' ':
        if boatside == startside:
            if letter in start:
                start.remove(letter)
                boat = letter
        else:
            if letter in end:
                end.remove(letter)
                boat = letter

def unload_boat():
    global boat
    if boat != ' ':
        if boatside == startside:
            start.append(boat)
        else:
            end.append(boat)
        boat = ' '

while True:
    draw_scene()
    print "Quit = q"
    print "Put c, v, k on boat = c, v, k"
    print "Move boat = m"
    print "Unload boat = u"
    print "> ",
    i = raw_input()
    if i == 'q':
        break
    elif i == 'c':
        load_boat('c')
    elif i == 'v':
        load_boat('v')
    elif i == 'k':
        load_boat('k')
    elif i == 'm':
        if boatside == startside: boatside = endside
        else: boatside = startside
    elif i == 'u':
        unload_boat()

    if 'c' in start and 'v' in start and boatside == endside:
        print "Cannibal eats Vegan"
        break
    if 'c' in end   and 'v' in end   and boatside == startside:
        print "Cannibal eats Vegan"
        break
    if 'v' in start and 'k' in start and boatside == endside:
        print "Vegan eats Kale"
        break
    if 'v' in end   and 'k' in end   and boatside == startside:
        print "Vegan eats Kale"
        break
    if 'c' in end and 'v' in end and 'k' in end:
        draw_scene()
        print "Congratulations!!!"
        break
