# Use for Logitech camera.

import cv2

class CameraControl():
    def __init__(self):
        self.camera = None
        self.frame = None
        # self.frame = self.camera.read()
        # if self.frame == None:
        #     print('NONE frame!')
        # else:
        #     # Change frame color
        #     self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)


    def is_available(self):
        '''Return True if camera is opened, otherwise is False.'''

        if self.camera == None:
            return False
            
        return self.camera.isOpened()


    def open_connection(self):
        '''Return True if connect successfully, otherwise is False.'''

        self.camera = cv2.VideoCapture(0)
        return self.is_available()


    def close_connection(self):
        '''Close CAMERA connection.'''
        if self.camera == None:
            return True

        self.camera.release()
        cv2.destroyAllWindows()

        return self.is_available()


    def get_frame(self):
        '''Return frame if get frame successfully. Otherwise return None.'''

        if not self.is_available():
            return None

        result, self.frame = self.camera.read()
        
        if result == False:
            return None

        # Change frame color
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        return self.frame

    
    def flip_frame(self, input_frame):
        '''Flip frame.'''

        if input_frame is None:
            return None

        output_frame = cv2.flip(input_frame, 1)
        return output_frame


    def get_frame_size(self):
        '''Return (frame width, frame height). Otherwise, return None.'''

        if self.frame == None:
            return None

        frame_height, frame_width, layers = self.frame.shape
        return frame_width, frame_height


    def rotate_frame(self, angle):
        '''Rotate frame 90-180-270 degrees clockwise. 
        Return True if success. Otherwise, return False.'''

        if angle == 90:
            self.frame = cv2.rotate(self.frame, cv2.ROTATE_90_CLOCKWISE)
            return True

        if angle == 180:
            self.frame = cv2.rotate(self.frame, cv2.ROTATE_180)
            return True

        if angle == 270:
            self.frame = cv2.rotate(self.frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
            return True

        return False
