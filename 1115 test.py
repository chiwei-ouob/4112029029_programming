'''Q1'''
import numpy as np
print (np.array([1, 2, 3, 4, 5, 6]).reshape(3, 2))

'''Q2'''
print (max([1, 3, 5, 7, 2, 4, 6, 8]),", ",min([1, 3, 5, 7, 2, 4, 6, 8]))

'''Q3'''
import pandas as pd
#import numpy as np  # This module has been imported in Line 5
score_book = pd.DataFrame({'grammer': ['python', 'java', 'go', np.NaN, 'python', 'C', 'C++'], 
                                        'score': [1.0, np.NaN, np.NaN, 4.0, 5.0, 7.0, 8.0]})
print ("score book: \n", score_book)
score_book.columns = ["grammer", "popularity"]
print ("score book after renaming a column: \n", score_book)
print (f"Average of the popularity: {score_book['popularity'].mean()}")

'''Q4'''
#import numpy as np  # This module has been imported in Line 5
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='sin(x)')
plt.title('Line chart')
plt.legend()
plt.show()

data = np.random.randn(100)
data1 = np.random.randn(100)

plt.bar(data, data1)
plt.ylim(0,4)
plt.show()