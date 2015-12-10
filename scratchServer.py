#!usr/bin/python

import tornado.ioloop
import tornado.websocket

#functions for controlling the robot contained in pi2go.py file.
import pi2go

pi2go.init()

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    
    # This method is called when the Set Server Scratch block is excuted.
    # When this occurs a link has been established between scratch and this server/
    def open(self):
        print("WebSocket opened")
    
    
    def on_close(self):
        print("WebSocket closed")
    
    def check_origin(self, origin):
        return True
    
    # This method is called when any Scratch  block is excuted.
    def on_message(self, message):
        
        #Messages are of the form: "MessageType/Instruction" hence each message
        #from scratch needs to be separated into is consistuent parts.
        print message
        msg= message.split("/")
        
        #MOTOR FUNCTIONS
        if msg[0]== 'stop':
            pi2go.stop()
        
        elif msg[0]== 'forward':
            pi2go.forward(float(msg[1]))
        
        elif msg[0]== 'reverse':
            pi2go.reverse(float(msg[1]))
    
        elif msg[0]== 'spinLeft':
            pi2go.spinLeft(float(msg[1]))
        
        elif msg[0]== 'spinRight':
            pi2go.spinRight(float(msg[1]))
    
        elif msg[0]== 'turnForward':
            pi2go.turnForward(float(msg[1]), float(msg[2]))
        
        elif msg[0]== 'turnReverse':
            pi2go.turnReverse(float(msg[1]), float(msg[2]))
        
        elif msg[0]== 'goM':
            pi2go.go(float(msg[1]), float(msg[2]))
        
        elif msg[0]== 'go':
            pi2go.go(float(msg[1]))

        # SERVO FUNCTIONS
        #elif msg[0]== 'startServos':
            #pi2go.startServos()

        #elif msg[0]== 'stopServos':
            #pi2go.stopServos()

        #elif msg[0]== 'setServos':
            #pi2go.setServo(msg[1],float(msg[2]))


        # LED FUNCTIONS
        #elif msg[0]== 'setLED':
            #pi2go.setLED(msg[1], msg[2], msg[3], msg[4])

        #elif msg[0]== 'setAllLEDs':
            #pi2go.setAllLEDs(msg[1], msg[2], msg[3])

        elif msg[0]== 'LsetLED':
            pi2go.LsetLED(msg[1], msg[2])

        # IR FUNCTIONS
        elif msg[0]== 'irLeft':
            val = pi2go.irLeft()
            self.write_message(str(val))
        
        elif msg[0]== 'irRight':
            val = pi2go.irRight()
            self.write_message(str(val))
    
        elif msg[0]== 'irLeftLine':
            val =pi2go.irLeftLine()
            self.write_message(str(val))
        
        elif msg[0]== 'irRightLine':
            val= pi2go.irRightLine()
            self.write_message(str(val))

        # ULTRASONIC FUNCTION
        elif msg[0]== 'ultraSonic':
            val=pi2go.getDistance()
            self.write_message(str(val))


app = tornado.web.Application([
                               (r'/', EchoWebSocket),
                               ])

if __name__ == '__main__':
    try:
        #parse_command_line()
        app.listen(1234)
        tornado.ioloop.IOLoop.instance().start()
    
    except KeyboardInterrupt:
        pass
    
    
    finally:
        pi2go.cleanup()









