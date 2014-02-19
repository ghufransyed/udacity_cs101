# is_offered.py


def is_offered(courses, course, hexamester):
    if course in courses[hexamester]:
        return True
    else:
        return False
