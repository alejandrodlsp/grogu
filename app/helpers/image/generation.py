from PIL import Image, ImageFont, ImageDraw
import textwrap
import uuid
import os

class ImageText():
    def __init__(self, image_path, text, pos, width, fontSize = 50, color = (0,0,0)):
        self.image_path = image_path
        self.text = text
        self.x = pos[0]
        self.y = pos[1]
        self.width = width
        self.color = color
        
        self.fontSize = fontSize
        self.font = ImageFont.truetype("resources/fonts/NotoSans-VariableFont_wdth,wght.ttf", self.fontSize)
        
        filename = str(uuid.uuid4())
        self.generation_path = f"tmp/{filename}.jpg"
        
    def generate(self):
        image = Image.open(self.image_path)
        draw = ImageDraw.Draw(image)
        
        text_lines =  textwrap.wrap(self.text, width=self.width)
        
        text_bb = self.font.getbbox(self.text)
        y_lines_offset = (len(text_lines) * (text_bb[1] - text_bb[3])) / 2 # number of lines * height of a line  / 2
        
        ypos = self.y + y_lines_offset
        for line in text_lines:
            line_bb = self.font.getbbox(line)
            line_height = line_bb[1] - line_bb[3]
            line_width = self.font.getlength(line)
            
            xpos = self.x - (line_width/2)   
            draw.text(
                    (xpos, ypos),
                    line,
                    self.color,
                    font=self.font
                )
            ypos -= line_height
    
        image.save(self.generation_path)
        return self.generation_path
    
    def purge(self):
        os.remove(self.generation_path)