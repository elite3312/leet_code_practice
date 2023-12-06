# 演算法筆記

## todo

- 695. Max Area of Island
- lca

## union_find

```cpp
vector<int> father;
int ans;
int find(int u){
    if(father[u] == u)return u;
    return father[u] = find(father[u]);
}
void merge(int u, int v){
    u = find(u), v = find(v);
    if(u!=v){
        father[u] = v;
        ans -- ;
    }
}
```
