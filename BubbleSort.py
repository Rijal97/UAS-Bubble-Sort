def Bubble_sort(rijal):
    n = len(rijal)
    for i in range(n):
        for j in range(n-i-1):
            if rijal[j] > rijal[j+1]:
                rijal[j], rijal[j+1] = rijal[j+1], rijal[j]
    return rijal

data = [57, 23, 76, 45, 89, 12, 68, 34, 90, 21, 84, 27, 61, 39, 95, 44, 73, 17, 52, 30, 11, 82, 25, 64, 49, 37, 96, 20, 88, 56, 13, 77, 92, 43, 65, 19, 54, 38, 85, 72, 9, 47, 78, 31, 63, 24, 99, 50, 66, 70]
print(f"data sebelum diurutkan", data)
sorting_data = Bubble_sort(data)
print(f"data sesudah diurutkan", sorting_data)
