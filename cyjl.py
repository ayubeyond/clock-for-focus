import random

# 成语库
idioms = ["井底之蛙", "画龙点睛", "朝三暮四", "滥竽充数"]

# 开始成语接龙
start_idiom = random.choice(idioms)
print("起始成语：" + start_idiom)

# 用户接龙
def find_next_idiom(current_idiom, idioms_list):
    last_char = current_idiom[-1]
    for idiom in idioms_list:
        if idiom.startswith(last_char):
            return idiom
    return "没有找到可以接龙的成语"

# 示例接龙
user_idiom = "数黄道黑"  # 假设用户输入的成语
next_idiom = find_next_idiom(user_idiom, idioms)
print("下一个成语：" + next_idiom)
