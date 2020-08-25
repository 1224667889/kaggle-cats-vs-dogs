def get_address():
    """返回狗地址列表、猫地址列表、工作目录"""
    import os
    print('{:-^30}'.format('数据集'))
    data_file = os.listdir('./train/')
    print('图片或文件数量:', str(len(data_file)))  # 25000
    dog_file = list(filter(lambda x: x[:3] == 'dog', data_file))
    cat_file = list(filter(lambda x: x[:3] == 'cat', data_file))
    print('狗:', str(len(dog_file)), '\n猫:', str(len(cat_file)))  # 狗:12500 猫:12500
    root = os.getcwd()
    print('工作目录:', root)    # 工作目录: L:\kaggle
    print('{:-^30}'.format(''))
    return dog_file, cat_file, root