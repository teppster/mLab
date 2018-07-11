import sys
import json

#command line argument
input_json = sys.argv[1]

# change it into a dictionary object
parsed_json = json.loads(input_json)

# recursively find the path to al the values
def findPath(d):
    #set up an empty dictionary
    results = {}

    # check all the values in the dictionary
    # if it is not another dictionary, then create a key - value pair
    # else recursively call the findPath and concatenate the key with all the keys returned from the dictionary.
    for key in d:

        if isinstance(d[key], dict):
            temp = findPath(d[key])

            for k in temp:
                results[key + '.' + k] = temp[k]
        else:
            results[key] = d[key]
    return results

print(findPath(parsed_json))

