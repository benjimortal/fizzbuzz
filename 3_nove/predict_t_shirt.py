from math import sqrt
import pandas as pd
from matplotlib import pyplot


def get_neighbors(k, weight, height, data_list):
    distances = []
    for point in data_list:
        x = point[1]
        y = point[0]
        size = point[3]
        distance = sqrt((weight-x) **2 + (height-y)**2)
        distances.append({'distance': distance, 'size': size})
    distances.sort(key=lambda d:d['distance'])
    return distances[:k]


def predict(neighbors):
    sizes = {}
    for dist in neighbors:
        size = dist['size']
        if size in sizes:
            sizes[size] += 1
        else:
            sizes[size] = 1
    total = len(neighbors)
    return {size: value/ total * 180 for size, value in sizes.items()}



def main():
    data_female = pd.read_csv('cleaned_female.csv', index_col=0)
    data_male = pd.read_csv('cleaned_male.csv', index_col=0)

    numbers_of_rows = len(data_female) +len(data_male)

    weight , height = input("Enter your weight and height:").split()
    weight = float(weight)
    height = float(height)
    marker_style = dict(color='lavender', marker = 'X', markersize = 10)

    """_, ax = pyplot.subplot()
    ax.scatter(data_female.Weight, data_female.Height, c= data_female.Color)
    ax.scatter(data_male.Weight, data_male.Height, c=data_male.Color)
    pyplot.plot(weight,height, **marker_style)  # ** betyder att packa upp de som finns innuti dictionary
    pyplot.xlabel("Weight (kg)")
    pyplot.ylabel("Height (cm)")
    pyplot.show()"""

    data_list = data_male.values.tolist()
    n = int(sqrt(numbers_of_rows))
    k_values = [3, 4, 5, 6, 7, 8, 9, 10, 11, n]
    for k in k_values:
        neighbors = get_neighbors(3, weight, height, data_list)
        result = predict(neighbors)
        print(f"I predict that you get a t-shirt size of(k={k}:")
        for size, procent in result.items():
            print(f"\t{size} with a confidence of {procent:.2f}%")
        print("_________________________________")





if __name__ == '__main__':
    main()
