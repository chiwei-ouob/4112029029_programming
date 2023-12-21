from keras.datasets import cifar10
from keras.layers import Dense, Dropout, Flatten, Activation
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential, load_model
from keras.utils import to_categorical
from keras.utils import plot_model
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

# 載入資料
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# 資料預處理
# 卷積層 (Conv) 接受四軸維陣列(即須四個參數): (batch_size, 垂直像素數, 水平像素數, 色彩通道數 -> 1為灰階 3為rgb彩色)
# CIFAR10 資料庫的資料為四維陣列，故無需轉換
x_train = x_train.reshape(-1, 32, 32, 3)/255
x_test = x_test.reshape(-1, 32, 32, 3)/255
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
'''----------------------------------------------------------------'''
model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# 訓練模型
model.fit(x_train, y_train, batch_size=128, epochs=20, verbose=1)
'''----------------------------------------------------------------'''

# 查看結果
scores = model.evaluate(x_test, y_test, verbose=1)
print ('Test loss:', scores[0])
print ('Test accuracy:', scores[1])

# 查看前十筆測試結果
pred = np.argmax(model.predict(x_test[:10]), axis=1)
print (pred)

# 查看前十張圖片
for i in range(10): 
  plt.subplot(2, 5, i+1)
  plt.imshow(x_test[i])
plt.suptitle("The first ten of the test data")
plt.show()