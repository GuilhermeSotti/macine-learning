import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import svm

style.use("dark_background")

def Status_Calc(stock, sp500):
  difference = stock - sp500

  if difference > how_much_better:
    return 1

  else:
    return 0

def Build_Data_Set(features = ["DE Radio",
                               "Trailing P/E"]):
  
  data_df = pd.DataFrame.from_csv("key_stats.csv")
  data_df = data_df[:, 100]
  data_df = data_df.reindex(np.random.permutation(data_df.index))

  data_df = ["Status2"] = list(map(Status_Calc, data_df['stock_p_change'], data_df['sp500_p_change']))
  X = np.array(data_df[features].values.tolist())
  Y = (data_df["Status"]
       .replace("underperform", 0)
       .replace("outperform", 1)
       .values.tolist())

def Analysis():

  X, Y = Build_Data_Set()
  clf = svm.SVC(kernel = "linear", C = 1.0)
  clf.fit(X, Y)
  
  w = clf.coef_[0]
  a = -w[0] / w[1]
  xx = np.linspace(min(X[:, 0]), max(X[:, 0 ]))
  yy = a * xx - clf.intercept_[0] / w[1]
  h0 = plt.plot(xx, yy, "k-", label = "non weigthed") 
  
  plt.xlabel("DE Radio")
  plt.ylabel("Trailing P/E")
  plt.legend()
  plt.show()

Analysis()