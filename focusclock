# 导入time模块
import time
# 定义专注时长（分钟）
focus_time = 25
# 定义休息时长（分钟）
break_time = 5
# 定义循环次数
loop_count = 4
# 定义一个函数，用于显示当前时间和提示信息
def show_time(message):
    # 获取当前时间
    current_time = time.strftime("%H:%M:%S")
    # 打印提示信息和当前时间
    print(message, current_time)
# 开始专注循环
for i in range(loop_count):
    # 显示开始专注的提示
    show_time("开始专注：")
    # 等待专注时长
    time.sleep(focus_time * 60)
    # 显示开始休息的提示
    show_time("开始休息：")
    # 等待休息时长
    time.sleep(break_time * 60)
# 显示专注结束的提示
show_time("专注结束！")
