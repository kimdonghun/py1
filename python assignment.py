import matplotlib.pyplot as plt

def trap(height):
    l, r = 0, len(height) - 1
    lmax, rmax = 0, 0
    water = [0] * len(height)

    while l < r:
        if height[l] < height[r]:
            lmax = max(lmax, height[l])
            water[l] = max(0, lmax - height[l])
            l += 1
        else:
            rmax = max(rmax, height[r])
            water[r] = max(0, rmax - height[r])
            r -= 1

    return sum(water), water


height = [0,1,0,2,1,0,1,3,2,1,2,1]
total, water = trap(height)

plt.bar(range(len(height)), height, color='gray')
plt.bar(range(len(water)), water, bottom=height, color='blue')
plt.title(f"Total Water = {total}")
plt.show()

height= [4,2,0,3,2,5]
total, water = trap(height)
plt.bar(range(len(height)), height, color='gray')
plt.bar(range(len(water)), water, bottom=height, color='blue')
plt.title(f"Total Water = {total}")
plt.show()

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
total, water = trap(height)
plt.bar(range(len(height)), height, color='gray')
plt.bar(range(len(water)), water, bottom=height, color='blue')
plt.title(f"Total Water = {total}")
plt.show()