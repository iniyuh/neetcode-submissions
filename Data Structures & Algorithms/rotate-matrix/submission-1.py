class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        def rotate(coords):
            r, c = coords[0]

            for r_, c_ in coords[1:]:
                matrix[r][c], matrix[r_][c_] = matrix[r_][c_], matrix[r][c]
        
        def rotateLayer(layer):
            print("layer", layer)
            M = N - 2*layer

            if M <= 1: return False

            i = 0
            while i < M - 1:
                print("rotating")
                topLeft = (layer, layer + i)
                topRight = (layer + i, layer + M - 1)
                bottomRight = (layer + M - 1, layer + M - 1 - i)
                bottomLeft = (layer + M - 1 - i, layer)

                rotate([topLeft, topRight, bottomRight, bottomLeft])
                i += 1
            
            return True
        
        i = 0
        while rotateLayer(i): i += 1
        print(N)

        return 
