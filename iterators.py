# nums=[1,2,3,4]
# # for i in nums:
# #     print(i)
#
# it=iter(nums)
# print(it.__next__())
# print(next(it))
# # for i in nums:
# #     print(i)

class TopTen:
    def __init__(self):
        self.num=1
    def iter(self):
        return self
    def __next__(self):
        val=self.num
        self.num+=1
        return val
values=TopTen()
for i in values:
    print(i)