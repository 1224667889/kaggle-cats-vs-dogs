import torch
from torchvision import models
from torch import nn
import func as f
from setting import input_size, batch_size, save_path, lr, n_epoch

f.arrange()     # 整理数据，移动图片位置(若已经整理完成可注释)

# 获取文件数据并转换成参数集
transform_train, train_set, train_loader, transform_val, val_set, val_loader = f.get_data(input_size, batch_size)
print('映射关系:', train_set.class_to_idx)  # {'cat': 0, 'dog': 1}
print('训练集长度:', len(train_set.imgs))  # 22500
print('训练集规格:', train_set[1][0].size())  # torch.Size([3, 224, 224])


device = f.device()     # 选择训练模式(GPU)
print('训练模式:', device, '模式')
# 残差网络(18指定的是带有权重的18层，包括卷积层和全连接层，不包括池化层和BN层)
# pretrained=True   使用预训练模型
# 使用resnet18模型
transfer_model = models.resnet18(pretrained=True)
for param in transfer_model.parameters():
    # 屏蔽预训练模型的权重，只训练最后一层的全连接的权重
    param.requires_grad = False
# 修改最后一层维数，即 把原来的全连接层 替换成 输出维数为2的全连接层
# 提取fc层中固定的参数
dim = transfer_model.fc.in_features
# 设置网络中的全连接层为2
transfer_model.fc = nn.Linear(dim, 2)
# 构建神经网络
net = transfer_model.to(device)


# 分类问题——交叉熵损失函数
criterion = nn.CrossEntropyLoss()
# 优化器——随机梯度下降
# 学习率lr=10^-3;
optimizer = torch.optim.SGD(net.fc.parameters(), lr=lr)
# optimizer = torch.optim.Adam(net.parameters(), lr=lr)
for epoch in range(n_epoch):
    print('第{}次训练'.format(epoch+1))
    f.train(net, optimizer, device, criterion, train_loader)
    f.validate(net, device, val_loader)

# 仅保存和加载模型参数
torch.save(net.state_dict(), save_path)