#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Song:
    """플레이리스트 음악 노드 클래스"""
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None

class PlayList:
    '''플레이리스트 클래스'''
    def __init__(self):
        self.head = None
        self.current = None

    def printList(self):
        print '플레이리스트:'
        node = self.head
        while (node is not None):
            print "%s" % node.title
            last = node
            node = node.next

    def append(self, newData):
        NewSong = Song(newData)

        if self.head is None:
            self.head = NewSong
            return
        last = self.head

        while(last.next):
            last = last.next

        last.next = NewSong
        NewSong.prev = last

    def playSong(self, selection):
        pointer = self.head
        while pointer != None:
            if str(pointer.title) == str(selection):
                self.current = pointer
                print self.current.title
                return
            
            pointer = pointer.next

        print '\n노래를 찾을 수 없습니다'
        return

    def getPrev(self):
        if self.current.prev == None:
            print "\n앞으로 갈 노래가 없습니다"
            return

        self.playSong(self.current.prev.title)

# 실행 코드
list1 = PlayList()
list1.append("The Climb")
list1.append('Hello')
list1.append("Bad Blood")

list1.printList()

list1.playSong("Bad Blood")
list1.getPrev()
list1.getPrev()

list1.getPrev()
list1.playSong("Hi")
list1.getPrev()
