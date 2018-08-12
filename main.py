import numpy as np

f = np.array([1,2,3])
g = np.array([2,3,4,5])

fg = np.convolve(f,g)

# print(fg)

n = len(f) + len(g) - 1
#
N = 2 ** (int(np.log2(n))+1)

print(n,N)


a = np.fft.fft(f,10)

b = np.fft.fft(g,10)

c = a * b

fft_fg = np.fft.ifft(c)[:n]

print(fft_fg - fg)