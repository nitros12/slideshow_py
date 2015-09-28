import turtle
turtle.hideturtle()
turtle.setworldcoordinates(0,0,885,500)
turtle.delay(0)
turtle.tracer(False)
def draw_quad(h,w,x,y,c):
    turtle.hideturtle()
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
    draw_quad(100,885,x,y+400,'#888899')
    draw_quad(400,885,x,y,'#555566')
    draw_text(top, x+10, y+420, 50)
    for i in range((len(main)//90)+1):
        draw_text(main[i*90:(i+1)*90],x+30,y+(380-(i*15)),15)
def animate_fw(slide1, slide2):
    for i in range(100):
        turtle.clear()
        draw_slide(slide1[0],slide1[1],-885+(i*8.85),0)
        draw_slide(slide2[0],slide2[1],i*8.85,0)
        turtle.update()
    return
slides = open('slides.txt','r').readlines()
slidelst = [item.strip('\n') for item in slides]
slides = []
for i in range(len(slidelst)//2):
    slides.append([slidelst[i*2],slidelst[(i*2)+1]])
for i in range(len(slides)-1):
    turtle.clear()
    draw_slide(slides[i][0],slides[i][1],0,0)
    turtle.update()
    input('enter to advance: ')
    animate_fw(slides[i+1],slides[i])
print('done')
