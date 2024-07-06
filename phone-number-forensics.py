import os
import os.path
from collections import defaultdict

def GET_STRING_FROM_FILE(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def just_digits(s):
    return ''.join(filter(str.isdigit, s))

def file_walker(path):
    result = list(os.walk(path))
    
    count_txt = 0
    count_CS = 0
    max_depth = 0
    max_depth_path = ''
    
    num_10_digits = 0
    num_7_digits = 0
    num_11_plus_digits = 0
    num_650_area_code = 0
    
    num_hamrah_last_name = 0
    num_armin_first_name = 0
    num_three_is_in_name = 0
    
    num_zd = 0
    name_count = defaultdict(int)
    hello_hi_or_goodbye = False
    
    num_ss = 0
    num_py = 0
    num_java = 0
    winner = 'Null'
    largest_file_size = 0
    name_largest_file_size = 'Null'

    for folder_tuple in result:
        currentpath, subfolders, files = folder_tuple
        if '__MACOSX' in currentpath: continue
        
        depth = currentpath.count("/")
        if depth > max_depth:
            max_depth = depth
            max_depth_path = currentpath

        for file in files:
            fullpath = os.path.join(currentpath, file)
            if file[0] == ".": continue

            if file[-4:] == ".txt":
                count_txt += 1
                contents = GET_STRING_FROM_FILE(fullpath)
                cl = contents.lower()
                if 'a' in cl:
                    count_CS += 1
                digits = just_digits(cl)
                if len(digits) == 10:
                    num_10_digits += 1
                if len(digits) == 7:
                    num_7_digits += 1
                if len(digits) > 10:
                    num_11_plus_digits += 1
                if digits.startswith('650'):
                    num_650_area_code += 1
                
                L = cl.split("\n")
                if len(L) > 1:
                    name = L[1]
                    if ',' in name:
                        L = name.split(',')
                        if len(L) < 2: continue
                        last_name = L[0].strip()
                        first_name = L[1].strip()
                    else:
                        L = name.split(' ')
                        if len(L) < 2: continue
                        first_name = L[0].strip()
                        last_name = L[1].strip()
                    full_name = f"{first_name} {last_name}"
                    name_count[full_name] += 1
                    if 'hamrah' in last_name: num_hamrah_last_name += 1
                    if 'armin' in first_name: num_armin_first_name += 1
                    if full_name.count('i') >= 3: num_three_is_in_name += 1
                    if 'zach' in first_name and 'dodds' in last_name: num_zd += 1 ##Zach Dodds is my favorite CS professor of college (so far:)
                    if first_name in "hello hi goodbye": hello_hi_or_goodbye = True
                
            if "screenshot" in fullpath.lower():
                num_ss += 1
            if ".py" in fullpath.lower():
                num_py += 1
            if ".java" in fullpath.lower():
                num_java += 1
            size = os.path.getsize(fullpath)
            if size > largest_file_size:
                largest_file_size = size
                name_largest_file_size = fullpath

    most_common_name = max(name_count, key=name_count.get)
    count_most_common_name = name_count[most_common_name]

    if num_java > num_py:
        winner = 'Java'
    elif num_py > num_java:
        winner = 'Python'
    elif num_py == num_java:
        winner = 'Tie!'

    return (count_CS, count_txt, max_depth, max_depth_path,
            num_10_digits, num_11_plus_digits, num_7_digits, num_650_area_code,
            num_hamrah_last_name, num_armin_first_name, num_three_is_in_name,
            num_zd, most_common_name, count_most_common_name,
            num_ss, num_py, num_java, winner, largest_file_size, name_largest_file_size, hello_hi_or_goodbye)

if True:
    print(f"[[ Start! ]]\n")
    path = "."
    result = file_walker(path)
    
    (count_CS, count_txt, max_depth, max_depth_path,
     num_10_digits, num_11_plus_digits, num_7_digits, num_650_area_code,
     num_hamrah_last_name, num_armin_first_name, num_three_is_in_name,
     num_zd, most_common_name, count_most_common_name,
     num_ss, num_py, num_java, winner, largest_file_size, name_largest_file_size, hello_hi_or_goodbye) = result

    perc = count_CS * 100 / count_txt
    print(f"num txt files       = {count_txt}")
    print(f"num containing 'a'  = {count_CS}")
    print(f"for an 'a' percentage of {perc:5.2f}%")
    print(f"the max depth: {max_depth}")
    print(f"This is the entire path for the longest path in our folder: {max_depth_path}")
    print(f"Num files with exactly 10 digits in the first line: {num_10_digits}")
    print(f"Num files with more than 10 digits: {num_11_plus_digits}")
    print(f"Num files with exactly 7 digits: {num_7_digits}")
    print(f"Num files with '650' area code: {num_650_area_code}")
    print(f"Num people with last name 'Hamrah': {num_hamrah_last_name}")
    print(f"Num people with first name 'Armin': {num_armin_first_name}")
    print(f"Num people with 3 'i's in their name: {num_three_is_in_name}")
    print(f"Num Zach Dodds: {num_zd}")
    print(f"The most common name is '{most_common_name}' with a count of {count_most_common_name}.")
    print(f"Num screenshots: {num_ss}")
    print(f"Num Python files: {num_py}")
    print(f"Num Java files: {num_java}")
    print(f"We have more {winner}!")
    print(f"Your largest file's name is {name_largest_file_size}, and it is {largest_file_size} bytes")
    print(f"Someone in my directory is named 'hello', 'hi', or 'goodbye': {hello_hi_or_goodbye}")
    print("\n[[ Fin. ]]")