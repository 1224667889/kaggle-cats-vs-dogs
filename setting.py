"""调整设置"""
input_size = 224    # 裁剪图片大小
batch_size = 128    # 一次训练所选取的样本数(直接影响到GPU内存的使用情况)
save_path = './weights.pt'  # 训练参数储存地址
lr = 1e-3             # 学习率
n_epoch = 10          # 训练次数