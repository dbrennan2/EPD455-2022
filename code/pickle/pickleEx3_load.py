import pickle
import numpy as np

# load x
test_x = np.load('testx.pkl',allow_pickle=True)
# load y
test_y = np.load('testy.pkl',allow_pickle=True)
# load model
with open('lm_model1.pkl', 'rb') as f:
    lm = pickle.load(f)

# make predictions based on the loaded model
pred_y = lm.predict(test_x)

# print the absolute error between prediction and test
print(np.mean(np.abs(pred_y - test_y)))


