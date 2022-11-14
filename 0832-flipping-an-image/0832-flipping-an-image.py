class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(image)):
            res.append(image[i][::-1])
        for i in range(len(image)):
            for j in range(len(image[0])):
                if res[i][j] == 0:
                    res[i][j] = 1
                else:
                    res[i][j] = 0
        return res
        print(res,image)
        