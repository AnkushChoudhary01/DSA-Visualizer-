import time
import pygame

def bubble_sort(arr, draw, delay):
    print("Bubble Sort started")
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            pygame.event.pump()  # keeps the window responsive
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw(arr)
                time.sleep(delay / 1000)  # delay in seconds

def insertion_sort(arr, draw, delay):
    print("Insertion Sort started")
    for i in range (1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key< arr[j]:
            pygame.event.pump()
            arr[j+1] = arr[j]
            j -= 1
            draw(arr)
            time.sleep(delay/1000)
        arr[j+1] = key
        draw(arr)
        time.sleep(delay/1000)

def selection_sort(arr, draw, delay):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            pygame.event.pump()
            if arr[j] < arr[min_index]:
                min_index = j
            draw(arr)
            time.delay(delay/1000)
        arr[i], arr[min_index] = arr[min_index], arr[i]
        draw(arr)
        time.delay(delay/1000)

def merge_sort(arr, draw, delay):
    def merge_sort_recursive(start, end):
        if end -start >1:
            mid = (start+end)//2
            merge_sort_recursive(start,mid)
            merge_sort_recursive(mid,end)
            merge(start,mid,end)
            draw(arr)
            time.sleep(delay/1000)
    def merge(start,mid,end):
        left = arr[start:mid]
        right = arr[mid:end]
        i = j = 0
        k = start
        while i < len(left) and j <len(right):
            pygame.event.pump()
            if left[i] < right[j]:
                arr[k]= left[i]
                i +=1
            else:
                arr[k] = right[j]
                j +=1
            k +=1
        draw(arr)
        time.sleep(delay/1000)
        while i < len(left):
            pygame.event.pump()
            arr[k] = left[i]
            i+=1
            k+=1
            draw(arr)
            time.sleep(delay/1000)
        while j < len(right):
            pygame.event.pump()
            arr[k] = right[j]
            j+=1
            k+=1
            draw(arr)
            time.sleep(delay/1000)
        
    merge_sort_recursive(0,len(arr))

def quick_sort(arr, draw, delay):
    def quick_sort_recusive(left,right):
        if left < right:
            pivot_index = pivot(left,right)
            quick_sort_recusive(left,pivot_index-1)
            quick_sort_recusive(pivot_index+1, right)
    def pivot(left, right):
        pivot = arr[right]
        i = left-1
        for j in range(left, right):
            pygame.event.pump()
            if arr[j] < pivot:
                i +=1
                arr[i], arr[j] = arr[j], arr[i]
                draw(arr)
                time.sleep(delay/1000)
        arr[i+1], arr[right] = arr[right], arr[i+1]
        draw(arr)
        time.sleep(delay/1000)
        return i +1
    quick_sort_recusive(0, len(arr)-1)





       

