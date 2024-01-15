# %%
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# %%
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

# %%
vals = np.linspace(-10, 10, num=100, dtype=np.float32)
activation = sigmoid(vals)
fig = plt.figure(figsize=(12,6))
fig.suptitle('Sigmoid function')
plt.plot(vals, activation)
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.yticks()
plt.ylim([-0.5, 1.5])

# %%
def logic_gate(w1, w2, b):
    return lambda x1, x2: sigmoid(w1 * x1 + w2 * x2 + b)

def test(gate):
    for a, b in (0, 0), (0, 1), (1, 0), (1, 1):
        print("{}, {}: {}".format(a, b, np.round(gate(a, b))))

# %%
w1 = 20
w2 = 20
b = -10
or_gate = logic_gate(w1, w2, b)
print("OR GATE")
test(or_gate)

# %%
w1 = 10
w2 = 10
b = -10
and_gate = logic_gate(w1, w2, b)
print("AND GATE")
test(and_gate)

# %%
w1 = -10
w2 = -10
b =   10
nor_gate = logic_gate(w1, w2, b)
print("NOR GATE")
test(nor_gate)

# %%
w1 = -10
w2 = -10
b =   20
nand_gate = logic_gate(w1, w2, b)
print("NAND GATE")
test(nand_gate)

# %%
def xor_gate(a, b):
    c = or_gate(a, b)
    d = nand_gate(a, b)
    return and_gate(round(c), round(d))
print("XOR GATE")
test(xor_gate)

# %%
def xnor_gate(a, b):
    c = or_gate(a, b)
    d = nand_gate(a, b)
    return nand_gate(round(c), round(d))
print("XNOR GATE")
test(xnor_gate)

# %%
# !pip install tensorflow

# %%
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x = [[0,0],[0,1],[1,0],[1,1]]
y = [0,1,1,0]

model = Sequential()
model.add(Dense(2, input_shape=(2,), activation='tanh'))
# model.add(Dense(4, activation='sigmoid'))
model.add(Dense(1, activation='tanh'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x, y, epochs=100)


# %%
print("XOR GATE")
print(x)
for i in model.predict(x):
    if (i<0.4 and i>-0.4):
        print(0)
    else:
        print(1)


