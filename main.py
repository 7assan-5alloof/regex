import re  # To be used for spotting numbers throughout the text

# Find numbers in each line of the file, and add all the results up
file = open(input("Enter file name: "))
sum = int()
count = int()
for line in file:
    line = line.rstrip()  # Important for finding the numbers
    numbers = re.findall("[0-9]+", line)
    if len(numbers) > 0:  # if numbers were found in the line
        for number in numbers:
            count += 1
            sum += int(number)  # Numbers are going to be 'str' type when added
            # to numbers by regex.findall()

print("Count:", count)
print("Sum:", sum)
