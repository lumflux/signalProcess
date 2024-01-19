import numpy as np
import matplotlib.pyplot as plt

unitNum = 12  # 天线数量
sigLen = 100  # 信号点数
f = 0.25
lambd = 4
d = 0.5 * lambd

signalGain = 10
noiseRate = 0.1

theta1 = np.pi / 6  # 期望信号入射角度
theta2 = np.pi * 2 / 9  # 干扰信号入射角度

""" A S N """
def A_(theta):
    return np.exp(1j * 2 * np.pi * np.arange(unitNum) * d * np.sin(theta) / lambd)

A1 = A_(theta1)
A2 = A_(theta2)

S1 = np.sin(2 * np.pi * f * np.arange(sigLen))
S2 = np.cos(2 * np.pi * f * np.arange(sigLen))

A = np.vstack((A1, A2)).T  # 导向矢量
S = np.vstack((S1, S2)) * signalGain  # 信号源
N = np.random.randn(unitNum, sigLen) * noiseRate  # 噪声

""" X = A S + N """
X = np.dot(A, S) + N

""" w """
R1 = np.cov(X)
R = np.dot(X, X.T.conj()) / sigLen
w = np.dot(np.linalg.inv(R), A1) / np.dot(
    np.dot(A1.T.conj(), np.linalg.inv(R).T.conj()), A1
)

""" 方向图 """
theta = np.linspace(-np.pi, np.pi, 360)
values = []
for t in theta:
    value = np.dot(
        w.T.conj(), np.exp(1j * 2 * np.pi * np.arange(unitNum) * d * np.sin(t) / lambd)
    )
    values.append(value.flatten())

""" 对比图 """
get_signal = X
expect_signal = S1
interf_signal = S2
output_signal = np.dot(w.T.conj(), get_signal)

""" 绘图 """
plt.figure()
grid = plt.GridSpec(4, 5)

plt.subplot(grid[:, 0:2], projection="polar")
plt.plot(theta, np.abs(values))
plt.title("Directional pattern")
plt.grid(True)

# plt.figure()
plt.subplot(grid[0, 2:6])
plt.semilogy(np.abs(get_signal))
plt.title("received signal")
plt.grid(True)
plt.autoscale()

plt.subplot(grid[1, 2:6])
plt.plot((expect_signal))
plt.title("expect_signal")
plt.grid(True)

plt.subplot(grid[2, 2:6])
plt.plot((interf_signal))
plt.title("interf_signal")
plt.grid(True)

plt.subplot(grid[3, 2:6])
plt.plot(np.abs(output_signal))
plt.title("output_signal")
plt.grid(True)

plt.tight_layout()
plt.show()
