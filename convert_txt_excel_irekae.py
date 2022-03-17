import sys

args = sys.argv
#print(args)
#print(len(args))
if len(args) <= 3:
    print("argument 引数3未満.")
    file_input_name = "test.txt"
    file_output_name = "out.csv"
    count_retu = 4
    #print(args)
    #exit()
else:
    file_input_name = args[1]
    file_output_name = args[2]
    count_retu = int(args[3])

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
        fs = []
        for i in range(count_retu):
            if len(sall_line) <= 0: 
                break
            s = sall_line.pop(0)
            s = s.replace("\n","")
            #fs.append(s)
            f.write(s + ",")
        f.write("\n")
        #f.write()

