

def bubbleSort(data,search):
    arr = data['license_data']
    size = len(arr)
    for i in range(size):
        swapped = False
        for j in range(0, size - i - 1):
            # Membandingkan spesifik json data
            if arr[j][search] > arr[j + 1][search]:
                # Swap jika elemen yang ditemukan lebih besar daripada pointer selanjutnya
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Jika keduanya tidak lebih besar atau kecil, list sudah di swap
        if not swapped:
            break
    return data

def selectionSort(data, search):
    arr = data['license_data']
    n = len(arr)
    print(n)
    
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j]['name'] < arr[min_index]['name']:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    sorting_name = [entry['name'] for entry in arr]

    return sorting_name

def quick_sort(data,search):
    arr = data['license_data']
    size = len(arr)
    indexAwal = 0
    indexAkhir = size - 1
    i = indexAwal
    j = indexAkhir
    pivot = arr[indexAwal]
    
    while (i < j):
        while (arr[i]['expires_at'] < pivot):
            i+=indexAwal
        while (arr[j]['expires_at'] > pivot):
            print(arr[j]['expires_at'])
            j-=indexAkhir
    if (i <= j):
        arr[i],arr[j] = arr[j], arr[i]
        
    if (indexAwal < j):
        quick_sort(arr, j - 1)

    if (i < indexAkhir):
        quick_sort(arr, i)

def insertion_sort(data,search):  
        arr = data['license_data']
        size = len(arr)
        for i in range(1, size):  
            a = arr[i]  
  
            j = i - 1  
          
            while j >= 0 and a <arr[j]:  
                arr[j + 1] = arr[j]  
                j -= 1  
                
            arr[j + 1] = a  
            
        return arr
# Merge Manual
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
# Sorting Merge
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)
