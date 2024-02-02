import Torch.nn as nn
import torchvisions.transforms as transforms
mean_gray=0.1307      # no.of input channels
stadev_gray=0.3081
transforms=transform.Compose[transform.ToTensor(),transform.Normalize((mean-gray),(stddev.gray))]
train_dataset=datasets.MNIST(root='./data',train=TRUE,transform=transforms)
test_dataset=datasets.MNIST(root='./data',train=FALSE,transform=transforms)
#visualization and loading the dataset
import matplotlib pyplot as plt
#denormalization
random_img=train_dataset[20][0]numpy*stddevgray+mean_gray
plt.imshow(random_img.reshape(28,28),cmap='gray')
batch_size=100
train_load=torch.utils.data.Dataloader(dataset=train_dataset,batch_size=batch.size,shuffle=True)
test_load=torch.utils.data.Dataloader(dataset=test_dataset,batch_size=batch.size,shuffle=False)
len(train_dataset)
len(test_dataset)