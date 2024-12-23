import cv2
import time
from ultralytics import SAM, FastSAM
from ultralytics.hub.utils import ONLINE

# Disable online mode
ONLINE = False

# Load the SAM model
model = SAM("sam2.1_s.pt")

# Display model information (optional)
model.info()

# Load and prepare the image
img = cv2.imread("./nature.jpg")
if img is None:
    print("Error: Unable to load image. Please check the file path.")
    exit(1)

print("Image shape:", img.shape)

# Prompt user for an option
options = {
    1: "Bounding box",
    2: "Single point",
    3: "Multiple points",
    4: "Multiple points per object",
    5: "Negative points"
}

print("Select an option:")
for key, value in options.items():
    print(f" {key}. {value}")

try:
    num = int(input("Enter your choice: "))
    if num not in options:
        raise ValueError("Invalid option")
except ValueError as e:
    print("Invalid option selected. Exiting.")
    exit(1)

# Define reusable points for prompts
bbox_points = [[661, 997], [1893, 1516]]
multi_points = [[661, 997], [1893, 1516]]

# Process based on selected option
if num == 1:
    results = model(img, bboxes=[bbox_points[0][0], bbox_points[0][1], bbox_points[1][0], bbox_points[1][1]], show=True)
    print("Results:", results)

elif num == 2:
    results = model(img, points=[661, 997], labels=[1], show=True)

elif num == 3:
    results = model(img, points=multi_points, labels=[1, 1], show=True)

elif num == 4:
    results = model(img, points=[multi_points], labels=[[1, 1]], show=True)

elif num == 5:
    results = model(img, points=[multi_points], labels=[[1, 0]], show=True)

# Wait for user to close the window
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
