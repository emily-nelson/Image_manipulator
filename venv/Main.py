from PIL import Image

triangle = Image.open(r'C:\Users\Admin\Documents\5. Projects\Image_manipulator\venv\triangle.jpeg')

width, height = triangle.size

triangle_resized = triangle.resize((int(width/2), int(height/2)))

triangle = triangle_resized.save('triangle_resized.jpeg')