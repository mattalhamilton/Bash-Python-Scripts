##Matt Hamilton
##Mod 03 Homework

d = 0

def m1(userinput):
    d = 0
    fname = input('What letter does the first name begin with? ')
    fname = str(fname)
    fname = fname.upper()

    
    for j in range(0,len(name_list)):
        if name_list[j].startswith(fname):
            print(name_list[j])
            d = d + 1

    if d == 0:
        print('No first names starting with ' + fname + ' were found\n')
    
        


        



def m2(userinput):
    lname = input('What letter does the last name begin with? ')
    lname = str(lname)
    lname = lname.upper()
    d = 0


    for j in range(0,len(name_list)):
        j= name_list[j].split()
        if j[1].startswith(lname):
            print(j[1], j[0])
            d = d + 1

    if d == 0:
        print('No last names starting with ' + lname + ' were found\n')

                 

def m3(userinput):
    fname = input('Enter the new first name: ')
    fname = str(fname)
    fname = fname.title()
    lname = input('Enter the new last name: ')
    lname = str(lname)
    lname = lname.title()

    insertname = ' '.join([fname, lname])
    name_list.append(insertname)
    print('\n' + name_list[-1] + ' has been added.\n')


def m4(userinput):
    fname = input('Enter the full name to delete: ')
    fname = str(fname)
    fname = fname.title()
    
    if fname not in name_list:
        print('That name was not found in the list')
        
    if fname in name_list:
        name_list.remove(fname)
        if fname in name_list:
            print('The name removal procedure failed.')
        if fname not in name_list:
            print('\n' + fname + ' has been removed.')
    



name_list = ['Constance Castillo', 'Kerry Goodwin',
 'Dorothy Carson', 'Craig Williams', 'Daryl Guzman', 'Sherman Stewart',
 'Marvin Collier', 'Javier Wilkerson', 'Lena Olson', 'Claudia George',
 'Erik Elliott', 'Traci Peters', 'Jack Burke', 'Jody Turner',
 'Kristy Jenkins', 'Melissa Griffin', 'Shelia Ballard', 'Armando Weaver',
 'Elsie Fitzgerald', 'Ben Evans', 'Lucy Baker', 'Kerry Anderson',
 'Kendra Tran', 'Arnold Wells', 'Anita Aguilar', 'Earnest Reeves',
 'Irving Stone', 'Alice Moore', 'Leigh Parsons', 'Mandy Perez',
 'Rolando Paul', 'Delores Pierce', 'Zachary Webster', 'Eddie Ward',
 'Alvin Soto', 'Ross Welch', 'Tanya Padilla', 'Rachel Logan',
 'Angelica Richards', 'Shelley Lucas', 'Alison Porter', 'Lionel Buchanan',
 'Luis Norman', 'Milton Robinson', 'Ervin Bryant', 'Tabitha Reid',
 'Randal Graves', 'Calvin Murphy', 'Blanca Bell', 'Dean Walters',
 'Elias Klein', 'Madeline White', 'Marty Lewis', 'Beatrice Santiago',
 'Willis Tucker', 'Diane Lloyd', 'Al Harrison', 'Barbara Lawson',
 'Jamie Page', 'Conrad Reynolds', 'Darnell Goodman', 'Derrick Mckenzie',
 'Erika Miller', 'Tasha Todd', 'Aaron Nunez', 'Julio Gomez',
 'Tommie Hunter', 'Darlene Russell', 'Monica Abbott', 'Cassandra Vargas',
 'Gail Obrien', 'Doug Morales', 'Ian James', 'Jean Moran',
 'Carla Ross', 'Marjorie Hanson', 'Clark Sullivan', 'Rick Torres',
 'Byron Hardy', 'Ken Chandler', 'Brendan Carr', 'Richard Francis',
 'Tyler Mitchell', 'Edwin Stevens', 'Paul Santos', 'Jesus Griffith',
 'Maggie Maldonado', 'Isaac Allen', 'Vanessa Thompson', 'Jeremy Barton',
 'Joey Butler', 'Randy Holmes', 'Loretta Pittman', 'Essie Johnston',
 'Felix Weber', 'Gary Hawkins', 'Vivian Bowers', 'Dennis Jefferson',
 'Dale Arnold', 'Joseph Christensen', 'Billie Norton', 'Darla Pope',
 'Tommie Dixon', 'Toby Beck', 'Jodi Payne', 'Marjorie Lowe',
 'Fernando Ballard', 'Jesse Maldonado', 'Elsa Burke', 'Jeanne Vargas',
 'Alton Francis', 'Donald Mitchell', 'Dianna Perry', 'Kristi Stephens',
 'Virgil Goodwin', 'Edmund Newton', 'Luther Huff', 'Hannah Anderson',
 'Emmett Gill', 'Clayton Wallace', 'Tracy Mendez', 'Connie Reeves',
 'Jeanette Hansen', 'Carole Fox', 'Carmen Fowler', 'Alex Diaz',
 'Rick Waters', 'Willis Warren', 'Krista Ferguson', 'Debra Russell',
 'Ellis Christensen', 'Freda Johnston', 'Janis Carpenter', 'Rosemary Sherman',
 'Earnest Peters', 'Kelly West', 'Jorge Caldwell', 'Moses Norris',
 'Erica Riley', 'Ray Gordon', 'Abel Poole', 'Cary Boone',
 'Grant Gomez', 'Denise Chapman', 'Vernon Moran', 'Ben Walker',
 'Francis Benson', 'Andrea Sullivan', 'Wayne Rice', 'Jamie Mason',
 'Jane Figueroa', 'Pat Wade', 'Rudy Bates', 'Clyde Harris',
 'Andre Mathis', 'Carlton Oliver', 'Merle Lee', 'Amber Wright',
 'Russell Becker', 'Natalie Wheeler', 'Maryann Miller', 'Lucia Byrd',
 'Jenny Zimmerman', 'Kari Mccarthy', 'Jeannette Cain', 'Ian Walsh',
 'Herman Martin', 'Ginger Farmer', 'Catherine Williamson', 'Lorena Henderson',
 'Molly Watkins', 'Sherman Ford', 'Adam Gross', 'Alfred Padilla',
 'Dwayne Gibson', 'Shawn Hall', 'Anthony Rios', 'Kelly Thomas',
 'Allan Owens', 'Duane Malone', 'Chris George', 'Dana Holt',
 'Muriel Santiago', 'Shelley Osborne', 'Clinton Ross', 'Kelley Parsons',
 'Sophia Lewis', 'Sylvia Cooper', 'Regina Aguilar', 'Sheila Castillo',
 'Sheri Mcdonald', 'Lynn Hodges', 'Patrick Medina', 'Arlene Tate',
 'Minnie Weber', 'Geneva Pena', 'Byron Collier', 'Veronica Higgins',
 'Leo Roy', 'Nelson Lopez']



while True:

    
    print('''Please select from the following options:

    1.  List all first names beginning with a chosen letter
    2.  List all last names beginning with a chosen letter
    3.  Add a name
    4.  Delete a name
    5.  Exit''')

    userinput = input('Option#: ')

    userinput = int(userinput)

    if userinput not in range(1,6):
        print('That is not a valid option. Please try again.\n')


    elif userinput == 1:
        option = m1(userinput)
        print(option)


    elif userinput == 2:
        option = m2(userinput)
        print(option)

    elif userinput == 3:
        option = m3(userinput)
        print(option)

    elif userinput == 4:
        option = m4(userinput)
        print(option)

    elif userinput == 5:
        break

    else:
        continue

print('Please press enter to exit the script: ')
input()

        

        

















