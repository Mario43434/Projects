from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np

# ✅ Define your custom attention layer first
class attention(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super(attention, self).__init__(**kwargs)

    def build(self, input_shape):
        self.W = self.add_weight(name="att_weight", shape=(input_shape[-1], 1), initializer="random_normal")
        self.b = self.add_weight(name="att_bias", shape=(input_shape[1], 1), initializer="zeros")
        super(attention, self).build(input_shape)

    def call(self, x):
        et = tf.squeeze(tf.tanh(tf.matmul(x, self.W) + self.b), axis=-1)
        at = tf.nn.softmax(et)
        at = tf.expand_dims(at, axis=-1)
        output = x * at
        return tf.reduce_sum(output, axis=1)

    def compute_output_shape(self, input_shape):
        return (input_shape[0], input_shape[-1])

# ✅ Now load the model with custom_objects
model = tf.keras.models.load_model("attention_lstm_model.h5", custom_objects={'attention': attention})

# ✅ Flask app starts here
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.form['features']  # e.g. "0.1,0.5,0.3,..."
    try:
        features = np.array([float(x) for x in input_data.split(',')]).reshape(1, 1, 9)
        prediction = model.predict(features)
        result = "Fraudulent" if prediction[0][0] > 0.5 else "Legitimate"
    except:
        result = "Invalid input. Please enter 9 comma-separated numbers."
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)

# Define the features used during training
selected_features = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'Amount']

# Select a few non-fraudulent transaction IDs
sample_ids = df[df['Class'] == 0].index[:5]  # First 5 legitimate transactions

# Extract and scale the features
X_samples = df.loc[sample_ids, selected_features].values
scaler = joblib.load(r'D:\Projects\CreditCard\scaler.pkl')
X_scaled = scaler.transform(X_samples).reshape(len(X_samples), 1, len(selected_features))

# Load model and predict
model = tf.keras.models.load_model('attention_lstm_model.h5', custom_objects={'attention': attention})
predictions = model.predict(X_scaled)

# Print results
for i, score in zip(sample_ids, predictions):
    label = "Fraudulent" if score[0] > 0.7 else "Legitimate"
    print(f"Transaction ID {i}: {label} (Confidence: {score[0]:.2f})")  