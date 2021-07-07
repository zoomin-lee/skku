import numpy as np
import struct

np.random.seed(1)

feature = []
for i in range(1000):
    number = 100000 + i
    with open('./sift/sift' + str(number), 'rb') as f:
        while True:
            for j in range(128):
                b = f.read(1)
                if not b:
                    break
                feature.append(int(ord(b)))
            if not b:
                break

feature = np.reshape(feature, (-1, 128))
random = np.random.choice(feature.shape[0], 100000, replace=False)
feature100000 = feature[random]
np.save("./feature", feature100000)

def compute_L2(point, centroid):
    return np.sqrt(np.sum((point - centroid) ** 2))

def kplus(points):
    print("8 Initial Centroids Setup")
    centroids = []
    first = np.random.choice(len(points), 1)
    centroids.append(points[first])
    for i in range(7):
        max_distance=0
        for j in range(len(points)):
            distance = compute_L2(centroids[i], points[j])
            if distance > max_distance:
                max_distance = distance
                max_index = j
        centroids.append(points[max_index])
    return np.vstack(np.array(centroids))

def get_index(points, centroids):
    min_distance = 100000
    for c in range(len(centroids)):
        distance = compute_L2(points, centroids[c])
        if distance < min_distance:
            min_distance = distance
            group_index = c
    return group_index

def EM_algorithm(data_points, centroids, iteration):
    for i in range(iteration):
        print(i+1,'th iteration')
        group = [[],[],[],[],[],[],[],[]]
        new_centroids = np.zeros((8, 128))
        for p in range(len(data_points)):
            group_index = get_index(data_points[p],centroids)
            group[group_index].append(data_points[p])
        group = np.array(group)
        for j in range(8):
            if len(group[j]) == 0:
                new_centroids[j] = centroids[j]
            else :
                new_centroids[j] = np.mean(group[j],axis=0)
        centroids = new_centroids
    return centroids

print("--- k-means++ Algorithm ---")
points = np.load('feature.npy')
centroids = kplus(points)
print("--- EM Algorithm ---")
new_centroids = EM_algorithm(points[:, :], centroids, 30)
np.save('kmeans_centroids', new_centroids)

print("--- Make Descriptor ---")
centroids = np.vstack(np.load('kmeans_centroids.npy'))
result = np.zeros((1000, 1024))
for i in range(1000):
    number = 100000 + i
    if i%100==0:
        print(i,"th image")
    with open('./sift/sift' + str(number), 'rb') as f:
        while True:
            feature = np.zeros(128)
            for j in range(128):
                b = f.read(1)
                if not b:
                    break
                feature[j] = (int(ord(b)))
            if not b:
                break

            index = get_index(feature, centroids)
            index1024 = index * 128
            result[i, index1024:index1024 + 128] += feature - centroids[index]
        result[i] = result[i] / np.sqrt(np.dot(result[i], result[i]))

with open('A4_2017310695.des', 'wb') as f:
    f.write(struct.pack('ii', 1000, 1024))
    f.write(result.astype('float32').tobytes())
