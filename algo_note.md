# 演算法筆記

## todo

## union_find

```cpp
vector<int> father;//initially every point is its own father
int find(int u){
    if(father[u] == u)return u;
    return father[u] = find(father[u]);
}
void merge(int u, int v){
    u = find(u), v = find(v);
    if(u!=v){
        father[u] = v;
    }
}
```

## binary_search

```cpp
int binarySearch(int arr[], int l, int r, int x)
{
    while (l <= r) {
        int m = l + (r - l) / 2;
 
        // Check if x is present at mid
        if (arr[m] == x)
            return m;
 
        // If x greater, ignore left half
        if (arr[m] < x)
            l = m + 1;
 
        // If x is smaller, ignore right half
        else
            r = m - 1;
    }
 
    // If we reach here, then element was not present
    return -1;
}
```
