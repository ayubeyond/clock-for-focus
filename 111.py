# 定义蛇的颜色，大小，初始位置，初始方向等
snake_color = (0, 255, 0) # 绿色
snake_size = 10 # 每个蛇节的边长
snake = [(100, 100), (90, 100), (80, 100)] # 蛇的身体，用一个列表存储每个蛇节的坐标
snake_direction = "right" # 蛇的初始方向

# 定义一个函数，用于画蛇
def draw_snake():
    # 遍历蛇的身体，画出每个蛇节
    for x, y in snake:
        # 用 pygame.draw.rect 函数画一个矩形，表示一个蛇节
        pygame.draw.rect(screen, snake_color, (x, y, snake_size, snake_size))
