# c++ notes

## Notes

- when using unordered map, if you expect to insert or delete new entries, do not do it within a "for (auto e:m)", it will mess up the auto iterator and lead to hard to detect bugs.

## STL

### vector

```cpp
//vector
vector<int> a ;
vector<vector<int>>a(n, vector<int>(m, 0));//n * m vector
vector<Node*>//vector of pointers
a.resize(n, vector<int>(m, 0))//n * m vector
```

### map

```cpp
//map(0(n) access, using red black tree)
map<int, int> m[n] = 1;
```

### set

```cpp
//set(0(n) access, using red black tree)
set<int> s
s.insert()
s.find()!=s.end()
s.count()
```

### queue

```cpp
queue<int> q
q.push()
q.front() 
q.pop()
```

### stack

```cpp
//stack
stack<int>s
s.push()
s.pop()
```

### haspmap(o(1) access)

```cpp
unordered_map<int,int> m
```

### set (o(1) access)

```cpp
unordered_set<int> s
```

### priority_queue

```cpp
priority_queue<int> q
```

### pair

```cpp
pair<int, string> pair1(100, "Tom");
```

### 2d array

```cpp
int arr[10][20] = {0};  // easier way
// this does the same
memset(arr, 0, sizeof arr); 
```

### sort with custom compare

```cpp
bool myComparison(const pair<int,int> &a,const pair<int,int> &b)
{
       return a.first<b.first;
}
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int> >& intervals) {
        vector<pair<int,int>>v;
        for (auto e:intervals){
            v.push_back({e[0],e[1]});}
        sort(v.begin(),v.end(),myComparison);
        return 0;
    }
};
```
