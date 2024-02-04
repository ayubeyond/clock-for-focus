# 导入相关的库
import jieba
import pandas as pd
import numpy as np

# 读取对联数据集
data = pd.read_csv('couplet.csv')
upper = data['upper'].tolist()
lower = data['lower'].tolist()

# 定义一个函数，输入上联，输出下联
def generate_couplet(upper_couplet):
  # 使用jieba分词对上联进行分词
  upper_words = list(jieba.cut(upper_couplet))
  # 初始化一个空的下联词语列表
  lower_words = []
  # 遍历上联词语列表
  for word in upper_words:
    # 如果上联词语在数据集中存在
    if word in upper:
      # 找到数据集中对应的下联词语
      lower_word = lower[upper.index(word)]
    # 如果上联词语在数据集中不存在
    else:
      # 随机选择一个同音或同韵的词语
      lower_word = np.random.choice(list(jieba.cut(word)))
    # 将下联词语添加到下联词语列表中
    lower_words.append(lower_word)
  # 将下联词语列表拼接成一句完整的下联
  lower_couplet = ''.join(lower_words)
  # 返回结果
  return lower_couplet
