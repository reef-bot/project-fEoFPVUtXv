# machine_learning.py

import tensorflow as tf

class MachineLearningModel:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def train_model(self, X_train, y_train):
        self.model.fit(X_train, y_train, epochs=10, batch_size=32)

    def predict(self, X):
        return self.model.predict(X)

# End of machine_learning.py