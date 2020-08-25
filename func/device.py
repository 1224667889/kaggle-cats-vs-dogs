def device():
    """自动选择训练模式，尽可能使用GPU进行运算"""
    import torch
    if torch.cuda.is_available():
        return torch.device('cuda:0')
    else:
        return torch.device('cpu')