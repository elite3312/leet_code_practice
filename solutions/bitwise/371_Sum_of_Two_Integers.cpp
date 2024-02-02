#include "utils/linked_list.hpp"
#include "utils/binary_tree.hpp"
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cstring>
#include <math.h>
#include <map>
using namespace binary_tree;
using namespace std;
/**copy from here**/
//sum a, b without + - operators
//-1000 <= a, b <= 1000
class Solution {
public:
	void fill_bin(int x, int bin[32]){
		if (x<0)
			x=-x;
		int i=0;
		while(i<32){
			bin[i++]=x%2;
			x>>=1;
		}
	}
	void add_bin(int bin_a[32],int bin_b[32],int sum_bin[32]){
		int i=0,carry=0;
		while(i<32){
			if (bin_a[i]^bin_b[i]){
				if(carry)sum_bin[i]=0;
				else sum_bin[i]=1;
			}
			else{
				if (bin_a[i]){// 1 1 
					if (carry)sum_bin[i]=1;
					else {
						sum_bin[i]=0;
						carry=1;
					}
				}
				else{// 00
					if (carry){
						sum_bin[i]=1;
						carry=0;
					}
					else sum_bin[i]=0;
				}
			}
			i++;
		}
	}
	void subtract_bin(int bin_a[32],int bin_b[32],int sum_bin[32]){
		//a>b here
		int i=0,borrow=0;
		while(i<32){
			if(borrow){
				if (bin_a[i]){
					bin_a[i]=0;
					borrow=0;
				}
				else{
					bin_a[i]=1;
				}
			}
			if(bin_a[i]==0&&bin_b[i]==0)
				sum_bin[i]=0;
			
			else if(bin_a[i]==0&&bin_b[i]==1){
				sum_bin[i]=1;
				borrow=1;
			}
			else if(bin_a[i]==1&&bin_b[i]==0)
				sum_bin[i]=1;
			
			else if(bin_a[i]==1&&bin_b[i]==1)
				sum_bin[i]=0;
			i++;
		}
	}  
	int bin_2_int(int bin[32]){
		int res=0,offset=31;
		while (offset>=0){
			res|=bin[offset]<<offset;
			offset-=1;
		}
		
		return res;
	}
	int getSum_(int a, int b) {
		if (a==0)return b;
		if (b==0)return a;
		int abs_a_bin[32]={0};
		int abs_b_bin[32]={0};
		int abs_sum_bin[32]={0};
		int res;
		fill_bin(a,abs_a_bin);
		fill_bin(b,abs_b_bin);
        if (a<0 && b <0 ||a>0 && b >0 ){
			add_bin(abs_a_bin,abs_b_bin,abs_sum_bin);
			if (a<0)
				res=-bin_2_int(abs_sum_bin);
			else res=bin_2_int(abs_sum_bin);
		}
		else if (a<0 && b >=0 ||a>=0 && b <0){
			if(a<0){
				if(abs(a)>abs(b)){
					subtract_bin(abs_a_bin,abs_b_bin,abs_sum_bin);
					res=-bin_2_int(abs_sum_bin);
				}
				else{
					subtract_bin(abs_b_bin,abs_a_bin,abs_sum_bin);
					res=bin_2_int(abs_sum_bin);
				}
			}
			else{
				if(abs(b)>abs(a)){
					subtract_bin(abs_b_bin,abs_a_bin,abs_sum_bin);
					res=-bin_2_int(abs_sum_bin);
				}
				else{
					subtract_bin(abs_a_bin,abs_b_bin,abs_sum_bin);
					res=bin_2_int(abs_sum_bin);
				}
			}
		}
		return res;
    };
	int getSum(int a, int b) {
    return b==0? a:getSum(a^b, (a&b)<<1); //be careful about the terminating condition;
}
};
/**copy to here**/
int main()
{
	Solution *s = new Solution();
	int a,b,res;
	a=20;
	b=30;
	res=s->getSum(a,b);
	cout<<res<<endl;//50

	a=1;
	b=2;
	res=s->getSum(a,b);
	cout<<res<<endl;//3

	a=-1;
	b=-2;

	res=s->getSum(a,b);
	cout<<res<<endl;//-3

	a=-1;
	b=2;

	res=s->getSum(a,b);
	cout<<res<<endl;//1

	a=1;
	b=-2;

	res=s->getSum(a,b);
	cout<<res<<endl;//-1

	a=0;
	b=-1;

	res=s->getSum(a,b);
	cout<<res<<endl;//-1

	a=0;
	b=17;

	res=s->getSum(a,b);
	cout<<res<<endl;//17
	

	
	return 0;
}

