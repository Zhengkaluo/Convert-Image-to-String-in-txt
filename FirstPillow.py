#灰度值 指黑白图像中颜色深度，0-255，白色255，黑色0
#RGB gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
from PIL import Image
import argparse #用来管理命令行参数输入

parser = argparse.ArgumentParser()

#定义输入文件，输出文件，输出字符画的宽和高
parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('--width',type = int, default = 80)
parser.add_argument('--height',type = int, default = 80)

#解析获得参数
args = parser.parse_args()

#文件路径
IMG = args.file

#字符画宽度
Width = args.width
Height = args.height

Output = args.output

ascii_char = list("%@B%8&WM#*oahkbdpqwmZO0WLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")

def get_char(r,g,b,alpha = 256):

    if alpha == 0:
        return " "

    length = len(ascii_char)

    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)


    unit = (256.0 + 1)/length

    return ascii_char[int(gray/unit)]


#用PIL image.open 打开文件，用im.resize()调整大小
#提取像素得到rgb值，getchar变成字符，字符拼接成txt
#char = get_char(*im.getpixel((j,i)))
#打印txt

if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((Width, Height), Image.NEAREST)

    #初始化输出的字符串
    txt = ""

    #遍历每一行每一列
    for i in range(Height):
        for j in range(Width):
            #每一个坐标rgb像素变成字符后添加到txt里
            txt += get_char(*im.getpixel((j,i)))
        
        txt += '\n'
    #输出到屏幕
    print(txt)

    #输出到文件

    if Output:
        with open(Output, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)

#执行的时候不用加python