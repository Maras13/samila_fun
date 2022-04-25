import imageio
import os

files = os.listdir('images')


#combine multiple images in a gif

image_path = [os.path.join('images', file)for file in files]

images = []
for img in image_path:
     if img.endswith('.png'):
            try:
                images.append(imageio.imread(img))
            
            except (IOError, SyntaxError) as e:
                print('Bad file:', img)

imageio.mimwrite('output/giff2.gif', images, fps=6)
            
