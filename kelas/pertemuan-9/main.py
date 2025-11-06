import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [320, 450, 400, 390, 410, 470, 500, 490, 480, 510,
530, 600, 620, 590, 550, 570, 610, 640, 700, 5000, 1000, 2000, 800,
700, 750]
y = [10, 35, 20, 70, 60]
y2 = [12, 43, 56, 23, 67]

plt.figure(figsize=(12,6))


plt.boxplot(x,vert=False)
# Detail element
plt.title("Contoh Grafik")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")

#menampilkan garis grid


#menampilkan grafik
plt.show()