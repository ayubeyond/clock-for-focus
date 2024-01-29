# 导入随机模块
import random

# 定义春联的上联和下联的字数
length = 7

# 定义春联的上联和下联的候选字
candidates = "春福喜财祥如意平安吉祥新年好运气贵人旺事业兴家庭和顺"

# 定义春联的横批的候选词
hengpi = ["新春快乐", "恭喜发财", "平安吉祥", "万事如意"]

# 随机生成春联的上联
shanglian = ""
for i in range(length):
    shanglian += random.choice(candidates)

# 随机生成春联的下联
xialian = ""
for i in range(length):
    xialian += random.choice(candidates)

# 随机选择春联的横批
hengpi = random.choice(hengpi)

# 打印春联
print(shanglian)
print(xialian)
print("  " + hengpi)
