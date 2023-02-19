from PIL import Image

page_num = int(input("페이지 수를 입력하세요: "))

image_dir = 'C:/Users/sky11/OneDrive/Desktop/tests/images'
pdf_dir = 'C:/Users/sky11/OneDrive/Desktop/tests/pdf'

img_list = []

img_main = Image.open('%s/page1.png' % image_dir).convert('RGB')

for i in range(2, page_num + 1): 
    img_list.append(Image.open('%s/page%s.png' % (image_dir, i)).convert('RGB'))

img_main.save('%s/test.pdf' % pdf_dir, save_all=True, append_images=img_list)