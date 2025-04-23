import cv2
import numpy as np

def adjust_brightness_contrast(image, alpha, beta):#alpha = contrast multiplier  beta=brightness shift
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)  # clips values to 0–255

def nothing(x):
    pass

# Load the image
image = cv2.imread("Capture1.PNG")
if image is None:
    print("❌ Error: input.jpg not found.")
    exit()

# Create named windows BEFORE creating trackbars
cv2.namedWindow("Adjustments")
cv2.namedWindow("Original")

# Create trackbars inside the 'Adjustments' window
cv2.createTrackbar("Contrast (x10)", "Adjustments", 10, 30, nothing)  # Alpha = 1.0 - 3.0
cv2.createTrackbar("Brightness", "Adjustments", 0, 100, nothing)      # Beta = 0 - 100

while True:
    # Get trackbar values
    alpha = cv2.getTrackbarPos("Contrast (x10)", "Adjustments") / 10.0
    beta = cv2.getTrackbarPos("Brightness", "Adjustments")

    # Apply transformation
    adjusted = adjust_brightness_contrast(image, alpha, beta)

    # Show images
    cv2.imshow("Original", image)
    cv2.imshow("Adjustments", adjusted)

    # Exit on ESC
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
