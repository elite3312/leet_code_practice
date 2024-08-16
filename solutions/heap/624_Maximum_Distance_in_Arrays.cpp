#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cstring>
#include <math.h>
#include <map>
#include <bitset>
using namespace std;
/**copy from here**/
class Solution
{
public:
    int maxDistance(vector<vector<int>>& arrays) {
        // Min-Heap for smallest elements
        priority_queue<pair<int, int>> minHeap;
        // Max-Heap for largest elements
        priority_queue<pair<int, int>> maxHeap;

        // Fill the heaps with elements from the arrays
        for (int i = 0; i < arrays.size(); ++i) {
            minHeap.push({-arrays[i][0], i});
            maxHeap.push({arrays[i].back(), i});
        }

        // Get the smallest and largest elements
        auto [minVal, minIdx] = minHeap.top(); minHeap.pop();
        auto [maxVal, maxIdx] = maxHeap.top(); maxHeap.pop();
        int diff = maxVal - -minVal;

        // If the smallest and largest elements come from the same array
        if (minIdx == maxIdx) {
            int altDiff1 = maxHeap.top().first - -minVal;
            int altDiff2 = maxVal - -minHeap.top().first;
            diff = max(altDiff1, altDiff2);
        }

        return diff;
    }
    /*we should use the priority queue instead of make_heap*/
    int maxDistance_0(vector<vector<int>> &arrays)
    {
        vector<pair<int, int>> min_heap, max_heap;
        int m = arrays.size();

        for (int i = 0; i < m; i++)
        {
            int n = arrays[i].size();

            // push to min heap
            min_heap.push_back(
                make_pair(-arrays[i][0], i));
            push_heap(min_heap.begin(), min_heap.end());

            // push to max heap
            max_heap.push_back(
                make_pair(arrays[i][n - 1], i));
            push_heap(max_heap.begin(), max_heap.end());
        }
        int min_top = -min_heap[0].first;
        int min_top_index = min_heap[0].second;

        int max_top = max_heap[0].first;
        int max_top_index = max_heap[0].second;

        if (max_top_index != min_top_index)
            return max_top - min_top;
        else
        {
            pop_heap(min_heap.begin(), min_heap.end());
            min_heap.pop_back();
            
            pop_heap(max_heap.begin(), max_heap.end());
            max_heap.pop_back();
            // move second largest elem to the back
            
            pop_heap(min_heap.begin(), min_heap.end());
            int min_top_next = -min_heap[min_heap.size() - 1].first;

            pop_heap(max_heap.begin() , max_heap.end());
            int max_top_next = max_heap[max_heap.size() - 1].first;
            return max(max_top - min_top_next,max_top_next - min_top);
        }
    }
};
/*
case 0
1 1 4(values of min heap)
0 2 1(belonging to which arr)

5 3 3
1 0 2
->5-1=4

case 1
1 2
0 1

6 3
0 1
->6-2=4
*/
/**copy to here**/
int main()
{
    Solution *s = new Solution();
    vector<vector<int>> f = {{-1,1},{-3,1,4},{-2,-1,0,2}}; // 6
    cout << s->maxDistance(f);
    vector<vector<int>> b = {{1, 2, 3}, {4, 5}, {1, 2, 3}}; // 4
    cout << s->maxDistance(b);

    vector<vector<int>> c = {{1}, {1}}; // 0
    cout << s->maxDistance(c);

    vector<vector<int>> d = {{1, 6}, {2, 3}}; // 4
    cout << s->maxDistance(d);

    vector<vector<int>> e = {{1, 5}, {3, 4}}; // 3
    cout << s->maxDistance(e);

    return 0;
}
