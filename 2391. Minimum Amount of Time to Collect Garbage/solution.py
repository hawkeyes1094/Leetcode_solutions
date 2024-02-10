class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        max_index = [-1,-1,-1]
        find_count = 0
        for i in range(len(garbage),0,-1):
            if max_index[0] == -1 and 'G' in garbage[i-1]:
                max_index[0] = i-1
                find_count = find_count + 1
            if max_index[1] == -1 and 'P' in garbage[i-1]:
                max_index[1] = i-1
                find_count = find_count + 1
            if max_index[2] == -1 and 'M' in garbage[i-1]:
                max_index[2] = i-1
                find_count = find_count + 1
            if find_count == 3:
                break
        
        # print("max_index:", max_index)
        # Create a hashmap/dictionary which contains the number of items of each type
        garbage_count = {'G':0,'P':0,'M':0}
        for i in range(0, len(garbage)):
            for item in garbage[i]:
                garbage_count[item] = garbage_count[item] + 1
        
        # print("Count:", garbage_count)
        result = garbage_count['G'] + garbage_count['P'] + garbage_count['M']
        for i in range(0, len(travel)):
            for j in range(0,3):
                if i < max_index[j]:
                    result = result + travel[i]
                    

        return result