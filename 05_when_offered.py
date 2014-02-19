# 05_when_offered.py


def when_offered(courses, course):
    result = []
    for hexamester in courses:
        if course in courses[hexamester]:
            result.append(hexamester)
    return result
