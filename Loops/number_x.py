nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 0
while i <= len(nums) - 1:
    print(nums[i])
    i += 1 

# print all heroes
heroes = ["ironman", "thor", "superman", "batman"]
idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1

# search for number x in the given tuple
numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
x = 36
j = 0
while j < len(numbers):
    if(numbers[j]==x):
        print("The number", numbers[j], "is found at index", j)
    else:
        print("finding....")
    j += 1
    print("End of loop")