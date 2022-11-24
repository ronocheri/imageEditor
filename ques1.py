def group_by_owners(files):
    # declare a dictionary
    dic = {}

    # create the keys+empty lists
    for x in files.values():
        key = x
        dic.update({key: []})

    # add the values in the right place
    for y in files.items():
        newkey=y[1]
        newvalue=y[0]

        print(newkey,newvalue)
        dic[newkey].append(newvalue)

    return dic



if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))