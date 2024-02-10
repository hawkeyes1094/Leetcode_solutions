def sort_key(range):
    return range[0]

class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = sort_key)
        answer = [intervals[0]]
        j = 0
        for i in intervals:
            if i[0] <= answer[j][1]:
                answer[j][1] = max(answer[j][1], i[1])
            else:
                answer.append(i)
                j = j + 1

        return answer