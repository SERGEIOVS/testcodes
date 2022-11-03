from pynput import mouse

def on_move(x , y):
    print('Mouse_x (move) : {0}'.format(( x ) ) , '|' , 'Mouse_y  (move): {0}'.format(( y ) ) )

def on_click(x , y , button , pressed):
    print('{0} {1}'.format('Pressed : ' if pressed else 'Released : ' , (x , y ) ) )

    if not pressed:
        # Stop listener
        return False

def on_scroll(x , y , dx , dy ) :
    print('Scrolled : {0} {1}'.format('down' if dy < 0 else 'up' , ( x , y ) ) ) 

# Collect events until released
with mouse.Listener(
        on_move = on_move ,
        on_click = on_click ,
        on_scroll = on_scroll) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move = on_move ,
    on_click = on_click ,
    on_scroll = on_scroll)
listener.start()