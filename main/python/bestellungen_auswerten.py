import csv


def get_content_from_file(dateiname: str) -> [{}]:
    with open(dateiname, encoding='utf-8') as csv_file:
        result = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = []
        for i, row in enumerate(csv_reader):
            if i == 0:
                header = row.copy()
            else:
                result.append(get_dict_from_row(header, row))
        return result


def get_dict_from_row(header: [], row: []) -> {}:
    result = {}
    for i, columnName in enumerate(header):
        result[columnName] = row[i]
    return result


def filter_content(content: [{}], key: str, value: str) -> [{}]:
    result = []
    for row in content:
        if row[key] == value:
            result.append(row)
    return result


def get_share(content: [{}], filtered_content: [{}]) -> float:
    return len(filtered_content) / len(content) * 100


def get_sum(content: [{}]) -> float:
    result = 0
    for row in content:
        result += (float(row["Preis"]) * int(row["Menge"]))
    return round(result, 2)
