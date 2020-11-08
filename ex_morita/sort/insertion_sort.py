from typing import List

"""
Insertion sort(挿入ソート)のオーダー数
- Average: O(n**2)
- Best: O(n)
- Worst: O(n**2)
"""

def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        # 1オリジンとなる
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            # tempに入っている値が配列の左側にある値より小さい場合は、適切な位置に行くまで、左にずらし続ける
            numbers[j+1] = numbers[j]
            j -= 1
            numbers[j+1] = temp
    return numbers

if __name__=='__main__':
    nums = [2, 5, 1, 8, 7, 3]
    result = insertion_sort(nums)
    print(result)

    import random
    nums_random = [random.randint(0, 1000) for i in range(10)]
    print(insertion_sort(nums_random))
