from turtle import Turtle, mainloop, done

def tree(plist, length=200, angle=65, factor=0.62, width=12): 
    """
    plist is list of pens
    length is length of branch
    angle is half of the angle between 2 branches
    factor is factor by which branch is shorented
    width is current width of branches in that level
    """

    if length > 3:
        
        lst = []

        for p in plist:
            p.width(width)
            if length < 7:
                p.color('green')

            p.forward(length)
            q = p.clone()
            p.left(angle)
            q.right(angle)
            lst.append(p)
            lst.append(q)

        tree(lst, length * factor,angle,factor, width * 0.75)

            





if __name__ == "__main__":


    p = Turtle()
    p.hideturtle()
    p.speed(0)
    p.getscreen()
    p.getscreen()

    p.left(90)
    p.penup() 
    p.forward(-210)
    p.pendown()
    p.color('brown')
    tree([p])

    mainloop()




