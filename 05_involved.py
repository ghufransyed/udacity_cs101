# 05_involved.py



courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253':
                {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262':
                {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
               'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


def involved(courses, person):
    result = {}
    for term in courses:
        for course in courses[term]:
            for entry in courses[term][course]:
                if courses[term][course][entry] == person:
                    if term in result:
                        result[term].append(course)
                    else:
                        result[term] = [course]
#            if 'teacher' in courses[term][course]:
#                if person == courses[term][course]['teacher']:
#                    if term in result:
#                        result[term].append(course)
#                    else:
#                        result[term] = [course]
#            if 'assistant' in courses[term][course]:
#                if person == courses[term][course]['assistant']:
#                    if term in result:
#                        result[term].append(course)
#                    else:
#                        result[term] = [course]
    return result
