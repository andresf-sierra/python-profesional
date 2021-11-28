def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def remove_set(some_list):
    return list(set(some_list))

def run():
    random_list = ["Esto","Parece","Increíble","pero","pero", "soy","soy", "James"]
    print(remove_duplicates(random_list))

if __name__=="__main__":
    run()            