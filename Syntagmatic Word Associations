from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
import numpy as np
import pandas as pd


def importing_data(filename):  # to open file
    data = open(filename).read()
    data = data.split('\n')  # to split we use  \n

    del data[0]  # to remove "reviews " we del the index
    del data[-1]  # to remove the extra index we del

    for x in range(len(data)):  # iterating here using a for loop over the data
        data[x] = data[x].replace('"', '')  
        data[x] = data[x].strip().upper().lower()  

    return data





def  make_df(
        top_pairs):  # this dataframe has top scores
    temppairs = []
    for x in range(top_pairs):
        temp = []
        for y in range(2):
            temp.append(vec.get_feature_names()[TopScores[x][0][
                y]])  
        temp.append(TopScores[x][1])  
        temppairs.append(temp)

    return pd.DataFrame(temppairs, columns=["Word1", "Word2", "Score"])

def cal_score(
        vsm):  # takes data 
    X = []
    for i in range(len(vsm.iloc[0])):  # Iterating over the data
        for j in range(i + 1, len(vsm.iloc[0])):
            temp = (i,j)  # the first word is i and the second word j and now we are turing that into a tuple
            temp2 = metrics.mutual_info_score(vsm[i], vsm[
                j])  # Calculating the mutual information of the two words 
            temp3 = (temp, temp2)  
            X.append(temp3)  # storing the each MI score in the tuple

    return X


data = get_data("file.csv")
vec = CountVectorizer(max_features=15,stop_words='english')  # converts the data into vector
output = vec.fit_transform(data)
matrix = output.toarray()

datavec = pd.DataFrame(matrix)  # converting the data into dataframe

X = get_scores(datavec)  # Gets the MI score 

Scores = []
for i in X:
    Scores.append(i[1])  # storing the score into the list

Y = np.argsort(Scores, axis=0)  # converting data into ascending

TopScores = []
for x in range(1, len(X)):  # converting data into descending order
    num = -x
    TopScores.append(X[Y[num]])

pairs = get_dataframe(50)

print("50 top assiatioon: ")
print(pairs.head())



