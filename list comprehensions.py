names=["Sudheshna","Srujan","Keerthana","Honey","Deepika","Samskruti","Shruti","Prashanthi"]
s_names=[]
for name in names:
    if "s" in name.lower():
        s_names.append(name)
# print(name)
print("These people have the letter 's' in their name: ",s_names)
# # s_names=[name for name in names if 's' in name]
# # print(s_names)
# names_copy=[name for name in names]
# print(names_copy)

## exercise
animals=['lion', 'tiger', 'monkey', 'elephant', 'frog']
filtered_animals=[animal.title() for animal in animals ]
print(filtered_animals)