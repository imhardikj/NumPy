import numpy as np

earnings = [
            [
                [500,505,490],
                [810,450,678],
                [234,897,430],
                [560,1023,640]
            ],
            [
                [600,605,490],
                [345,900,1000],
                [780,730,710],
                [670,540,324]
            ]
          ]
earnings = np.array(earnings)

print(earnings[0,0,0])

print(earnings.shape)

print(earnings[:,0,0])

print(earnings[:, 0, :])