import cv2 as cv

def save_array_as_ppm(array, output_path):
    """
    Save a 2D list (array) containing RGB color information as a PPM image.
    
    Parameters:
        array (list): Input array containing color information.
        output_path (str): Path to save the PPM file.
    """
    height = len(array)
    width = len(array[0])

    # Write PPM header
    with open(output_path, 'w') as f:
        f.write("P3\n")
        f.write(f"{width} {height}\n")
        f.write("255\n")

        # Write pixel values
        for row in array:
            for pixel in row:
                f.write(" ".join(str(value) for value in pixel) + "\n")

    print(f"Image saved as {output_path}")
    saveAsPng(output_path)

def saveAsPng(name):
    i = cv.imread(name)
    cv.imwrite(name + ".png",i)

def generateEmptyImage(r, g, b, width, height):
    
    collumns = []

    for j in range(height):
        row = []
        for i in range(width):
            row.append([r, g, b])
            
        collumns.append(row)
    return collumns

def write_pixel(image_array, x, y, color):
    """
    Write a color to a specified position in the image array.
    
    Parameters:
        image_array (list): 3D list representing the image array.
        x (int): X coordinate of the pixel.
        y (int): Y coordinate of the pixel.
        color (tuple): RGB color tuple.
    """
    image_array[y][x] = color


