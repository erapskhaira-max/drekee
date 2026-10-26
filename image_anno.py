import cv2
import matplotlib.pyplot as plt

#step 1: load the image 
image_path = 'example.jpg' # User-provided image path
image = cv2.imread(image_path)

#Convert BGR to RGB for correct color display with matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions
height , width , _= image_rgb.shape

#step 2: Draw TWO Rectangles Around the Interesting Regions
# Rectangle 1: Top-left corner
rect1_width, rect1_height = 150,150
top_left1 = (20,20) # fixed 20 pixels padding from top-left
bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_height)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0,255,0),3) #Yellow rectangle

# Rectangle 2: bottom-right corner
rect2_width,rect2_height = 200,150
top_left2 = (width - rect2_width - 20 , height - rect2_height - 20 ) # 20 pixels padding
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)
cv2.rectangle(image_rgb, top_left2, bottom_right2 , (225,0,225),3) # magenta rectangle 

# step 3: Draw Circles at the centers of both the rectangles
center1_x = top_left1[0] + rect1_width // 2 
center1_y = top_left1[1] + rect1_height //2
center2_x = top_left2[0] + rect2_width // 2 
center2_y = top_left2[1] + rect2_height //2
cv2.circle(image_rgb , (center1_x, center1_y) , 15,(0, 255, 0),-1) # filled green color circle 






