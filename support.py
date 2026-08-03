from csv import reader

# Gets CSV Data From Path
def get_csv_data(path):
    return_data = []

    with open(path) as data:
        data_read = reader(data, delimiter=",")
        for row in data_read:
            return_data.append(row)

    return return_data