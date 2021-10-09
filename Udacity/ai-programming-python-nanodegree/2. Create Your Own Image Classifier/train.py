from collections import OrderedDict
import torch
from torch import optim
import torch.nn as nn
from torchvision import transforms, datasets, models
import argparse


def load_data():
    data_dir = 'flowers'
    train_dir = data_dir + '/train'
    valid_dir = data_dir + '/valid'
    test_dir = data_dir + '/test'
    
    train_transforms = transforms.Compose([transforms.Resize(255),
                                    transforms.CenterCrop(224),
                                    transforms.RandomHorizontalFlip(),
                                    transforms.ToTensor(),
                                    transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])])

    valid_transforms = transforms.Compose([transforms.Resize(255),
                                    transforms.CenterCrop(224),
                                    transforms.ToTensor(),
                                    transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])])

    test_transforms = transforms.Compose([transforms.Resize(255),
                                    transforms.CenterCrop(224),
                                    transforms.ToTensor(),
                                    transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])])

    train_data = datasets.ImageFolder(train_dir, transform=train_transforms)
    valid_data = datasets.ImageFolder(valid_dir, transform=train_transforms)
    test_data = datasets.ImageFolder(test_dir, transform=train_transforms)

    trainloader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)
    validloader = torch.utils.data.DataLoader(valid_data, batch_size=64)
    testloader = torch.utils.data.DataLoader(test_data, batch_size=64)
    return trainloader, validloader, testloader

def Classifier(arch="vgg16", dropout=0.5, hidden_layer=1024):
    model = models.vgg16(pretrained=True)
    input_size = 25088

    for param in model.parameters():
        param.requires_grad = False

    my_classifier = nn.Sequential(
        OrderedDict(
            [
                ("dropout", nn.Dropout(0.5)),
                ("fc1", nn.Linear(input_size, 1024)),
                ("relu1", nn.ReLU()),
                ("fc2", nn.Linear(1024, 256)),
                ("output", nn.Linear(256, 102)),
                ("softmax", nn.LogSoftmax(dim=1)),
            ]
        )
    )

    model.classifier = my_classifier

    return model


model = Classifier()


def validation(model, testloader, criterion, device='cuda'):
    # TODO: Do validation on the test set
    correct = 0
    total = 0
    model.to('cuda')
    with torch.no_grad():
        for inputs, labels in testloader:
            inputs, labels = inputs.to('cuda'), labels.to('cuda')
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    accuracy = 100 * correct / total
    print('Accuracy: %d %%' % (accuracy))
    return accuracy


def train_model(model, trainloader, validloader, validation, epochs, arch, lr):
    #Train the classifier layers using backpropagation using the pre-trained network to get the features
    steps = 0
    print_every = 40
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.classifier.parameters())


    #Setting to gpu per user input
    model.to('cuda')

    #Beginning epoch passes
    for e in range(epochs):
        running_loss = 0

        for images, labels in trainloader:
            steps += 1

            #Moving images / labels to GPU per user input

            images, labels = images.to('cuda'), labels.to('cuda')

            #Zero-ing out the optimizer's gradient
            optimizer.zero_grad()

            #Calculating loss and updating weights
            outputs = model.forward(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            #Adjusting running loss
            running_loss += loss.item()

            #Calculating validation loss & accuracy every 20 steps
            if steps % print_every == 0:
                #Moving model to eval mode
                model.eval()

                val_loss = 0
                accuracy = 0

                #Calculating validation loss & accuracy
                for val_images, val_labels in validloader:

                    #Moving to GPU per user input
                    val_images, val_labels = val_images.to('cuda'), val_labels.to('cuda')

                    #Turning off gradient for validation purposes
                    with torch.no_grad():
                        val_outputs = model.forward(val_images)
                        val_loss = criterion(val_outputs, val_labels)

                        #Calculating probability from the val_outputs
                        ps = torch.exp(val_outputs)
                        top_p, top_class = ps.topk(1, dim = 1)
                        equals = top_class == val_labels.view(*top_class.shape)
                        accuracy += torch.mean(equals.type(torch.FloatTensor))

                #Printing out our metrics along the way
                print('Epoch: {} / {}..'.format(e + 1, epochs),
                      'Training Loss: {:.3f}..'.format(running_loss / print_every),
                      'Validation Loss: {:.3f}..'.format(val_loss / len(validloader)),
                      'Validation Accuracy: {:.3f}..'.format(accuracy / len(validloader)))

                running_loss = 0
    return model



def mk_checkpoint(model, arch):
    checkpoint = {'architecture': arch,
                 'classifier': model.classifier,
                 'state_dict': model.state_dict()}
    return checkpoint


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train a model')
    parser.add_argument('data')
    parser.add_argument('--arch', default="vgg16")
    parser.add_argument('--learning_rate', default="0.001", type=float)
    parser.add_argument('--epochs',default=3,type=int)
    parser.add_argument('--gpu',default=False, action="store_true")
    args = parser.parse_args()

    arch = args.arch
    lr = args.learning_rate
    epochs = args.epochs
    device = 'cuda'

    trainloader, validloader, testloader = load_data()
    model = Classifier()
    model = train_model(model, trainloader, validloader,validation, epochs, arch, lr)
    checkpoint = mk_checkpoint(model, arch)

    torch.save(checkpoint, 'checkpoint.pth')