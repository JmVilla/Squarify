from PIL import Image

mission_number = raw_input("What mission_id is this for? ").strip()

image_loop = 0

while image_loop == 0:
	orig_img = raw_input("Copy and paste your image (ext included) here. If you are done adding images, type 'done': ").strip()
	print orig_img
	if orig_img == 'done':
		image_loop = 1
	else: 
		im = Image.open(orig_img)
		(im_width, im_height) = im.size
		print im.size
		final_dimension = max(im.size)
		final_image = Image.new('RGB',[final_dimension,final_dimension],'white')
		
		mask = im if im.mode == 'RGBA' else None

		final_image.paste(im,(((final_dimension/2)-(im_width/2)),((final_dimension/2)-(im_height/2))),mask)

		final_image.save(mission_number+'_'+orig_img)

im.close()

# x = (z/2) - (y/2)
# x = distance between image and background edges
# y = width of image
# z = total image width



