def arrange():
    """整理数据，移动图片位置"""
    import shutil
    import os
    from .get_address import get_address
    dog_file, cat_file, root = get_address()

    print('开始数据整理')
    # 新建文件夹
    for i in ['dog', 'cat']:
        for j in ['train', 'val']:
            try:
                os.makedirs(os.path.join(root,j,i))
            except FileExistsError as e:
                pass

    # 移动10%(1250)的狗图到验证集
    for i, file in enumerate(dog_file):
        ori_path = os.path.join(root, 'train', file)
        if i < 0.9*len(dog_file):
            des_path = os.path.join(root, 'train', 'dog')
        else:
            des_path = os.path.join(root, 'val', 'dog')
        shutil.move(ori_path, des_path)

    # 移动10%(1250)的猫图到验证集
    for i, file in enumerate(cat_file):
        ori_path = os.path.join(root, 'train', file)
        if i < 0.9*len(cat_file):
            des_path = os.path.join(root, 'train', 'cat')
        else:
            des_path = os.path.join(root, 'val', 'cat')
        shutil.move(ori_path, des_path)

    print('数据整理完成')