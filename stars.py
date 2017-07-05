import sys
def draw_stars(nums):
    for i in range(0, len(nums)):
        if isinstance(nums[i], int):
            for j in range(0, nums[i]):
                sys.stdout.write("*")
            print
        else:
            for j in range(0, len(nums[i])):
                sys.stdout.write(nums[i][0].lower())
            print
draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])