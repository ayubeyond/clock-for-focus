# 导入random模块
import random

# 生成一个随机的谜语，可以是任何你想要的内容
riddle = random.choice(["什么东西越热越爱出汗？", "什么水永远也喝不完？", "什么东西有头有尾，却没有身体？"])

# 生成一个对应的答案，要和谜语匹配
answer = random.choice(["电饭锅", "口水", "硬币"])

# 设置一个变量，用来记录用户猜了几次
guess_count = 0

# 设置一个变量，用来记录用户是否猜对了
guessed = False

# 显示谜语，提示用户输入答案
print("猜猜看，" + riddle)

# 使用while循环，让用户可以多次猜测，直到猜对或者猜满三次为止
while not guessed and guess_count < 3:
    # 获取用户的输入，转换成小写，去掉空格
    guess = input("你的答案是：").lower().strip()
    # 判断用户的输入是否正确
    if guess == answer:
        # 如果正确，显示恭喜信息，设置guessed为True，跳出循环
        print("恭喜你，猜对了！")
        guessed = True
    else:
        # 如果错误，显示遗憾信息，增加guess_count的值，继续循环
        print("遗憾，猜错了！")
        guess_count += 1

# 如果用户没有在三次内猜对，显示正确答案
if not guessed:
    print("很遗憾，你没有猜出来。正确答案是：" + answer)
