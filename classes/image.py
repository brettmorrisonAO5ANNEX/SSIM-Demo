import cv2
import numpy as np

#demo designed for images in the RGB color space
class Image:
    #constructor
    def __init__(self, imagepath):
        #a cv2 image object for the image
        self.image = cv2.imread(imagepath)

        #an array representation of the array
        self.image_array = self.create_image_array()

        #set to 3 by default b/c demo is designed for RGB
        self.channels = 3

        #3D array containing the windows/patches of the image
        self.windows = self.extract_windows()

    #converts color space and creates an array version of the image
    def create_image_array(self):
        # Convert BGR to RGB (if needed)
        rgb_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        # Convert the cv2 image instance to a NumPy array
        return np.array(rgb_image)

    #extracts 4 regions from image and stores them in windows
    def extract_windows(self):
        # Get the height and width of the image
        height, width = self.image.shape[:2]

        #define window size
        window_width = int(np.ceil(width / 2))
        window_height = int(np.ceil(height / 2))

        #pad image w/ 0's to be able to split image into 4 (window_height x window_width) regions
        pad_x = (2*window_width - width)
        pad_y = (2*window_height - height)
        padded_image = np.pad(self.image_array, ((0, pad_y), (0, pad_x), (0, 0)), mode='constant', constant_values=0)

        #fetch dimensions of padded image
        padded_height, padded_width = padded_image.shape[:2]

        # Initialize the windows array
        windows = np.empty((4, window_height, window_width, 3))

        curr_window = 0
        for y in range(0, padded_height, window_height):
            for x in range(0, padded_width, window_width):
                windows[curr_window] = padded_image[y:y+window_height, x:x+window_width]
                curr_window += 1

        return windows
    
    #for testing
    def save_windows(self, name):
        window_num = 0
        for window in self.windows:
            #convert to uint8
            window_8bit = window.astype(np.uint8)
            cv2.imwrite(f"windows/{name}_window{window_num+1}.png", cv2.cvtColor(window_8bit, cv2.COLOR_RGB2BGR))
            window_num += 1
