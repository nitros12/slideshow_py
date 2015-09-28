import turtle
turtle.ht()
turtle.setworldcoordinates(0,0,885,500)
turtle.delay(0)
turtle.tracer(None)
def draw_quad(h,w,x,y,c):
    turtle.fillcolor(c)
    turtle.pu()
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.goto(x+w,y)
    turtle.goto(x+w,y+h)
    turtle.goto(x,y+h)
    turtle.goto(x,y)
    turtle.end_fill()
def draw_text(text, x,y,s):
    turtle.goto(x,y)
    turtle.write(text,False,align="left",font=("Ubuntu",s,"normal"))
def draw_slide(top, main, x, y):
    draw_quad(100,885,0,400,'#888899')
    draw_quad(400,885,0,0,'#555566')
    draw_text(top, 10, 420, 50)
    print(len(main)//100)
    for i in range((len(main)//100)+1):
        draw_text(main[i*100:(i+1)*100],30,380-(i*15),15)
        print("drew {} at x {} y {}".format(main[i*100:(i+1)*100], 30, 390-(i*15)))
draw_slide("hello","potatoes r guds for yous",0,0)
turtle.update()
    
