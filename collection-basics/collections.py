names = {'basic':'1997','fortran':'1997', 'c':'2000', 'c++':'2001', '.net':'2003', 'java':'2003','python':'2019'}

year = names.get('java')


if year is None:
    print('Year is missing ')
else:
    print('Year is ', year)
