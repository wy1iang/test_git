import my_utils.str_util
import my_utils.file_util

str = 'abcdefg'
print(my_utils.str_util.str_reverse(str))
print(my_utils.str_util.substr(str,2,4))

filename = 'word.txt'
my_utils.file_util.print_file_info(filename)
my_utils.file_util.append_to_file(filename,'abc')
my_utils.file_util.print_file_info(filename)