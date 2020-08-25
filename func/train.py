def train(net, optimizer, device, criterion, train_loader):
    """训练"""
    net.train()
    batch_num = len(train_loader)
    running_loss = 0.0
    for i, data in enumerate(train_loader, start=1):
        # 将输入传入GPU
        inputs, labels = data
        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # 计算误差并显示
        running_loss += loss.item()
        if i % 10 == 0:
            print('batch:{}/{} loss:{:.3f}'.format(i, batch_num, running_loss / 20))
            running_loss = 0.0