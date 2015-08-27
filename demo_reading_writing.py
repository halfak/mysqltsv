

import io
import sys

import mysqltsv

writer = mysqltsv.Writer(sys.stdout, headers=['user_id', 'user_text', 'edits'])
writer.write([10, 'Foobar_Barman', 2344])
writer.write({'user_text': 'Barfoo_Fooman', 'user_id': 11, 'edits': 20})
writer.write([None, "127.0.0.1", 42])

my_file = io.StringIO("user_id\tuser_text\tedits\n" +
                      "10\tFoobar_Barman\t2344\n" +
                      "11\tBarfoo_Fooman\t20\n" +
                      "NULL\t127.0.0.1\t42\n")
reader = mysqltsv.Reader(my_file, types=[int, str, int])
for row in reader:
    print(repr(row.user_id), repr(row['user_text']), repr(row[2]))
