months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

new_list = list()
for word in months:
    if "r" in word:
        new_list.append(word)
print(new_list)
