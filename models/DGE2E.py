import numpy as np
import pandas as pd
import scispacy
import spacy
import torch
from torch import nn
from transformers import BertModel
import dgl
import Config
from .utils import RelGraphConvLayer, RelEdgeLayer, Attention


class DGE2E_Encoder(nn.Module):
    def __init__(self,Config):
        self.config = Config
        self.bio_bert = BertModel.from_pretrained(self.config.bio_bert_path)
        self.dropout = nn.Dropout(self.config.dropout)


    def encde(self):
        pass


    def forward(self):
        pass


class DGE2E_Decoder(nn.Moudle):
    def __int__(self):
        self.cell = nn.RNNCell()



    def decoe(self):
        pass

    def forward(self):
        pass



class Dynamic_Graph_Generator(nn.Module):
    def __init__(self, entity_ls, G_s):
        pass

    def forward(self):
        pass



class Attetntion(nn.Module):
    def __init__(self):
        pass

    def forward(self):
        pass