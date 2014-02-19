# exam_05.py



english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May",
6:"June", 7:"July", 8:"August", 9:"September",10:"October",
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012".
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj",
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober",
11:"november", 12:"december"}

cornish = {1: 'Mys Genver', 2: 'Mys Whevrel', 3: 'Mys Merth',
           4: 'Mys Ebrel', 5: 'Mys Me', 6: 'Mys Efan',
           7: 'Mys Gortheren', 8: 'Mys Est', 9: 'Mys Gwyngala',
           10: 'Mys Hedra', 11: 'Mys Du', 12: 'Mys Kevardhu'}


def date_converter(calendar, date):
    marker_1 = date.find('/')
    marker_2 = date.find('/', marker_1 + 1)
    month_int = int(date[:marker_1])
    day_int = int(date[marker_1 + 1:marker_2])
    year_int = int(date[marker_2 + 1:])
    print "day is :%r" % day_int
    print "month is :%r" % month_int
    print "year is :%r" % year_int
    return (str(day_int) + ' '
            + calendar[month_int] + ' '
            + str(year_int).zfill(2))


print date_converter(english, '08/14/1972')
print date_converter(cornish, '7/7/05')
