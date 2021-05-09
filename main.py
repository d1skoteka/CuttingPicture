from PIL import Image

img = Image.open("exempel.jpg")

red_img, green_img, blue_img = img.split()

value_cut_left = 200
max_width = 80
max_height = 70

trim_coords_two_sides = (0, 0, img.width-value_cut_left, img.height)

right_side_crop_coords = (0, 0, img.width - value_cut_left, img.height)
blue_crop = blue_img.crop(right_side_crop_coords)
both_sides_blue_crop = blue_img.crop(trim_coords_two_sides)
blue_img_final = Image.blend(blue_crop,both_sides_blue_crop, 0.5)

left_side_crop_coords = (value_cut_left, 0, img.width, img.height)
red_monro_crop = red_img.crop(left_side_crop_coords)
both_sides_blue_crop = red_img.crop(trim_coords_two_sides)
red_img_final = Image.blend(red_monro_crop, both_sides_blue_crop, 0.5)

green_img_final = green_img.crop(trim_coords_two_sides)

final_img = Image.merge("RGB",(red_img_final, green_img_final, blue_img_final))
final_img.save("new_image.jpg")

final_img.thumbnail((max_width, max_height))
final_img.save("final_image.jpg")
