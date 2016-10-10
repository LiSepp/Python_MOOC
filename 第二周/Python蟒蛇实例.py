#Python蟒蛇实例
import turtle
#
def drawSnake(rad, angle, len, neckrad):
	for i in range(len):
		turtle.circle(rad, angle)		#使蟒蛇沿圆形移动，rad描述轨迹半径，angle表示沿圆爬行的弧度值
		turtle.circle(-rad, angle)
	turtle.circle(rad, angle / 2)
	turtle.fd(rad)						#表示向前直线爬行
	turtle.circle(neckrad + 1, 180)
	turtle.fd(rad*2/3)

def main():								#先运行main()函数
	turtle.setup(1300, 800, 0, 0)		#启动一个长宽（1300，800）的窗口，起始点为（0,0）
	pythonsize = 30						#这两句设定运行轨迹的宽度，设为30个像素
	turtle.pensize(pythonsize)
	turtle.pencolor("blue")				#设置颜色
	turtle.seth(-40)					#设置角度，0表示向东，90表示向北，180向西，270向南，负值表示相反的方向
	drawSnake(40,80,5,pythonsize/2)		

main()
