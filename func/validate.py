def validate(net, device, val_loader):
    """测试函数"""
    import torch
    net.eval()  # 测试，需关闭dropout
    correct = 0
    total = 0
    with torch.no_grad():
        for data in val_loader:
            images, labels = data
            images, labels = images.to(device), labels.to(device)
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print('测试图像的网络精度: %d %%' %
          (100 * correct / total))