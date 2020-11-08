from typing import List

"""
Selection sort(選択ソート)のオーダー数
- Average: O(n**2)
- Best: O(n**2)
- Worst: O(n**2)
"""

def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        # 最小値となる要素を指し示すインデックス
        min_idx = i
        for j in range(i+1, len_numbers):
            # i+1番目から、forループする
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        
        # i番目の要素と最小値を入れ替える
        tmp_i = numbers[i]
        tmp_min_i = numbers[min_idx]
        numbers[i] = tmp_min_i
        numbers[min_idx] = tmp_i
    return numbers

if __name__=='__main__':
    nums = [2, 5, 1, 8, 7, 3]
    result = selection_sort(nums)
    print(result)

    import random
    nums_random = [random.randint(0, 1000) for i in range(10)]
    print(selection_sort(nums_random))
