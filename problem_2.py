import os

def find_c_files(path=None, suffix=None):
    if path is None or suffix is None:
        print('Please check the path or suffix')
        return -1

    if len(os.listdir(path)) == 0:
        return []

    list_of_dir_file = os.listdir(path)
    #print(list_of_dir_file)
    list_of_dir = []
    list_of_file = []

    for item in list_of_dir_file:
        if os.path.isdir(path + '/' + item):
            list_of_dir.append(item)
        if os.path.isfile(path + '/' + item):
            list_of_file.append(item)

    for file in list_of_file:
        file_n_len = len(file)
        if suffix == file[file_n_len-2:]:
            list_of_suffix_file.append(file)

    for folders in list_of_dir:
        # print(path + '/'+folders)
        find_c_files(path + '/' + folders, suffix)
    return list_of_suffix_file

    return 0

# Test Case 1
list_of_suffix_file = []
path = os.getcwd()
print(find_c_files(path,'.c'))
#['t1.c', 'test.c', 'a.c', 'b.c', 'a.c']

# Test Case 2
list_of_suffix_file = []
print(find_c_files())
#[]
#Please check the path or suffix
#-1

# Test Case 3
list_of_suffix_file = []
print(find_c_files(path,'.h'))
# ['t1.h', 'a.h', 'b.h', 'a.h']