import numpy as np
import PIL.Image, PIL.ImageFont, PIL.ImageDraw


def draw_bounding_box_on_image(image, 
                                ymin,
                                xmin,
                                ymax,
                                xmax, 
                                color = 'red', 
                                thickness = 1, 
                                display_str = None, 
                                use_normalized_coordinates = True):
    '''
    Function to draw a bounding box on an image.
    This function takes in the image, bounding box coordinates, color of bounding box, 
    string to be displayed and whether to use normalized coordinates.
    '''
    draw = PIL.ImageDraw.Draw(image)
    im_width, im_height = image.size
    if use_normalized_coordinates:
        (left, right, top, bottom) = (xmin * im_width,
        xmax * im_width, ymin * im_height, ymax * im_height)
    else:
        (left, right, top, bottom) = (xmin, xmax, ymin, ymax)

        draw.line([(left, top), (left, bottom), (right, bottom),
        (right, top), (left, top)], 
        width = thickness, fill = color)




def draw_bounding_boxes_on_image_array(image, boxes, color = [], thickness = 1, display_str_list = []):
    image_pil = PIL.Image.fromarray(image)
    rgbimg = PIL.Image.new('RGBA', image_pil.size)
    rgbimg.paste(image_pil)

    draw_bounding_boxes_on_image(rgbimg, boxes, color, thickness, display_str_list)
    return np.array(rgbimg)


def draw_bounding_boxes_on_image(image, boxes, color = [], thickness = 1, display_str_list = ()):
    boxes_shape = boxes.shape
    if not boxes_shape:
        return
    if len(boxes_shape) != 2 or boxes_shape[1] != 4:
        raise ValueError('Input must be of size [N, 4]')

    for i in range(boxes_shape[0]):
        (draw_bounding_box_on_image(image, boxes[i, 1], 
        boxes[i, 0], boxes[i, 3], boxes[i, 2], color[i], thickness, display_str_list[i]))