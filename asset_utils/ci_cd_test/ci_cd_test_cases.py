import bin_search

test_cases = {
    "case1": {
        "array":[1,2,3,4,5,6,7,8],
        "target": 2,
        "result": 1
    },
    "case2": {
        "array":[2,3,5,6,7,8,12,34,78],
        "target": 5,
        "result": 2
    },
    "case3": {
        "array":[32,43,45,76,78,98],
        "target": 2,
        "result": -1
    },
}

all_test_cases_passed = []

for test_case in test_cases.values():
    res = bin_search.binSearch(test_case["array"],test_case["target"])
    if res == test_case["result"]:
        print("Test case passed!")
        all_test_cases_passed.append(1)
    else:
        print("Test case failed!")
        all_test_cases_passed.append(0)

if len(set(all_test_cases_passed)) == 1:
    print("All test cases passed!!")
else:
    print("All test cases failed!!")
