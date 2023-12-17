import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout

# 載入手寫資料庫 (MNIST)
# from keras.datasets import mnist
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# 載入圖像資料庫 (包含以下類別: ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck'])
from keras.datasets import cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# 資料預處理
# 除以255 -> 標準化
x_train = x_train.reshape(50000, 1024, 3).astype('float32')/255
x_test = x_test.reshape(10000, 1024, 3).astype('float32')/255
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

# 建構神經網路
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=(1024, 3)),   # 或是全部改為(32, 32, 3)
    keras.layers.Dense(128, activation='relu'), 
    keras.layers.Dropout(0.2), 
    keras.layers.Dense(10, activation='softmax')
])

# 設定損失函數、優化器和評估指標
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

# 訓練神經網路
history = model.fit(x_train, y_train, batch_size=32, epochs=10, verbose=1, validation_data=(x_test, y_test))

# 評估訓練結果
score = model.evaluate(x_test, y_test, verbose=0)
print ('Test loss:', score[0], 'Test accuracy:', score[1])

# 繪製損失變化圖
import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# 繪製準確率變化圖
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()