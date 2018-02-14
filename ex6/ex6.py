##########################################################
# file : ex6.py
# writer : Nadav vitri , nadav.vitri , 203819909
# EXERCISE : intro2cs ex6 2016-2017
# DESCRIPTION: This program contain different function that together take image
# and a list of tiles and create a photomasaic picture.
# after running the code the photomasaic image will show up and also will saved
# this in the original image folder.
##########################################################
import mosaic
import sys
import copy

INDEX_0 = 0
INDEX_1 = 1
INDEX_2 = 2
INDEX_3 = 3
INDEX_4 = 4
INDEX_5 = 5
MAIN = "__main__"
NUMBER_OF_ARGUMENTS = 5
NUMBER_1 = 1
ERROR_MESSAGE ="Wrong number of parameters. The correct usage is: /" \
               "ex6.py<image_source><image_dir><output_name>" \
               "<tile_height><num_candidates>"

def compare_pixel(pixel1, pixel2):
    """this function receive two pixel (tuple of 3 numbers) and calculate and
    return the distance between these pixles(absolute value)"""
    total_sum = 0
    for i in range(3):
        total_sum += abs(pixel1[i] - pixel2[i])
    return total_sum


def compare(image1, image2):
    """this function receive two image (list of lists) and compare the distance
    between them by calculating the pixels with compare_pixel function and
    return the total sum distance between every pixels"""
    length = min(len(image1), len(image2))  # if one of the image bigger
    width = min(len(image1[INDEX_0]), len(image2[INDEX_0]))
    total_compare = 0
    for lst in range(length):
        for i in range(width):
            total_compare += compare_pixel(image1[lst][i], image2[lst][i])
    return total_compare


def get_piece(image, upper_left, size):
    """this function receive image,place(pixel) to start the "cutting"
    and size for piece from the image. the function take a piece from the image
    by copy (the chosen place to start the cutting and the chosen size) to
    new list and return that list"""
    row, column = upper_left
    min_width = min(size[INDEX_1],len(image[INDEX_0]) - column) #the piece have
    min_height = min(size[INDEX_0],len(image) - row) #to be part from the image!
    new_image = []
    for i in range(min_height):
        new_image.append(image[row + i][column: column + min_width])
    return new_image


def set_piece(image, upper_left, piece):
    """this function replace specific piece from the image and set in instead
    of that with another piece. the function receive image, place to start
    the setting and a piece that will replace the piece of the image. the
    function only change the image and not return somthing!"""
    row, column = upper_left
    min_width = min(len(piece[INDEX_0]), len(image[INDEX_0]) - column)
    min_height = min(len(piece), len(image) - row)
    for i in range(min_height):
        for j in range(min_width):
            image[row + i][column + j] = piece[i][j]


def average(image):
    """this function receive image and return the average of the pixels in
    the image. the function return tuple like (R,G,B) that every part of the
    tuple is the average of this color in the image"""
    total_red = 0
    total_green = 0
    total_blue = 0
    total_pixels = len(image)*(len(image[INDEX_0]))
    for row in image:
        for i in row:
            total_red += i[INDEX_0]
            total_green += i[INDEX_1]
            total_blue += i[INDEX_2]
    return (total_red/total_pixels, total_green/total_pixels,
            total_blue / total_pixels)


def preprocess_tiles(tiles):
    """this function receive list of tiles and return the average of the colors
    for every tile in that list"""
    tiles_average = []
    for tile in tiles:
        tiles_average.append(average(tile))
    return tiles_average


def get_best_tiles(objective, tiles, averages , num_candidates):
    """this function return the most similar tiles (from list of tiles) to the
    image (objective).the function receive image,list of tiles,the average of
    the color for every tile and the number for the returning tile, and
    calculate the distance for every tile and return the tiles that there
    average is the most similar to the image"""
    image_average = average(objective)
    image_tile_compare = []
    final_candidate = []
    for tile in averages:
        image_tile_compare.append(compare_pixel(image_average, tile))
    candidates = sorted(image_tile_compare)
    for i in range(num_candidates):
        if candidates[i] in image_tile_compare:
            final_candidate.append(tiles
                                   [image_tile_compare.index(candidates[i])])
    return final_candidate


def choose_tile(piece, tiles):
    """this function choose the best tile (the tile that the distance from the
    original image is the closer) from a list of tiles."""
    tiles_distance = []
    for tile in tiles:
        tiles_distance.append(compare(tile,piece))
    best = min(tiles_distance)
    return tiles[tiles_distance.index(best)]


def make_mosaic(image, tiles, num_candidates):
    """this fucntion make a photomasaic picture by using the function before.
    the function recive image,tiles and the number to choose tile from the
    list of the tiles.first the function copy the image and after that take a
    piece from the image and set the chosen tiles for that piece(by pick
    the best tiles for that piece with the 'get_best_tiles' and 'choose_tiles'
    function)."""
    new_image = copy.deepcopy(image)
    width = len(tiles[INDEX_0][INDEX_0])
    height = len(tiles[INDEX_0])
    tiles_average = preprocess_tiles(tiles)
    for j in range(0,len(image), height):
        for i in range(0, len(image[INDEX_0]), width):
            piece = get_piece(new_image, (j, i), (height, width))
            good_tiles = get_best_tiles(piece, tiles,
                                        tiles_average, num_candidates)
            set_piece(new_image, (j, i), choose_tile(piece, good_tiles))
    return new_image


def main(image_source, image_dir, output_name, tile_height, num_candidates):
    """this function receive the image file, the folder for the image,
    name for the photomasaic, the tile height and the number candidates."""
    tiles = mosaic.build_tile_base(image_dir, tile_height)
    original_image = mosaic.load_image(image_source)
    mosaic_image = make_mosaic(original_image, tiles, num_candidates)
    mosaic.save(mosaic_image, output_name)


if __name__ == MAIN:
    if len(sys.argv) == NUMBER_OF_ARGUMENTS + NUMBER_1:
        ex6 = sys.argv[INDEX_0]
        image_source = sys.argv[INDEX_1]
        image_dir = sys.argv[INDEX_2]
        output_name = sys.argv[INDEX_3]
        tile_height = int(sys.argv[INDEX_4])
        num_candidates = int(sys.argv[INDEX_5])
        main(image_source, image_dir, output_name, tile_height, num_candidates)
    else:
        print(ERROR_MESSAGE)