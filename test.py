def test():
    from PIL import Image
    import torch
    from torchvision import models
    from torch import nn
    from setting import input_size, save_path
    from torchvision import transforms

    # ------------------------ 加载数据 --------------------------- #
    # 定义预训练变换
    transform_val = transforms.Compose([
        transforms.Resize([input_size, input_size]),  # 注意 Resize 参数是 2 维，和 RandomResizedCrop 不同
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])

    class_names = ['0', '180', '270', '90']  # 这个顺序很重要，要和训练时候的类名顺序一致

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # ------------------------ 载入模型并且训练 --------------------------- #
    transfer_model = models.resnet18(pretrained=True)
    for param in transfer_model.parameters():
        param.requires_grad = False
    dim = transfer_model.fc.in_features
    transfer_model.fc = nn.Linear(dim, 2)
    # 构建神经网络
    net = transfer_model.to(device)
    net.load_state_dict(torch.load(save_path))
    net.eval()

    image_PIL = Image.open(r'test/image')

    image_tensor = transform_val(image_PIL)
    # 以下语句等效于 image_tensor = torch.unsqueeze(image_tensor, 0)
    image_tensor.unsqueeze_(0)
    # 没有这句话会报错
    image_tensor = image_tensor.to(device)

    out = net(image_tensor)
    # 得到预测结果，并且从大到小排序
    _, indices = torch.sort(out, descending=True)
    # 返回每个预测值的百分数
    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

    if percentage[0] > percentage[1]:
        out = '此图片有{:>4.1f}%可能是只猫'.format(percentage[0])
    else:
        out = '此图片有{:>4.1f}%可能是只狗'.format(percentage[1])

    return out
