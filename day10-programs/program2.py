school_friends = ['John', 'Alice', 'Bob', 'David'] 
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

print("School friends: ", school_friends)
print("College friends: ", college_friends)

all_friends = set(school_friends) | set(college_friends)
print("All unique friends (using set | operator): ", list(all_friends))

all_friends_union = set(school_friends).union(set(college_friends))
print("All unique friends (using union method): ", list(all_friends_union))