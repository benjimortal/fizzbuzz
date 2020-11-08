import pandas as pd
from matplotlib import pyplot
from dataclasses import make_dataclass


Person = make_dataclass("Person", [
    ('age', int),
    ('height', float),
    ('weight', float),
    ('chest', float),
    ('size', str),
    ('color', str)
], namespace={
    '__str__': lambda  self:f'{self.age}, {self.height},{self.weight},{self.chest},{self.size}, {self.color} \n'
})



def perpare_data(df, new_file_name):
    ages = df.Age.tolist()
    heights = [s/10 for s in df.stature.tolist()] #convertera till cm
    weights = [w/10 for w in df.weightkg.tolist()] # convertera till kg komprehantion
    chests = [c/10 for c in df.chestcircumference.tolist()]
    print(ages)
    print(heights)
    print(weights)
    print(chests)
    print(len(ages), len(heights), len(weights), len(chests))
    with open(new_file_name, "w") as out_file:
        out_file.write("Age, Height, Chest, Size, Color\n")
        for i in range(len(ages)):
            age = ages[i]
            height = heights[i]
            weight = weights[i]
            chest = chests[i]
            print(age, height, weight, chest)
            if chest < 84:
                size = "XX_Small"
                color = "pink"
            elif 84 <= chest < 90:
                size = "X_Small"
                color = "yellow"
            elif 90 <= chest < 95:
                size = "Small"
                color = "red"
            elif 95 <= chest < 102:
                size = "Medium"
                color = "blue"
            elif 102 <= chest < 112:
                size = "Large"
                color = "lawngreen"
            elif 112 <= chest < 123:
                size = "X_Large"
                color = "green"
            elif 123 <= chest < 133:
                size = "XX_Large"
                color = "slategray"
            else:
                size = "XXX_Large"
                color = "black"

            person = Person(age, height, weight, chest, size, color)
            out_file.write(str(person))

def main():
    df = pd.read_csv('female.csv', index_col=0)
    #print(df.stature.values.tolist())
    perpare_data(df, 'cleaned_female.csv')
    df = pd.read_csv('male.csv', index_col=0, encoding='latin-1')
    # print(df.stature.values.tolist())
    perpare_data(df, 'cleaned_male.csv')


if __name__ == '__main__':
    main()
