# encoding:utf-8
import csv


def readecsv(file_path):
    csvFile = open(file_path, 'rb');
    reader = csv.reader(csvFile);
    result = [];
    for item in reader:
        result.append(item)
    csvFile.close()
    return result;
