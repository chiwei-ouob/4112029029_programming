from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler  # 用於將資料標準化
from sklearn.model_selection import train_test_split, cross_val_predict  # 交叉預測結果
from sklearn.tree import DecisionTreeClassifier  # 採用決策樹 (適用分類資料集)
from sklearn.metrics import classification_report  # 用於產生分類預測結果報告

# 指定 x, y 資料
dx, dy = load_digits(return_X_y=True)

# 標準化
dx_std = StandardScaler().fit_transform(dx)

# 分割訓練資料集與測試集
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, train_size=0.5, random_state=0)

# 建立模型
forest = DecisionTreeClassifier()
forest.fit(dx_train, dy_train)
y_kfold_predictions = cross_val_predict(forest, dx_std, dy, cv=5)  # 進行 K-fold 交叉驗證對所有資料進行預測

print (classification_report(dy, y_kfold_predictions))  # 輸出分類預測結果報告