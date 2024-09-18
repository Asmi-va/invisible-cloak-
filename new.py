import cv2
import numpy as np
import time

# Initialize the video writer
fourCC = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_auto_detect.avi', fourCC, 20, (640, 480))  # Adjust to your webcam resolution
cap = cv2.VideoCapture(0)

# Countdown before starting to allow the user to set up
for i in range(3, 0, -1):
    print(f"Starting in {i} seconds...")
    time.sleep(1)
print("Go!")

# Background capturing variables
background = 0
for i in range(60):
    ret, background = cap.read()
    if ret:
        background = np.flip(background, axis=1)  # Flip to avoid mirror effect

# Automatic color detection based on dominant color in cloak region
def get_dominant_color(image, region=(100, 300, 100, 300)):
    """Extracts the dominant color in a specified region of the image"""
    region_img = image[region[0]:region[1], region[2]:region[3]]
    region_hsv = cv2.cvtColor(region_img, cv2.COLOR_BGR2HSV)
    dominant_hue = np.median(region_hsv[:, :, 0])
    dominant_sat = np.median(region_hsv[:, :, 1])
    dominant_val = np.median(region_hsv[:, :, 2])
    
    # Adjust hue ranges dynamically based on dominant color
    lower_bound = np.array([dominant_hue - 10, max(50, dominant_sat - 50), max(50, dominant_val - 50)])
    upper_bound = np.array([dominant_hue + 10, min(255, dominant_sat + 50), min(255, dominant_val + 50)])
    return lower_bound, upper_bound

cloak_active = False

while cap.isOpened():
    returnV, img = cap.read()
    if not returnV:
        break
    
    img = np.flip(img, axis=1)  # Flip the current frame to avoid mirror effect

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Convert image to HSV

    # Get color range based on the cloak region
    lower_bound, upper_bound = get_dominant_color(img)

    # Create masks for the cloak
    mask1 = cv2.inRange(hsv, lower_bound, upper_bound)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))  # Remove noise

    # Invert the mask to get the rest of the image
    mask2 = cv2.bitwise_not(mask1)

    # Apply the masks to the images
    result1 = cv2.bitwise_and(img, img, mask=mask2)  # Everything except the cloak
    result2 = cv2.bitwise_and(background, background, mask=mask1)  # Background where the cloak is

    # Combine the two results
    finalOutput = cv2.addWeighted(result1, 1, result2, 1, 0)

    out.write(finalOutput)  # Save the output to a video file
    cv2.imshow('Magic Cloak!', finalOutput)  # Show the final output

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up resources
cap.release()
out.release()
cv2.destroyAllWindows()
