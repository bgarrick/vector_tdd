class Vector:
    def __init__(self, nums):
        self.nums = nums
        self.dims = len(nums)
        self.norm = self._length()

    def __eq__(self, other):
        return self.nums == other.nums

    def _length(self):
        return sum([i**2 for i in self.nums]) ** 0.5

    def unit_vector(self):
        return Vector([i/self.norm for i in self.nums])
    
    def scale(self, s):
        return Vector([i*s for i in self.nums])