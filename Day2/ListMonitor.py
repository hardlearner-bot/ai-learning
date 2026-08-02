import sys

lst = []
prev_size = sys.getsizeof(lst)
for a in range(20):
    lst.append(a)
    curr_size = sys.getsizeof(lst)
    if curr_size != prev_size:
        print(f"元素数量:{len(lst)}，列表的内存从{prev_size} 变为{curr_size}字节")
        prev_size = curr_size
