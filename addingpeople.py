def adding_people(contacts):
   while True:
       gate = input('Would you like to add a person y/n: ')
       if gate == 'n'.lower():
           print(f'Thats all for today, you have {len(contacts)} people in ur contacts!')
           break
       name = input('Enter a name: ')
       email = input('Enter an email: ')
       career = input('Enter a career: ')
       person = {'name': name, 'email': email, 'career': career}
       contacts.append(person)
