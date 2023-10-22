from base_tester.tester import TestResults

class Solution(TestResults):

    def contains_duplicate(self, nums: str) -> bool:
        return len(set(nums)) != len(nums) 


    def test(self):
        test_cases = [
            ([1,2,3,1], True),
            ([1,2,3,4], False),
            ([1,1,1,3,3,4,3,2,4,2], True)
        ]
        result = True
        for test_case in test_cases:
            result = result and (self.contains_duplicate(test_case[0]) == test_case[1])
        
        return result


if __name__ == '__main__':
    Solution().run_tests()    