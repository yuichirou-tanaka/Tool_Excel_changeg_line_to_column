"""
下記のテーブルを
100	102	105	107
110	113	115	118
121	124	127	130

に変換する。
100
102
105
107
110
113
115
118
121
124
127
130

"""

import sys

args = sys.argv
#print(args)
#print(len(args))
if len(args) <= 2:
    print("argument 引数2未満.")
    file_input_name = "test.txt"
    file_output_name = "out.csv"
else:
    file_input_name = args[1]
    file_output_name = args[2]

# ----------------
# first pin volt setting
#-----------------
sall_line = []
with open(file_input_name, 'r') as f: 
    sall_line = f.readlines()

#-----------------
# CSV 出力
#-----------------
with open(file_output_name, 'w') as f: 
    
    while len(sall_line) > 0:
        s = sall_line.pop(0)
        s = s.replace("\n","")
        sa = s.split("\t")

        for sab in sa:
            f.write(sab + "\n")

