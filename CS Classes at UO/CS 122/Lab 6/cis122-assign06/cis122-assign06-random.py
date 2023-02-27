import os
from cis122_assign06_shared import pad_left, pad_right
while True:
    # takes the name of a file
    zuko = input("Enter file name (blank to exit): ")
    if len(zuko.strip())== 0:
        break
    elif not os.path.exists(zuko):
        print("Invalid file name: " , zuko)
    else: 
        file = open(zuko)
        # variables
        num_lines = 0 
        comment = 0 
        count = 0 
        total = 0 
        for line in file:
            lines = line.strip()
            num_lines += 1 # counts the line are not comments
            average = (total/num_lines)
            average = round(average, 2)
            if lines[0] != "#":
                count += 1 # counts each line
                total += int(lines) # total number of lines
            else:
                comment += 1 # counts the line that is a comment 
        file.close()
        label_spacing = 10
        num_spacing = 10
        print(pad_right("Count: " , label_spacing) + pad_left(count , num_spacing))
        print(pad_right("Comments: " , label_spacing) + pad_left(comment , num_spacing))
        print(pad_right("Total: " , label_spacing) + pad_left(total , num_spacing))
        print(pad_right("Average: " , label_spacing) + pad_left(average , num_spacing))
