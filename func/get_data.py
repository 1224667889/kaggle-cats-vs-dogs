def get_data(input_size, batch_size):
    """获取文件数据并转换"""
    from torchvision import transforms
    from torchvision.datasets import ImageFolder
    from torch.utils.data import DataLoader

    # 串联多个图片变换的操作（训练集）
    # transforms.RandomResizedCrop(input_size) 先随机采集，然后对裁剪得到的图像缩放为同一大小
    # RandomHorizontalFlip()  以给定的概率随机水平旋转给定的PIL的图像
    # transforms.ToTensor()  将图片转换为Tensor,归一化至[0,1]
    # transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  归一化处理(平均数，标准偏差)
    transform_train = transforms.Compose([
        transforms.RandomResizedCrop(input_size),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    # 获取训练集（通过上面的方面操作）
    train_set = ImageFolder('train', transform=transform_train)
    # 封装训练集
    train_loader = DataLoader(dataset=train_set,
                              batch_size=batch_size,
                              shuffle=True)

    # 串联多个图片变换的操作（验证集）
    transform_val = transforms.Compose([
        transforms.Resize([input_size, input_size]),  # 注意 Resize 参数是 2 维，和 RandomResizedCrop 不同
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    # 获取验证集（通过上面的方面操作）
    val_set = ImageFolder('val', transform=transform_val)
    # 封装验证集
    val_loader = DataLoader(dataset=val_set,
                            batch_size=batch_size,
                            shuffle=False)
    # 输出
    return transform_train, train_set, train_loader, transform_val, val_set, val_loader