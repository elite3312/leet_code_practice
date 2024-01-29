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
