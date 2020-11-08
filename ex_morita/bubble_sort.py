from typing import List

"""
Bubble sortのオーダー数
- Average: O(n**2)
- Best: O(n)
- Worst: O(n**2)
"""

def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i): 
            # だからO(n**2)になるのか！！
            ## 加えて、-iとすることで、limitを一つずつずらしている
            if numbers[j] > numbers[j+1]:
                # 左側にある要素が右側にある要素よりも大きい場合は、要素を入れ替える
                tmp_j = numbers[j]
                tmp_j_1 = numbers[j+1]
                numbers[j] = tmp_j_1
                numbers[j+1] = tmp_j
    return numbers


if __name__=='__main__':
    nums = [2, 5, 1, 8, 7, 3]
    result = bubble_sort(nums)
    print(result)

    import random
    nums_random = [random.randint(0, 1000) for i in range(10)]
    print(bubble_sort(nums_random))
