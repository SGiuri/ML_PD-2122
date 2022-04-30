# Introduzione al Machine Learning

Un sistema per far si che i computer si programmino da soli.   
Parte dalla disponibilità di dati. 



## Tipologie di Machine Learning  
Questi dati possono essere già associati ad un target 
fotografie di mele --> c'e' la mela o non c'e' la mela
Potrebbero essere non necessariamente gia' associati ad uno specifico target:
fotografie generiche di frutta.   

### Supervisionato
Quando il target e' gia dichiarato.   
Per ciascuna fotografia che ho a disposizione, so gia' in anticipo quali contengono mele
quali contengono pere, o banane.   
Dati: X    
target: y    
X --> y    
X e' una matrice, una tabella di _numeri_    
y e' una colonna, una matrice =, anchessa fatta di numeri.

#### Classificazione
y e' rappresentato da _categorie_ 
- mela / pera / banana
- vero / falso
- e' una frode / non e' una frode

L'algoritmo di Machine Learning cerchera' di associare ciascun elemento ad una categoria.
```python
from sklearn.neighbors import KNeighborsClassifier
knn_cl = KNeighborsClassifier()
```
#### Regressione
y e' un numero che va da un minimo ad un massimo:
- Quantificazione del costo di una casa.

L'algoritmo di Machine Learning cerchera' di _calcolare_ quel numero


### Non Supervisionato
Non abbiamo a disposizione la colonna _y, target_. I dati vengono analizzati e suddivisi, 
categorizzati in modo automatico.

#### Clusternig _KMeans_


## Struttura di un progetto di Machine Learning



## Fonti per Dataset:

- [Vincent are bundock github repo](https://vincentarelbundock.github.io/Rdatasets/articles/data.html)
- [Awesome Dataset Github repo](https://github.com/awesomedata/awesome-public-datasets)
- [UCI EDU Maryland University Dataset](https://archive.ics.uci.edu/ml/datasets.php)
### Dataset di serie temporali
- [National Oceanic and Atmospheric Administration](www.ncdc.noaa.cov/cag) per serie temporali su clima negli USA e Globali
- [Earth System Research Library](https://psl.noaa.gov/data/timeseries/) del NOAA fornisce time series climatiche annuali o mensili
- [European Climate Assessment & Dataset project](https://www.ecad.eu/)
- [Quandl](www.quandl.com/search) fornisce serie temporali finanziarie
- [Time Series Data library](https://pkg.yangzhuoranyang.com/tsdl/articles/tsdl.html) contiene serie temporali su
diversi settori industriali


## Strumenti grafici comunemente usati per visualizzazioni EDA

- `sns.barplot()`<br>
- `sns.boxplot()`<br>
- `sns.histplot()`<br>
- `sns.catplot()`<br>
- `sns.heatmap()`<br>
- `pd.crosstab()`<br>`

## Framework:

- [TensorFlow](https://www.tensorflow.org/api_docs/python/tf)
- [Scikit Learn](https://scikit-learn.org/stable/modules/classes.html)
- [Keras](https://keras.io/api/)
- [Pytorch](https://pytorch.org/docs/stable/torch.html)
- [etc...etc...](https://hackr.io/blog/machine-learning-frameworks)

## Scikit Learn:
- [Estimators](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html)
- []
