import random 
import time

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def merge(S1, S2, S):
    i = j = 0
    n, m = len(S1), len(S2)
     
    while i < n and j < m:
        if S1[i] <= S2[j]:
            S[i + j] = S1[i] 
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1
    # adding unassigned elements
    while i < n:
        S[i + j] = (S1[i])
        i += 1

    while i < n:
        S[i +j] =  (S2[j])
        j += 1

def merge_sort(S):
    n = len(S)
    if n < 2:
        return
    mid = n//2
    S1 = S[:mid]
    S2 = S[mid:]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)
    return S

def quick_sort(a):
    if len(a) <= 1:
        return a
    
    left = []
    right = []
    pivot = a[0]

    for element in a:
        if element >= pivot:
            right.append(element)
        else:
            left.append(element)

    left = quick_sort(left)
    right = quick_sort(right[1:])
    return left + [pivot] + right

def check_bubble(test_num, sort):
    avg = []
    pass_count = 0
    for _ in range(10):
        array = [random.randint(-x, x) for x in range(test_num)]
        print('Tested for :', array)
        start = time.time()
        gen = sort(array)
        avg.append(time.time() - start)

        sol = sorted(array)
        if gen == sol:
            print('Passed, The sorted array:', gen)
            pass_count += 1
        else:
            print('Fail, The sorted array:', sol, 'and Generated array:', gen)
    
    print(sum(avg) // len(avg))

def check_merge(test_num, sort):
    avg = []
    for _ in range(10):
        array = [random.randint(-x ,x) for x in range(test_num)]
        print('Tested for :', array)
        start = time.time()
        gen = merge_sort(array)
        avg.append(time.time() - start)
        sol = sort(array)

        if gen == sol:
            print('Passed, The sorted array:', gen)
            pass_count += 1
        else:
            print('Fail, The sorted array:', sol, 'and Generated array:', gen)
    
    print(sum(avg)// len(avg))

def check_quick(test_num, sort):
    avg = []
    for _ in range(10):
        array = [random.randint(-x ,x) for x in range(test_num)]
        print('Tested for :', array)
        start = time.time()
        gen = quick_sort(array)
        avg.append(time.time() - start)
        sol = sort(array)

        if gen == sol:
            print('Passed, The sorted array:', gen)
            pass_count += 1
        else:
            print('Fail, The sorted array:', sol, 'and Generated array:', gen)
    
    print(sum(avg) // len(avg))