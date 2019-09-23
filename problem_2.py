import os

list_of_file = []


def find_c_files(path):
    if len(os.listdir(path)) == 0:
        return []

    list_of_dir_file = os.listdir(path)

    list_of_dir = []

    for file in list_of_dir_file:
        if '.c' in file:
            list_of_file.append(file)
        if '.' not in file:
            list_of_dir.append(file)

    for folders in list_of_dir:
        #print(path + '/'+folders)
        find_c_files(path + '/' + folders)
    return list_of_file


    #print(list_of_file)
    #print (list_of_dir)

    return 0

path = os.getcwd()
print(find_c_files(path))
