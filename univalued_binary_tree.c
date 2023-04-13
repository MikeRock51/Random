/**
* QWASAR.IO -- univalued_binary_tree
*
* @param {treenode*} param_1
*
* @return {bool}
*
*/
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#ifndef STRUCT_TREENODE
#define STRUCT_TREENODE

typedef struct s_treenode
{
    int val;
    struct s_treenode* left;
    struct s_treenode* right;
} treenode;

#endif

bool univalued_binary_tree(treenode *node)
{
    int value;
    
    if (!node)
        return true;

    if (node->left && node->left->val != node->val)
        return false;
    if (node->right && node->right->val != node->val)
        return false;

    // printf("Here\n");
    return (univalued_binary_tree(node->left) && univalued_binary_tree(node->right));
}

int main()
{
    treenode *tri = malloc(sizeof(treenode));
    tri->val = 2;
    // tri->left = NULL;
    // tri->left = NULL;

    
    printf("%d\n", univalued_binary_tree(tri));
}
