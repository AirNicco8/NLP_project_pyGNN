from tokenizer import Tokenizer
import sys
import pickle

dim = 100000 # !TODO tune this parameter

test_dataset = "output/test_dataset.dats"
train_dataset = "output/train_dataset.dats"
val_dataset = "output/train_dataset.dats"

tok = Tokenizer()
tok.train_from_file(train_dataset, dim)
tok.update_from_file(val_dataset)
tok.update_from_file(test_dataset)
output = 'output/tdats.tok'
tok.save(output)