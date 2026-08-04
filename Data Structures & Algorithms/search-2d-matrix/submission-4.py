class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Given
        #matrix = [[]] #At some mxn array
        #target = 0 #integer

        #m = # of nested arrays (aka columns)
        #n = # of elements in each nested arrays

        m_low, m_high = 0, len(matrix) - 1

        while m_low <= m_high: #while m window columns have not closed
            m_mid = m_low + (m_high - m_low) // 2
            # First check if target is within the range of this row
            if target < matrix[m_mid][0]: #if target is less than the lowest element in the matrix[m_mid] nested array
                m_high = m_mid - 1
                continue
            if target > matrix[m_mid][-1]: #if target is higher than the highest element in the matrix[m_mid] nested array
                m_low = m_mid + 1
                continue
            else:
                #target is within the lowest and highest elements of the current nested array
                n_low, n_high = 0, len(matrix[m_mid]) - 1
                while n_low <= n_high: #while n window rows have not closed
                    n_mid = n_low + (n_high - n_low) // 2
                    #Now on m_mid's nested array at matrix[m_mid]]0 --> n-1]
                    if matrix[m_mid][n_mid] < target: #too small, inc: new window of n_mid+1 = new low
                        n_low = n_mid+1 #move up n_low
                    elif matrix[m_mid][n_mid] > target: #too large, dec: new iwndow of n_mid-1 = new high
                        n_high = n_mid-1 #move up n_high
                    else: #found
                        return True
                
                #Went through all of n windows in the m_mid nested array that the target could only be in if that value is in the array, but could not find
                return False

        return False #Target was not found in ranges of any of the m nested arrays

#object declaration
object1 = Solution()

#Given:
matrix1 = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target1 = 10

matrix2 = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target2 = 15

#Test cases:
object1.searchMatrix(matrix1, target1)
object1.searchMatrix(matrix1, target1)