branch = int(input('Vui lòng nhập số chi nhánh : '))
result = ""
for i in range(1,branch+1):
    print(f'Chi nhánh {i}: ')
     
    for j in range(1,4):
        revenue_in_month = int(input(f'Tháng {j}: '))
        result = result + f'Chi nhánh {i}, ' + f'tháng {j}: ' + str(revenue_in_month) + ' triệu đồng \n'

print('\n------ KẾT QUẢ ------')
print(result)
    