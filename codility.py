def solution(A):
        N = len (A)
        present_arr = [ False] * (N + 1)

        for num in A:
            if 1 <= num <= N:
                present_arr[num] = True

        for i in range(1, N+1):
            if not present_arr[i]:
                return i
        return N + 1

print(solution([1, 3, 6, 4, 1, 2]))

py