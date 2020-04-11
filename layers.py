import csv
import keras
import matplotlib.pyplot as plt
from keras.models import Sequential

from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD, Adam, RMSprop

import h5py
from keras.utils import plot_model

import numpy as np





# load pima indians dataset
# dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
X = []
Y = []

# Load dataset
path = '/home/dxf/Documents/dataset2.csv'
with open(path, 'r', newline='', encoding='utf-8') as f:
    readers = csv.reader(f)
    for row in readers:
        # Split into input (X) and output (Y) variables
        x0 = row[0]
        X.append(x0)
        y0 = row[1]
        Y.append(y0)

# print(len(X))
# print(len(Y))

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)





# Create model
model = Sequential()

model.add(Dense(32, activation='tanh', input_dim=1))
# prevent overfitting
# model.add(Dropout(0.5))

model.add(Dense(16, activation='tanh'))
model.add(Dense(16, activation='tanh'))
model.add(Dense(16, activation='tanh'))
# model.add(Dropout(0.5))
model.add(Dense(1))

model.summary()

# Compile model
model.compile(loss='mse', optimizer='sgd', metrics=['acc'])

# Fit the model
hist = model.fit(np.array(x_train), np.array(y_train), epochs=20, batch_size=64, verbose=1, validation_split=0.2, shuffle=False)

# Save model
#model.save('regression_model.h5')


# Plot
plt.figure()

acc = hist.history['acc']
val_acc = hist.history['val_acc']
loss = hist.history['loss']
val_loss = hist.history['val_loss']

epochs = range(len(acc))





plt.plot(epochs, loss, 'bo', label='Training loss-5')
plt.plot(epochs, val_loss, 'b', label='Validation loss-5')


# another acti func


# Create model
model = Sequential()

model.add(Dense(32, activation='tanh', input_dim=1))
# prevent overfitting
# model.add(Dropout(0.5))
model.add(Dense(16, activation='tanh'))

model.add(Dense(16, activation='tanh'))
# model.add(Dropout(0.5))
model.add(Dense(1))

model.summary()

# Compile model
model.compile(loss='mse', optimizer='sgd', metrics=['acc'])

# Fit the model
hist = model.fit(np.array(x_train), np.array(y_train), epochs=20, batch_size=64, verbose=1, validation_split=0.2, shuffle=False)

# Save model
#model.save('regression_model.h5')


# Plot


acc = hist.history['acc']
val_acc = hist.history['val_acc']
loss = hist.history['loss']
val_loss = hist.history['val_loss']

epochs = range(len(acc))


plt.plot(epochs, loss, 'go', label='Training loss-4')
plt.plot(epochs, val_loss, 'g', label='Validation loss-4')



# aanother acti func


# Create model
model = Sequential()

model.add(Dense(32, activation='tanh', input_dim=1))
# prevent overfitting
# model.add(Dropout(0.5))
model.add(Dense(16, activation='tanh'))
# model.add(Dropout(0.5))
model.add(Dense(1))

model.summary()

# Compile model
model.compile(loss='mse', optimizer='sgd', metrics=['acc'])

# Fit the model
hist = model.fit(np.array(x_train), np.array(y_train), epochs=20, batch_size=64, verbose=1, validation_split=0.2, shuffle=False)

# Save model
#model.save('regression_model.h5')


# Plot


acc = hist.history['acc']
val_acc = hist.history['val_acc']
loss = hist.history['loss']
val_loss = hist.history['val_loss']

epochs = range(len(acc))


plt.plot(epochs, loss, 'ro', label='Training loss-3')
plt.plot(epochs, val_loss, 'r', label='Validation loss-3')

plt.title('Training and validation loss at 3,4,5 layers')
plt.legend()

plt.show()

'''
# evaluate the model
scores = model.evaluate(x_test, y_test, verbose=0)

print(scores)

print('Test loss', scores[0])
print('Test accuracy', scores[1])
'''



