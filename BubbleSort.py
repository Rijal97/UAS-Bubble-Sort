def Bubble_sort(rijal): #Ini adalah definisi fungsi Bubble_sort, yang menerima satu parameter rijal, yaitu daftar (list) yang akan diurutkan.
    n = len(rijal) #Baris ini menghitung panjang dari daftar rijal dan menyimpannya dalam variabel n.
    for i in range(n): #Ini adalah loop pertama yang berulang sebanyak n kali, di mana i adalah variabel yang akan berubah dari 0 hingga n-1. Loop ini digunakan untuk setiap iterasi pengurutan.
        for j in range(n-i-1): #Loop kedua yang berulang dari 0 hingga n-i-1. Ini memastikan bahwa setiap elemen yang tersisa diperiksa dan diurutkan di setiap iterasi.
            if rijal[j] > rijal[j+1]: #Baris ini membandingkan dua elemen yang berdekatan dalam daftar. Jika elemen di posisi j lebih besar daripada elemen di posisi j+1, maka mereka akan ditukar.
                rijal[j], rijal[j+1] = rijal[j+1], rijal[j] #Ini adalah proses pertukaran elemen. Jika kondisi if di atas terpenuhi, maka elemen rijal[j] dan rijal[j+1] akan ditukar tempat.
    return rijal #Setelah semua iterasi selesai dan daftar sudah diurutkan, fungsi mengembalikan daftar rijal yang sudah diurutkan.

data_list = [57, 23, 76, 45, 89, 12, 68, 34, 90, 21, 84, 27, 61, 39, 95, 44, 73, 17, 52, 30, 11, 82, 25, 64, 49, 37, 96, 20, 88, 56, 13, 77, 92, 43, 65, 19, 54, 38, 85, 72, 9, 47, 78, 31, 63, 24, 99, 50, 66, 70] #Ini adalah daftar data_list yang berisi 50 angka acak yang akan diurutkan.
print(f"data sebelum diurutkan", data_list) #Baris ini mencetak daftar angka sebelum diurutkan.
sorting_data = Bubble_sort(data_list) #Memanggil fungsi Bubble_sort dengan data_list sebagai argumen dan menyimpan hasil yang sudah diurutkan dalam sorting_data.
print(f"data sesudah diurutkan", sorting_data) #Baris ini mencetak daftar angka setelah diurutkan.
