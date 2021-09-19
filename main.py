from getdata import fetch_housing_data
from loaddata import load_housing_data
from grafdata import graf_data


def main():
    # вызов fetch_housing_data() приводит к созданию каталога  datasets / housing в рабочей области,
    # загрузке файла housing.tgz, извлечению из него файла housing.csv и его перемещению в указанный каталог
    fetch_housing_data()

    # возвращает Раndаs-объект DataFrame, содержащий все данные
    housing = load_housing_data()
    # возвращает график, содержащий все данные
    graf_data(housing)
    # Создание тренировочного набора
    from sklearn.model_selection import StratifiedShuffleSplit

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]
    for set_ in (strat_train_set, strat_test_set):
        set_.drop("income_cat", axis=1, inplace=True)


if __name__ == '__main__':
    main()
