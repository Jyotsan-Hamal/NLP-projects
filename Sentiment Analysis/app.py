import re
import torch
from keras.preprocessing.sequence import pad_sequences
import pickle


import torch
from torch import nn
from torch.nn import functional as F


# Check if GPU is available and if not, use CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# Print whether GPU or CPU is being used
print('Using', 'GPU' if device.type == 'cuda' else 'CPU')

max_fatures = 2000
embed_dim = 128
lstm_out = 196


class LSTMNet(nn.Module):
    def __init__(self):
        super(LSTMNet, self).__init__()
        self.embed = nn.Embedding(max_fatures, embed_dim)
        self.dropout = nn.Dropout(0.4)
        self.lstm = nn.LSTM(embed_dim, lstm_out, batch_first=True, dropout=0.2)
        self.dense = nn.Linear(lstm_out, 2)

    def forward(self, x):
        x = self.embed(x)
        x = self.dropout(x)
        lstm_out, _ = self.lstm(x)
        x = self.dense(lstm_out[:, -1, :])
        return F.log_softmax(x, dim=1)


# Load the tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Initialize the model
py_model = LSTMNet()

# Load the model
py_model.load_state_dict(torch.load('sentiment.pth'))

# Move the entire model to the same device as the input tensor
py_model.to(device)
# Your sentence
sentence = "Recession Hit veronique branquinho, she has to quit her company, such a shame!"
sentence = sentence.lower()
sentence = re.sub('[^a-zA-z0-9\s]', '', sentence)

# Tokenize the sentence
sentence = tokenizer.texts_to_sequences(sentence)

# Pad the sequence
sentence = pad_sequences(sentence, maxlen=32)

# Convert to tensor
sentence = torch.tensor(sentence, dtype=torch.long).to(device)

# Get the model's prediction
prediction = py_model(sentence)

# Print the prediction
if torch.argmax(prediction) == 1:
    print("Positive sentiment")
else:
    print("Negative sentiment")
