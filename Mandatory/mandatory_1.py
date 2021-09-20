#Assignment 1
print('\nAssignment 1')
#Model an organisation of employees, management and board of directors in 3 sets
boardOfDirectors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

#Who in the board of directors is not an employee?
directorsThatAreNotEmployees = boardOfDirectors.difference(employees)
print(directorsThatAreNotEmployees)

#who in the board of directors is also an employee?
directorsThatAreEmployees = employees.intersection(boardOfDirectors)
print(directorsThatAreEmployees)

#how many of the management is also member of the board?
managersThatAreAlsoDirectors = boardOfDirectors.intersection(management)
numberOfManagersThatAreAlsoDirectors = len(managersThatAreAlsoDirectors)
print(numberOfManagersThatAreAlsoDirectors)

#All members of the management also an employee
managersThatAreAlsoEmployees = management.intersection(employees)
print(managersThatAreAlsoEmployees)

#All members of the management also in the board?
print(managersThatAreAlsoDirectors)

#Who is an employee, member of the management, and a member of the board?
employeesThatAreAlsoManagersAndDirectors = employees.intersection(management, boardOfDirectors)
print(employeesThatAreAlsoManagersAndDirectors)

#Who of the employee is neither a memeber or the board or management?
employeesThatAreNotManagerAndDirector = employees.difference(management, boardOfDirectors)
print(employeesThatAreNotManagerAndDirector)

#Assignment 2
print('\nAssignment 2')
#Using a list comprehension create a list of tuples from the folowing datastructure
datastructure = {
    'a': 'Alpha',
    'b': 'Beta',
    'g': 'Gamma'
    }
newTuple = [(k, v) for k, v in datastructure.items()]
print(newTuple)

#Assignment 3
print('\nAssignment 3')
#From these 2 sets
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å'}

#Of the 2 sets create a:
#Union
union = set1.union(set2)
print(union)

#Symmeric Difference
symmetricDifference = set1.symmetric_difference(set2)
print(symmetricDifference)

#Difference
difference = set2.difference(set1)
print(difference)

#Disjoint
disjoint = set1.isdisjoint(set2)
print(disjoint)

#Assignment 4 - Date Decoder
print('\nAssignment 4')

monthdict = {
    'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr': 4,
    'may': 5,
    'jun': 6,
    'jul': 7,
    'aug': 8,
    'sep': 9,
    'okt': 10,
    'nov': 11,
    'dec': 12
}

def dateSplitter(date):
    splitdate = date.split('-')
    convertMonth = monthdict.get(splitdate[1])
    convertedDate = ('19' + splitdate[2], convertMonth, splitdate[0])
    print(convertedDate)

dateSplitter('8-mar-85')