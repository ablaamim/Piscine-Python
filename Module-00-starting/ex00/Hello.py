ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here

# Lists are mutable, tuples are not
ft_list[1] = "World!";

ft_tuple = ("Hello", "Morocco!") # tuples are immutable

# Sets are mutable, but they are unordered and unindexed
ft_set.discard("tutu!") # remove() raises an error if the item does not exist
#ft_set.discard("tutu!") # discard() does not raise an error if the item does not exist
ft_set.add("Benguerir!")
# second = set(ft_list) # copy the set
# print(second | ft_set) # union
# print(second & ft_set) # intersection

# Dictionaries are mutable, unordered and indexed
ft_dict["Hello"] = "1337-Benguerir!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)