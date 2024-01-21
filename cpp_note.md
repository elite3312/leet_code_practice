# c++ notes

## STL

```cpp
//vector
vector<int> a ;
vector<vector<int>>a(n, vector<int>(m, 0));//n * m vector
vector<Node*>//vector of pointers
a.resize(n, vector<int>(m, 0))//n * m vector

//map(0(n) access, using red black tree)
map<int, int> m[n] = 1;

//set(0(n) access, using red black tree)
set<int> s
s.insert()
s.find()!=s.end()
s.count()

//queue
queue<int> q
q.push()
q.front() 
q.pop()

//stack
stack<int>s
s.push()
s.pop()

//haspmap(o(1) access)
unordered_map<int,int> m

//set (o(1) access)
unordered_set<int> s

//priority_queue
priority_queue<int> q

//pair
pair<int, string> pair1(100, "Tom");
```
