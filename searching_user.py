def searching_people(contacts):
    master_list = {'name': [],'email': [],'career': []}
    
    duplicate = False

    
    for individual in contacts: # for every dict in the list, and for the sublist and value zip together 
        for sublist, value in zip(master_list.values(),individual.values()):
            sublist.append(value)

    while True:
        extra = set()
        covered = set()
        search = input('Type an identifying charcteristic (type "n" to stop): ')
        if search == 'n'.lower():
            break
        found = False # no one found
        for person in contacts: # for each dict in the list
            check = any(search in value for value in person.values()) # this is saying, take a search if matches one of the values in all of the values in person.values(), that returns check.) 
            if check == True and len(search) >= 4: #if search is in a value and longer than 4 charcters
                    found = True
                    message = f'I believe you are looking for {person['name']}! '
                    break #will trgger on the innermost loop (if check == True and len(search) >= 4)
            if found:
                break  
        if found == False:
            print('Sorry, check character amount or missing entry!')   
        if found == True:
            for v in master_list.values():
                for key_word in v:
                    if key_word in covered:
                        extra.add(key_word)
                    else:
                        covered.add(key_word)
            
            for word in extra:
                if search == word:
                   duplicate = True
                   
            if duplicate == True:
                print('You have duplicate entrie(s) in your list')
        
            else:
                print(message)   
