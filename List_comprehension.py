friends = ["sam", "samantha", "siraj", "Lionel"]
starts_s =[friend for friend in friends if friend.startswith("s")]
print(starts_s)
print("friends:", id(friends), "starts_s:",id(starts_s))

# 1. Find all of the numbers from 1–1000 that are divisible by 8

#  div7 = [n for n in range(1,1000) if n % 7 == 0] 
#  print(div7)
a=[i for i in range(1000)]
nums = [num for num in a if num % 8 == 0]
print(nums)
