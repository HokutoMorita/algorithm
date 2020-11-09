from typing import List

"""
Merge sortのオーダー数
- Average: O(n * log n)
- Best: O(n * log n)
- Worst: O(n * log n)
"""

def merge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers
    center = len(numbers) // 2 # 割り算の結果を整数にしたいときは、演算子「//」を使う
    left = numbers[:center] # centerよりも左側のリストを抽出
    right = numbers[center:] # centerよりも右側のリストを抽出
    
    merge_sort(left)
    merge_sort(right)

    # インデックス番号の初期化
    i = 0 # leftのインデックス番号
    j = 0 # rightのインデックス番号
    k = 0 # numbersのインデックス番号
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # 左側の要素方が小さい場合は、左側の要素をnumbersのk番目に入れる
            numbers[k] = left[i]
            i += 1
        else:
            # 右側の要素方が小さい場合は、右側の要素をnumbersのk番目に入れる
            numbers[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1
    
    return numbers

if __name__=='__main__':
    nums = [5, 4, 1, 8, 7, 3, 2, 9]
    result = merge_sort(nums)
    print(result)

    import random
    nums_random = [random.randint(0, 1000) for i in range(10)]
    print(merge_sort(nums_random))
