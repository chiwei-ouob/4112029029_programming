import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor  # could be adjusted for different model

# 讀取檔案
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")

# 移除無關資料
train_df = train_df.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)
test_df = test_df.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)

# 將性別改為整數
train_df = train_df.replace(['male','female'], [1, 0])
test_df = test_df.replace(['male','female'], [1, 0])

# 填補清除空值
train_df.loc[:, train_df.isnull().any()] = train_df.loc[:, train_df.isnull().any()].fillna(train_df.mean())
test_df.loc[:, test_df.isnull().any()] = test_df.loc[:, test_df.isnull().any()].fillna(test_df.mean())

# 指定 x, y 資料
dy_train = train_df['Survived']
dx_train = train_df.drop(['Survived'], axis=1)
dx_test = test_df

# 標準化
dx_train_std = StandardScaler().fit_transform(dx_train)
dx_test_std = StandardScaler().fit_transform(dx_test)

# 分割訓練資料集與測試集 (此專案無須此步驟)
# dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, train_size=0.2, random_state=0)

# 建立模型
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(dx_train, dy_train)
predictions = knn.predict(dx_test)

# print (dy_test)
print (predictions)
print (knn.score(dx_train, dy_train))
# print (knn.score(dx_test, dy_test))  # 測試集未提供是否生存之資料，故無法判定訓練成績