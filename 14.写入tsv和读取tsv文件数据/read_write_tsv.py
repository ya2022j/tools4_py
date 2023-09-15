import csv

data = [
    ['Alice', 25, 'Female'],
    ['Bob', 30, 'Male'],
    ['Charlie', 35, 'Male']
]

def write_into_tsv(data_list,tsvfile):


    with open(tsvfile, 'a', newline='') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        for row in data_list:
            writer.writerow(row)
        tsvfile.close()


# write_into_tsv(data,"t.tsv")


def read_tsv_file(tsvfile):
    with open(tsvfile, newline='') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        data = [row for row in reader]
        print(data)
read_tsv_file("t.tsv")
