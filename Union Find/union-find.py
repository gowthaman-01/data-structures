class Union:
    def __init__(self, elements):
        self.elements = {}
        self.size = {}
        for element in elements:
            self.elements[element] = element
            self.size[element] = 1

    def find(self, element):
        if self.elements[element] == element:
            return element
        else:
            self.elements[element] = self.find(self.elements[element])
            return self.elements[element]

    def combine(self, element1, element2):
        element1 = self.find(element1)
        element2 = self.find(element2)
        if element1 == element2:
            return

        else:
            if self.size[element1] <= self.size[element2]:
                self.elements[element1] = element2
                self.size[element2] += self.size[element1]
            else:
                self.elements[element2] = element1
                self.size[element1] += self.size[element2]


union = Union(["NUS", "MIT", "SMU", "UIUC", "CMU", "HV", "NTU"])

union.combine("NUS", "NTU")
union.combine("NUS", "SMU")
union.combine("MIT", "UIUC")
union.combine("CMU", "UIUC")
union.combine("HV", "UIUC")

print(union.elements)
