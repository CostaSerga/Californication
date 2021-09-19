import matplotlib.pyplot as plt
# возвращает Раndаs-объект DataFrame, содержащий все данные
def graf_data(housing):
    housing.hist(bins=50, figsize=(20,15))
    plt.savefig("attribute_histogram_plots")
    plt.show()