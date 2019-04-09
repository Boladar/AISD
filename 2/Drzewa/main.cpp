//
//  main.cpp
//  Drzewa
//
//  Created by Kacper Trzeciak on 06/04/2019.
//  Copyright © 2019 Kacper Trzeciak. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include "GeneratorTablic.cpp"
#include "Rotate.cpp"
#include "Insert.cpp"
#include "Path.cpp"

using namespace std;
struct Node
{
    int key;
    Node *left;
    Node *right;
    int height;
};

int height(Node *N)
{
    if (N == NULL)
        return 0;
    return N->height;
}

Node* newNode(int key)
{
    Node* node = new Node();
    node->key = key;
    node->left = NULL;
    node->right = NULL;
    node->height = 1;
    return(node);
}


int Balance(Node *N)
{
    if (N == NULL)
        return 0;
    return height(N->left) - height(N->right);
}


void PreOrder(Node *n)
{
    if(n==NULL)
        return;
    cout << n->key << " ";
    PreOrder(n->left);
    PreOrder(n->right);
    
}

void InOrder(Node * n)
{
    if(n==NULL)
        return;
    InOrder(n->left);
    cout << n->key << " ";
    InOrder(n->right);
}

void DeleteTree (Node * &p )
{
    if (p==NULL)
        return;
    DeleteTree(p->left);
    DeleteTree(p->right);
    delete p;
}

int main()
{
    Node *root = NULL;
    for (int n=10000;n<100000;n+=10000)
    {
        int * arr= new int [n] ;
        GenerujTablice(arr,n);
        for (int i=0;i<n;i++)
            root = insert(root, arr[i]);
        delete[] arr;
        PreOrder(root);
        cout << "\n";
        InOrder(root);
        cout << "\n";
        vector<int> path;
        bool ok=PathToNode(root,50,path);
        if (ok==true)
        {
            for(int i=0;i<path.size()-1;i++)
            {
                cout << path[i] << "->";
            }
            cout << path[path.size()-1] << "\n";
        }
        DeleteTree(root);
        root = NULL;
    }
    return 0;
}

