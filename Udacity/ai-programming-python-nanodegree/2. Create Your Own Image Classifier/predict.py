import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from collections import OrderedDict
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms, datasets, models
import json
import argparse


def load_checkpoint(filename):
    checkpoint = torch.load(filename)

    model = models.vgg16(pretrained=True)

    for param in model.parameters():
        param.requires_grad = False

    model.classifier = checkpoint["classifier"]
    model.load_state_dict(checkpoint["state_dict"])
    return model

from PIL import Image

def process_image(image):
    img = Image.open(image)

    prepoceess = transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    # TODO: Process a PIL image for use in a PyTorch model
    model = prepoceess(img)
    return model

def predict(image_path, model, topk, category_names,
            device='cuda'):
    model.to('cuda')
    model.eval()
    img = process_image(image_path)
    img = img.numpy()
    img = torch.from_numpy(np.array([img])).float()

    with torch.no_grad():
        output = model.forward(img.cuda())
        
    probability = torch.exp(output).data
    
    return probability.topk(topk)

    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_path')
    parser.add_argument('checkpoint', default = "checkpoint.pth")
    parser.add_argument('--top_k', default = 5)
    parser.add_argument('--category_names', default = '/home/workspace/aipnd-project/cat_to_name.json')
    parser.add_argument('--gpu', default = True,action="store_true")
    args = parser.parse_args()
    
    topk = args.top_k
    category_names = args.category_names
    device = 'cuda'
    
    model = load_checkpoint(filename=args.checkpoint)
    prediction = predict(args.image_path, model, topk,
                             category_names=category_names, device=device)
    print(prediction)