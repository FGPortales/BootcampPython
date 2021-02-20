from array import array

import colorgram

arr = []
colors = colorgram.extract('image.jpg', 30)

for p in range(30):
    temp = []
    for s in range(3):
        temp.append(colors[p].rgb[s])
    arr.append(tuple(temp))

# first_color = colors[0]
# print(colors)
# print(colors[0].rgb)
#
# rgb = first_color.rgb
# red = rgb[0]
print(arr)
