import torch
import torch.nn.functional as F
import torch.nn as nn


# # The recognition net
class TypeRecognitionNet(nn.Module):
    """ Type Recognition Neural Network.

    :param C: number of classes
    :param G: number of features
    :param hidden_size: size of hidden layers
    """

    def __init__(self, C: int, G: int, hidden_size=10) -> None:
        super(TypeRecognitionNet, self).__init__()
        self.hidden_1 = nn.Linear(G, hidden_size)
        self.hidden_2 = nn.Linear(hidden_size, C + 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """One forward pass.

        :param x: the input vector
        :type x: torch.Tensor
        :return: the calculated cost value
        :rtype: torch.Tensor
        """
        x = self.hidden_1(x)
        x = F.relu(x)
        x = self.hidden_2(x)
        x = F.softmax(x, dim=1)
        return x
