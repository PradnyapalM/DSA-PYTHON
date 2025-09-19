# Level 2
# Q1 Count Character
# eg "hello"->{h:1,e:1,l:2,o:1}
"""
freq = {}
data = "hello"
for item in data:
    freq[item] = freq.get(item,0)+1
print(freq)
"""

# Q 2 Wap to count frequently elements of array
"""
def count_frequency_basic(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item,0)+1
    return freq

arr = [1,2,3,2,1,3,3]
print(count_frequency_basic(arr))
"""

# Q3  Find the most frequent element in the array

def count_frequency_basic(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item,0)+1
    return freq

def find_most_frequent(arr):
    freq = count_frequency_basic(arr)
    max_count = 0
    most_frequent = None

    for item, count in freq.items():
        if count>max_count:
            max_count = count
            most_frequent = item
    return most_frequent, max_count

arr = [1,2,3,2,1,3,3,3]
print(find_most_frequent(arr))