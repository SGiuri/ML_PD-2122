models = {('kNN',KNeighborsClassifier()),
    ('SVC',SVC(random_state=SEED, probability=True)),
    ('DT',DecisionTreeClassifier(random_state=SEED)),
    ('RF',RandomForestClassifier(random_state=SEED)),
    ('GB',GradientBoostingClassifier(random_state=SEED)),
    ('GauNB',GaussianNB()),
    ('LR',LogisticRegression(solver='liblinear',max_iter=10000))}