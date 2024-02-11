from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64

def generateIdCard(user_info: dict) -> None:
    with Image.open('assets/id_card_front.png') as im:
        im.load()
        face_image = Image.open(BytesIO(base64.b64decode(user_info['image'].replace('data:image/png;base64,', ''))))
        face_image = face_image.resize((230,305))
        im.paste(face_image, (623, 200))
        draw = ImageDraw.Draw(im)
        draw.text((200,182),user_info['ten_day_du'], fill=(0,0,0),font=ImageFont.truetype("arial.ttf", 30))
        draw.text((200,182 + 67),user_info['ma_sv'], fill=(0,0,0),font=ImageFont.truetype("arial.ttf", 30))
        draw.text((200,182 + 67 * 2),user_info['lop'], fill=(0,0,0),font=ImageFont.truetype("arial.ttf", 30))
        draw.text((200,182 + 67 * 3),user_info['ngay_sinh'], fill=(0,0,0),font=ImageFont.truetype("arial.ttf", 30))
        draw.text((200,182 + 67 * 4),user_info['nganh'], fill=(0,0,0),font=ImageFont.truetype("arial.ttf", 30))
        im.save('info.png')