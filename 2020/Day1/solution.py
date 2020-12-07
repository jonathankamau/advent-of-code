
class Sum:

    def readFile(self):

        nums = []
        file = open('input.txt', 'r')

        for line in file:
            nums.append(int(line))
        return nums

    def getTwoSum(self, year):

        nums = self.readFile()

        for num in nums:
            second_num = year - num
            if second_num in nums:
                result = second_num * num
                break
            else:
                result = 0

        return result

    def getThreeSum(self, year):

        nums = self.readFile()
        print('nums', nums)

        second_pair = 0

        for num in nums:
            second_pair = year - num
            second_result = self.getTwoSum(second_pair)
            if second_result > 0:
                result = num * second_result
                break
            else:
                result = 0

        return result


sumclass = Sum()

print('two sum', sumclass.getTwoSum(2020))
print('three sum', sumclass.getThreeSum(2020))
