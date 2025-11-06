import matplotlib.pyplot as plt

nilai = [65, 70, 75, 80, 85, 90, 92, 95, 60, 78, 83, 88, 77, 69, 91, 85, 74, 72, 68, 66]

plt.figure(figsize=(10,10))

plt.hist(nilai, color="skyblue", edgecolor="black")

plt.title("Distribusi Nilai Siswa")
plt.xlabel("Nilai")
plt.ylabel("Nilai")
plt.grid(axis='y', alpha=0.5)
plt.show()

mean = sum(nilai)/len(nilai)
print(mean)
