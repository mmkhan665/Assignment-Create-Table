

table_no = int(input("Enter table number"))
table_range = int(input("PassEnter range of table number"))

for i in range(table_no, table_range+1):
        print(f"{table_no} x {i} = {table_no*i}")