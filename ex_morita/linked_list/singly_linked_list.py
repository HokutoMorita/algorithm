from __future__ import annotations
from typing import Any


class Node(object):
    def __init__(self, data: Any, next_node: Node = None):
        self.data = data
        self.next = next_node

class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head
    
    def append(self, data: Any) -> None:
        """
        ノードの接尾に新しいノードを追加する
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next: # last_node.nextがNoneになるまでループ
            last_node = last_node.next
        
        # 最後のノードの次のノードとして、Newノードを追加
        last_node.next = new_node
    
    def insert(self, data: Any) -> None:
        """
        ノードの先頭に新しいノードを追加する
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def print(self) -> None:
        current_node = self.head
        while current_node: # current_nodeがNoneになるまでループ
            print(current_node.data)
            current_node = current_node.next
    
    def remove(self, data: Any) -> None:
        current_node = self.head
        if current_node and current_node.data == data:
            # 削除対象のデータが先頭のノードにある場合の処理
            self.head = current_node.next
            current_node = None
            return 

        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
        
        if current_node is None:
            # whileループを抜けて、current_nodeがNoneになる場合は、削除対象のデータがLinkedList内になかったことになる
            return
        
        # 削除対象のデータがあるノード(current_node)を外して、LinkedListを繋ぎ直す処理
        previous_node.next = current_node.next
        current_node = None
    
    def reverse_iterative(self) -> None:
        """
        LinkedListの要素の順番を逆向きに並べ替える
        """
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node
        self.head = previous_node
    
    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node, previous_node: Node):
            if not current_node: # current_nodeがNoneの場合
                return previous_node
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

            return _reverse_recursive(current_node, previous_node)
        
        self.head = _reverse_recursive(self.head, None)

if __name__=='__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.insert(0)
    l.print()
    print("#####")
    l.remove(2)
    l.print()
    print("#####")
    # l.reverse_iterative()
    l.reverse_recursive()
    l.print()
    # print(l.head.data)
    # print(l.head.next.data)
    # print(l.head.next.next.data)
    # print(l.head.next.next.next.data)
