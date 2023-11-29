# from sklearn.datasets import load_boston
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor  # could be adjusted for different model

# 讀取檔案
housing_df = pd.read_csv("HousingData.csv")

# 填補清除空值
housing_df.loc[:, housing_df.isnull().any()] = housing_df.loc[:, housing_df.isnull().any()].fillna(housing_df.mean())
'''
housing_df ['CRIM'] = housing_df['CRIM'].fillna(housing_df.mean())
housing_df ['ZN'] = housing_df['ZN'].fillna(housing_df.mean())
housing_df ['INDUS'] = housing_df['INDUS'].fillna(housing_df.mean())
housing_df ['CHAS'] = housing_df['CHAS'].fillna(housing_df.mean())
housing_df ['AGE'] = housing_df['AGE'].fillna(housing_df.mean())
housing_df ['LSTAT'] = housing_df['LSTAT'].fillna(housing_df.mean())
'''

# 指定 x, y 資料
dy = housing_df['MEDV']
dx = housing_df.drop(['MEDV'], axis=1)

# 標準化
dx_std = StandardScaler().fit_transform(dx)

# 分割訓練資料集與測試集
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, train_size=0.2, random_state=0)

# 建立模型
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(dx_train, dy_train)
predictions = knn.predict(dx_test)

print (dy_test)
print (predictions)
print (knn.score(dx_train, dy_train))
print (knn.score(dx_test, dy_test))