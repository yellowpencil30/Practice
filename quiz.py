import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

# 모델 설계
model = Sequential([
    # 항상 이 순서인가?
    Flatten(input_shape =(28, 28)),
    Dense(128, activation = 'relu'),
    # 은닉층과 출력층을 따로 구분할 필요가 없는가? 그러면 하나 더 추가해도 됨?
    Dense(10, activation = 'softmax')
])

# 모델 설정
model.compile(optimizer='adam',
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])

print('모델 학습을 시작합니다')
history = model.fit(x_train, y_train, epochs=5, validation_split=0.2)
print('모델 학습이 완료되었습니다.')

plt.plot(history.history['accuracy'], label = 'Training Accuracy')
plt.plot(history.history['val_accuracy'], label = 'Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

predictions = model.predict(x_test)
predicted_label = tf.argmax(predictions[3]).numpy()
true_label = y_test[3]

print(f"\n모델의 예측: {predicted_label}")
print(f"실제 정답: {true_label}")

plt.imshow(x_test[3], cmap='gray')
plt.title(f"Predicted: {predicted_label}, True: {true_label}")
plt.show()