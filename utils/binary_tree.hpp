#ifndef BINARY_TREE_HPP
#define BINARY_TREE_HPP
#include<stdio.h>
namespace binary_tree
{

    // Definition for a binary tree node.
    struct TreeNode
    {
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode(int x) : val(x), left(NULL), right(NULL) {}
    };

}
#endif // BINARY_TREE_HPP