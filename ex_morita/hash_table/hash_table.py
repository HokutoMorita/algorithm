import hashlib
from typing import Any


class HashTable(object):
    def __init__(self, size=10) -> None:
        self.size = size
        # sizeの大きさ分の二元リストを作成する
        ## (例) size=5の場合
        ### [[], [], [], [], []]
        self.table = [[] for _ in range(self.size)] 

    def hash(self, key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size
    
    def add(self, key, value) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                # keyが既に存在する場合は、valueを更新する(つまり、上書きする)
                data[1] = value
                break
        else: # こんな書き方できたのか、、、
            # for文が条件を満たさずに、ループ処理がされなかった場合の処理
            self.table[index].append([key, value])

    def print(self) -> None:
        for index in range(self.size):
            print(index, end=' ') # 改行なしで出力
            for data in self.table[index]:
                print('-->', end=' ')
                print(data, end=' ')
            print()#改行

    
    def get(self, key) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

if __name__=='__main__':
    hash_table = HashTable()
    hash_table.add('car', 'Tesla')
    hash_table.add('car', 'Toyota')
    hash_table.add('pc', 'Mac')
    hash_table.add('sns', 'YouTube')
    # print(hash_table.table)
    hash_table.print()
    print(hash_table.get('car'))
