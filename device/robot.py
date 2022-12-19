import serial

class RobotControl():
    def __init__(self):
        self.__robot_port = 'COM1'
        self.__baudrate = 9600
        self.__timeout = 1
        self.robot_serial = serial.Serial(self.__robot_port, self.__baudrate, timeout=self.__timeout)


    def is_connected(self):
        '''Return True if robot connection is open, otherwise is False.'''

        return self.robot_serial.is_open()


    def open_connection(self):
        '''Return True if connect successfully, otherwise is False.'''

        if self.is_connected() == True:
            return True

        self.robot_serial = serial.Serial(self.__robot_port, self.__baudrate, timeout=self.__timeout)
        return self.is_connected()


    def close_connection(self):
        '''Return True if close connection successfully. Otherwise, return False.'''

        if self.is_connected() == False:
            return True
            
        self.robot_serial.close()
        # self.robot_serial.__del__()
        return self.is_connected()

    
    def go_home(self):
        '''Force ROBOT get back to home position. 
        Return True if send command successfully, otherwise is False.'''

        if self.is_connected() == False:
            print("Port is not open")
            return False

        self.robot_serial.write(b'G28' + b'\r\n')
        return True


    def go_to_point(self, pos_x, pos_y, pos_z):
        '''Force ROBOT move to point (x, y, z). 
        Return True if send command successfully, otherwise is False.'''

        if self.is_connected() == False:
            print("Port is not open")
            return False

        self.robot_serial.write(f"G01 X{pos_x} Y{pos_y} Z{pos_z}".encode() + b'\r\n')
        return True
