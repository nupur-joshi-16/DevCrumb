# Number manipulation

height = 1.65
weight = 84

bmi = weight/(height*height)
print(bmi)


# round number
print(round(bmi))

# 3.3 => 3
# 3.9 => 4

print(round(bmi, 2))


# assign operators

# Shorthand
score = 10
print(score) #10
score += 5
print(score) #15
score -= 1
print(score) #14
score *= 2
print(score) #28
score /= 2
print(score) #14.0

# f-string
height = 1.8
is_winning = True
print(f"User score: {score}, User height: {height}, User win? {is_winning}")

