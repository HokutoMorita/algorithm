from typing import List

"""
Quick sortのオーダー数
- Average: O(n * log n)
- Best: O(n * log n)
- Worst: O(n**2)
"""

def partition(numbers: List[int], low: int, high: int) -> int:
    """
    配列を左側と右側に分ける
    pivotの最終的な位置を示すインデックス番号を返す
    """
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high): # lowからhighまでforループ
        if numbers[j] <= pivot:
            i += 1
            tmp_i = numbers[i]
            tmp_j = numbers[j]
            numbers[i] = tmp_j
            numbers[j] = tmp_i

    # pivotに入っていた値とi+1番目の値を入れ替える
    tmp_i_1 = numbers[i+1]
    tmp_high = numbers[high]
    numbers[i+1] = tmp_high
    numbers[high] = tmp_i_1
    return i+1 # pivotの最終的な位置を示すインデックス番号を返す


def quick_sort(numbers: List[int]) -> List[int]:
    """
    普通に難しいから、Udemyの動画を見直した方がいいかも
    """
    def _quick_sort(numbers: List[int], low: int, high: int) -> None:
        """
        インナー関数
        """
        if low < high:
            partition_index = partition(numbers, low, high)
            # 左側のソート
            _quick_sort(numbers, low, partition_index-1)
            # 右側のソート
            _quick_sort(numbers, partition_index+1, high)

    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers


if __name__=='__main__':
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(quick_sort(nums))
