import numpy as np

class Solution:
    def solve(self):
        flag = False

        print('Generating...')
        # print('==================LOG==================')
        while True:
            # Generate random from range 0 -> 5 of size 4x4 Matrix
            A = np.random.randint(-3, 3, size = (4, 4))

            # np.linalg.eig return a pair of eigenvalues and eigenvector
            evalue, evect = np.linalg.eig(A)
            
            # If 'j' exist in evalue --> Matrix can not be diagonalized normally
            for i in evalue:
                if 'j' not in str(i):
                    flag = True
                    break
            
            if flag: break
            else: pass
        # print('==================LOG==================')

        self.printSolution(A, evalue, evect)
        self.calculateA_100(A, evalue, evect)
        

    def printSolution(self, A, evalue, evect):
        print(f'Diagonalizable matrix successfully generated: \n{A}')

        # The eigenvalues must be unique
        print(f'\nIts eigenvalues is: {evalue}')       
        
        # The result differs because of the scalar
        print(f'\nIts eigenvectors is: \n{evect}')


    def calculateA_100(self, A, evalue, evect):
        p = evect
        print(f'\nModal matrix P, which also is eigenvectors: \n {p}')

        d = np.zeros((4, 4))
        for i in range(4):
            d[i, i] = evalue[i]

        print(f'\nDiagonalized matrix D of matrix A is: \n{d}')

        p_inv = np.linalg.inv(p)
        print(f'\nInversion of model matrix P^-1 = \n{p_inv}')

        s1 = np.linalg.matrix_power(d, 100) # Raise the diagonalized matrix to the power of 100
        s2 = np.dot(p, s1) # 
        s3 = np.dot(s2, p_inv)
        print(f'\nA^100 = P * D^100 * P^-1 = \n{s3}')

        # One liner solution, but result is overflow if raise to the power of 100
        # print(f'\nA^100 = P * D^2 * P^-1 = \n{np.linalg.matrix_power(A, 100)}')

if __name__ == '__main__':
    x = Solution()
    x.solve()