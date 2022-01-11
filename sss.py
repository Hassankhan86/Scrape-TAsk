import csv

l = ['aaa', 'bbb', 'ccc']

s = ' '.join(l)

print(s)


O = s.split(" ")
print(O)

# file = open('topyoutubers.csv', 'w',encoding='utf8')
# writer = csv.writer(file)

# # write title row
# writer.writerow(['Username', 'Uploads', 'Views'])


# with open('combined_file.csv', 'w', newline='') as outcsv:
#     writer = csv.writer(outcsv)
#     writer.writerow(["Date", "temperature 1", "Temperature 2"])
# l = [[1, 2], [2, 3], [4, 5]]

# out = open('out.csv', 'w')
# for row in l:
#     for column in row:
#         out.write('%d;' % column)
#     out.write('\n')
# out.close()


# with open('test.csv', 'wb') as f:
#     wtr = csv.writer(f, delimiter= ' ')
#     wtr.writerows( [[1, 2], [2, 3], [4, 5]])

# with open('test.csv', 'r') as f:
#     for line in f:
#         print(line)


# file = open('topyoutubers.csv', 'w',encoding='utf8')
# writer = csv.writer(file)

# # write title row
# writer.writerow(['Name', 'Price','Vin', 'Summary', 'Features'])
# while True:
#     channels = [1,2,3,4,5,6,7,8]

#     # print(username + ' ' + uploads + ' ' + views)
#     writer.writerow([channels])
num_of_loops = 10
while num_of_loops > 0:
    print(num_of_loops)
    num_of_loops = num_of_loops -1
