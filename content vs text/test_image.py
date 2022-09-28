import requests

get_image_link = requests.get("https://media.istockphoto.com/photos/imge-of-mint-picture-id618734380")

with open('f1.txt', 'w') as f1:
	f1.write(get_image_link.text)

with open('f2.txt', 'wb') as f2:
        f2.write(get_image_link.content)

