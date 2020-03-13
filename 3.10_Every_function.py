# Write a program that creates a list of items and uses each function introduced in this chapter at least once.

languages = ['russian','belarusian','english','french']
print(languages)
languages.append('japanese')
print(languages)
#if i use -1 instead of 4, then 'german' goes before 'japanese', 
#it means insert() function put an element exactly at place -1, where 'japanese' now, so 'japanese' becomes shifted to the right
languages.insert(6,'german')
print(languages)
#used pop() function
popped_language = languages.pop()
print(popped_language)
print(languages)
del languages[-2]
print(languages)

#used sorted() function to print my list in alphabetical order without modifying the actual list.
print(sorted(languages))
print(languages)
#used reverse() to change the order of my list and than back it actual list.
languages.reverse()
print(languages)
languages.reverse()
# used sort() to change my list so it’s stored in alphabetical order. 
print(languages)
languages.sort()
print(languages)
print(f"Languages you know:{len(languages)}")
