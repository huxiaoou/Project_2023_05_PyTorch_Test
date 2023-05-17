import torch

x = torch.rand(5, 3)

print(x)

if torch.cuda.is_available():
    print("cuda is available")
else:
    print("cuda is not available")
