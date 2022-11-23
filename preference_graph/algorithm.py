def create_preference_list(str):

    preference_list = list()
    preference_list = str.split('\n')
    preference_list = list(filter(lambda x: x != '', preference_list))
    preference_list=list(map(lambda x: x.split(' '), preference_list))
    return preference_list

def create_list_of_nodes(str):
    preference_list = create_preference_list(str)
    list_of_nodes=list()
    for i in range(len(preference_list)-1):
        for j in preference_list[i]:
            for k in preference_list[i+1]:
                list_of_nodes.append((j, k))

    return list_of_nodes

