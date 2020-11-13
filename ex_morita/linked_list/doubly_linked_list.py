from __future__ import annotations
from typing import Any, Optional


class Node(object):
    def __init__(self, data: Any, next_node: Node = None, prev_node: Node = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList(object):
    """
    双方向リンクリスト
    """
    def __init__(self, head: Node = None) -> None:
        self.head = head
    
    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next: # current_node.nextがNoneになるまでループ
            current_node = current_node.next
        
        # 双方向にリンクさせる
        current_node.next = new_node
        new_node.prev = current_node
    
    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        # 双方向にリンクさせる
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
    
    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def remove(self, data: Any) -> Node:
        current_node = self.head

        # 先頭部分のノードを削除
        if current_node and current_node.data == data:
            if current_node.next is None:
                current_node = None
                self.head = None
                return
            else:
                next_node = current_node.next
                next_node.prev = None
                current_node = None
                self.head = next_node
                return
        
        while current_node and current_node.data != data:
            current_node = current_node.next
        
        if current_node is None:
            return
        
        
        if current_node.next is None:
            # 接尾部分のノードを削除
            prev = current_node.prev
            prev.next = None
            current_node = None
            return
        else:
            # 双方向リンクリストの真ん中にあるノードを削除
            next_node = current_node.next
            prev_node = current_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None
            return


if __name__=='__main__':
    d = DoublyLinkedList()
    d.append(1)
    d.append(2)
    d.append(3)
    # print(d.head.data)
    # print(d.head.next.data)
    # print(d.head.next.next.data)
    # print(d.head.next.next.prev.data)
    # print(d.head.next.next.prev.prev.data)
    d.print()
    print("####")
    d.insert(4)
    # print(d.head.data)
    # print(d.head.next.data)
    # print(d.head.next.next.data)
    # print(d.head.next.next.prev.data)
    # print(d.head.next.next.prev.prev.data)
    d.print()
    print("####")
    d.remove(2)
    d.print()
