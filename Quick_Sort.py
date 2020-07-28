
#QuickSort


def change(x , i, j):
    x[i], x[j] = x[j], x[i]

def Select(x, l, r):
    select_val = x[l]
    select_idx = l
    while l <= r:
        while l <= r and x[l] <= select_val:#괜찮을땐 패스
            l += 1
        while l <= r and x[r] >= select_val:#왼쪽부터 체크해서 
            r -= 1                          #걸리면 오른쪽에서 찾기
        if l <= r:#
            change(x, l, r)
            l += 1
            r -= 1
    change(x, select_idx, r)
    return r

def quickSort(x, pivotMethod = Select):
    def Qsort(x, first, last):
        if first<last:
            splitP = pivotMethod(x, first, last)
            Qsort(x, first, splitP - 1)
            Qsort(x, splitP + 1, last)
    Qsort(x, 0, len(x)-1)

x = [5,2,8,6,1,9,3,7]
quickSort(x)
print(x)
help(pivotMethod())


#Quick_Sort Simple
arr = [7,3,1,6,5,2,4]
print(quick_sort(arr))

def Quick_sort(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = a[-1]
    g_left = []
    g_right=[]
    for i in range(0,n-1):
        if a[i] <= pivot:
            g_left.append(a[i])
        else:
            g_right.append(a[i])
    return Quick_sort(g_left) + [pivot] + Quick_sort(g_right)

d = [8,12,1,9,102,25,32,98,31]
print(Quick_sort(d))



'''JAVA   ###< Ctrl + /'''

# package JAVA;

# import java.util.ArrayList;
# import java.util.Arrays;
# import java.util.List;


# public class Quick{
#     public static void main(String[] args){

#         Integer[] array = {30, 50, 7, 40, 88, 15, 44, 55, 22,
#         33, 77, 88, 11, 66, 1, 85};
#         ArrayList<Integer> aList = new ArrayList<Integer>();
#         aList.addAll(Arrays.asList(array));

#         aList = (ArrayList<Integer>) quicksort(aList);
#         out.print(aList.toString());
#     }

    
#     public static <T extends Comparable<? super T>> List<T> 
#     quicksort(List<T> list) {

#         if (list.size() <=1) return list;
#         int pivot =list.size() / 2;
#         List<T> a = new ArrayList<T>();
#         List<T> b = new ArrayList<T>();
#         int c = 0;
#         for (T number : list){
#             if (list.get(pivot).compareTo(number) < 0)
#             b.add(number);
#             else if (list.get(pivot).compareTo(number) > 0)
#                 a.add(number);
#             else
#                 c++;
#         }
#         a = quicksort(a);
#         for (int i = 0; i < c; i ++)
#             a.add(list.get(pivot));

#             b = quicksort(b);

#             List<T> sorted = new ArrayList<T>();
#             sorted.addAll(a);
#             sorted.addAll(b);
#             return sorted;        
    
#     }

# }