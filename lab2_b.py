# CS3
# Angel Rodriguez II
# Lab 2 - Option B
# Diego Aguirre
# 09-25-2019
# Purpose: The purpose of this code is to read a given text file, store the passwords into a linked list,
#           sort the passwords using either a merge sort or bubble sort algorithm, then lastly this code will
#           return the top 20 most seen passwords in the text file.

import time
from node import Node
import sys
list = []

def has_been_created(password):
    temp2 = head
    while temp2.next != None: # traverses the linked list
        if temp2.password == password: # if the comparison is true, then the node count gets incremented by 1
            temp2.count += 1
            return True
        else: # otherwise, the node gets added to the linked list
            temp2 = temp2.next
    return False

def swap(temp1, temp2): # this method swaps the nodes sent in the paramater by changing the data
    temp.password = temp1.password # Creates a temp node and stores the data from temp1
    temp.count = temp1.count
    temp1.password = temp2.password # makes temp1 data equal to temp2
    temp1.count = temp2.count
    temp2.password = temp.password # makes temp2 data the same as temp, which was the same as temp1 before it was changed
    temp2.count = temp.count

def print_linkedlist(head): # prints the linked list
    temp = head
    while temp is not None:
        print(temp.password)
        print(temp.count)
        temp = temp.next
    print('-----------------------')

def print_last_i_nodes(head, k): # prints the last number of specified numbers in the linked list utilizing a double pointer technique
    temp1 = head
    temp2 = head
    for i in range(k): # sets the first pointer ahead a fixed amount of nodes
        temp1 = temp1.next
    while temp1.next is not None: # moves both pointers at the same rate until the first pointer reaches the end of the linked list
        temp1 = temp1.next
        temp2 = temp2.next
    while temp2.next is not None:  # the 2nd pointer is now at the end of the linked list minus how many nodes
                                   # you wanted to print, then it prints all the nodes until it reaches the end of the linked list
        print(temp2.next.password)
        print(temp2.next.count)
        temp2 = temp2.next

def get_mid_node(head): # returns the middle node of the linked list
    temp = head
    mid_val = (len_of_linkedlist(temp)) // 2 # calls the method that returns the length of the linked list and divides the value by 2
    for i in range(mid_val): # moves the temp pointer n/2 times to reach the middle of the linked list
        temp = temp.next
    mid_node = temp
    return mid_node

def sorted_merge(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.count <= b.count:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)
    return result

def merge_sort(head):
    temp = head
    if temp is None or temp.next is None:
        return temp
    mid = get_mid_node(temp) #find the middle of the linked list and sets it to mid
    after_mid = mid.next # creates the head of the right part of the linked list
    mid.next = None # cuts off the left linked list from the right
    left = merge_sort(temp) # recursively calls until the base case is reached
    right = merge_sort(after_mid) # recursively calls until the base case is reached
    sorted_list = sorted_merge(left, right)
    return sorted_list # returns the head of the sorted list

def bubble_sort_linked_list(Node):
    for i in range(len_of_linkedlist(Node)):
        head = Node
        swapped = False # will be used later in this method to check if any swaps were made, also resets swapped to False each iteration
        while head.next is not None:
            temp1 = head # assigns temp1 to equal head node
            temp2 = temp1.next # assigns temp2 to equal temp1.next, which is also equal to head.next
            if temp1.count > temp2.count: # comparison of the count values
                swap(temp1, temp2) # calls the swap method
                swapped = True # sets boolean swapped to equal True
            head = head.next
        if swapped == False: # if the swapped value remains False, then no changes were made to the linked list, which means the list is already in order
            break

def len_of_linkedlist(Node): # method that returns the length of a linked list
    temp = Node
    counter = 0
    while temp.next != None:
        counter += 1
        temp = temp.next
    return counter

with open("passwords.txt", "r") as f: # opens the given file name in read mode and closed the file when the code is finished executing
    for line in f:
        # print(line, end="")
        current_line = line.split() # splits the lines in the text file where there is white space
        if len(current_line) == 2: # this is only here because some of the lines in the HUGE text file are missing the passwords
                                   # so, this ensures that the loop can execute properly
            user_name = current_line[0]
            user_password = current_line[1]
            list.append(user_password) # appends the passwords to a list

dict = {}
list_with_duplicates = []
for i in range(len(list)):
    list_with_duplicates.append(str(list[i]))
for item in list:
   if item in dict: # You can assume this operation takes O(1)
       dict[item] = dict[item] + 1
   else:
       dict[item] = 1
# print(dict["wish"]) # 2
# print(dict["here"]) #1

head = Node(list[0], 0, None)
temp = head

for i in range(1, len(list)):
    temp = Node(list[i], 0, None) # creates temp node
    if(has_been_created(list[i])) == False: # calls the has_been_created method and checks if it returns False
        temp.next = head
        head = temp



# print_linkedlist(head)
# temp1 = head.next
# temp2 = head.next.next
# print(temp1.password)
# print(temp2.password)
# swap(temp1, temp2)
# print_linkedlist(head)

# middle_node = get_mid_node(head)
# print(middle_node.password)
# print(middle_node.count)
# print_last_i_nodes(head, 2)
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
# start = time.time()
merge_sort(head)
# bubble_sort_linked_list(head)
# end = time.time()
print_linkedlist(head)
print_last_i_nodes(head, 20)
# print(end - start)


# print(len(list))
# merge_sort(head) # works properly
# # print_linkedlist(head)
# print_last_i_nodes(head, 2)

# print_linkedlist(head)




