# from ultralytics import YOLO

# model = YOLO('best(1).pt')

# results = model.predict(source=0, conf=0.25, show=True)

# import os

# def delete_zip_files(folder_path):
#     # Check if the folder exists
#     if not os.path.exists(folder_path):
#         print(f"The folder '{folder_path}' does not exist.")
#         return
    
#     # Iterate through all files in the folder
#     for file_name in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, file_name)
        
#         # Check if the file has a .zip extension and is a file (not a folder)
#         if file_name.endswith('.csv') and os.path.isfile(file_path):
#             try:
#                 os.remove(file_path)
#                 print(f"Deleted: {file_path}")
#             except Exception as e:
#                 print(f"Error deleting {file_path}: {e}")
    
#     print("All .zip files deleted successfully.")

# # Example usage
# folder_path = "C:/Users/tejes/Downloads"  # Replace with the path to your folder
# delete_zip_files(folder_path)

import cv2
import numpy as np

# Load the image
image = cv2.imread('epi.jpg')  # Replace with your image path

image=cv2.resize(image,(660,295))
# Save or display the modified image
cv2.imwrite('temp.jpg', image)

