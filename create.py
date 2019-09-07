import numpy as np
import imageio
import os

WIDTH = 1920


low = 0
high = 30000

MB = 1024 * 1024
target_size = 100 * MB

file_path = "/tmp/test.png"
result_path = "test.png"

if __name__ == '__main__':

    mid = None
    for i in range(20):
        mid = (low + high) // 2
        print(mid)
        img = np.random.randint(0, 255, (mid, WIDTH, 3), dtype=np.uint8)
        imageio.imsave(file_path, img)
        size = os.path.getsize(file_path)
        print(size)
        if size > target_size:
            high = mid
        elif size < target_size:
            low = mid

    img = np.random.randint(0, 255, (mid, WIDTH, 3), dtype=np.uint8)
    imageio.imsave(result_path, img)
