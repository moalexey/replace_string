# -*- coding: UTF-8 -*-

'''Replace text string in file if file ends with given simbols
'''

import os

# Find this string
replace_this_string = 'Old text'

# Replacement text
string_for_replace = 'New text'

# If file ends with simbols: .html or .htm
file_ends_with = ('.html', '.htm')

for root, dirs, files in os.walk('.'):
    for name in files:
        if name.endswith(file_ends_with):
            file_name = os.path.join(root, name)

            file = open(file_name).read()
            file = file.replace(replace_this_string, string_for_replace)
            open(file_name, 'w').write(file)
