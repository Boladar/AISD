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
using namespace std;

void GenerujTablice(int tab[],int n)
{
    int wylosowana;
    bool jest=false;
    for (int i=0;i<n;i++)
    {
        while(true)
        {
            wylosowana=rand()%n+1;
            jest=false;
            for (int j=0;j<i;j++)
            {
                if(tab[j]==wylosowana)
                {
                    jest=true;
                    break;
                }
            }
            if(jest==false)
            {
                tab[i]=wylosowana;
                break;
            }
        }
    }
}

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

struct Node * minValueNode(struct Node* node)
{
    struct Node* current = node;
    while (current->left != NULL)
        current = current->left;
    return current;
}

Node *rightRotate(Node *y)
{
    Node *x = y->left;
    Node *T2 = x->right;
    
    x->right = y;
    y->left = T2;
    
    y->height = std::max(height(y->left),
                         height(y->right)) + 1;
    x->height = std::max(height(x->left),
                         height(x->right)) + 1;
    return x;
}

Node *leftRotate(Node *x)
{
    Node *y = x->right;
    Node *T2 = y->left;
    
    y->left = x;
    x->right = T2;
    
    x->height = max(height(x->left),
                    height(x->right)) + 1;
    y->height = max(height(y->left),
                    height(y->right)) + 1;
    return y;
}

Node* insert(Node* node, int key)
{
    if (node == NULL)
        return(newNode(key));
    
    if (key < node->key)
        node->left = insert(node->left, key);
    else if (key > node->key)
        node->right = insert(node->right, key);
    else
        return node;
    node->height = 1 + max(height(node->left),
                           height(node->right));
    int balance = Balance(node);
    if (balance > 1 && key < node->left->key)
        return rightRotate(node);
    if (balance < -1 && key > node->right->key)
        return leftRotate(node);
    if (balance > 1 && key > node->left->key)
    {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }
    if (balance < -1 && key < node->right->key)
    {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }
    return node;
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

struct Node* deleteNode(struct Node* root, int key)
{
    if (root == NULL)
        return root;
    if ( key < root->key )
        root->left = deleteNode(root->left, key);
    else if( key > root->key )
        root->right = deleteNode(root->right, key);
    else
    {
        if( (root->left == NULL) || (root->right == NULL) )
        {
            struct Node *temp = root->left ? root->left :
            root->right;
            
            if (temp == NULL)
            {
                temp = root;
                root = NULL;
            }
            else
                *root = *temp;
            delete temp;
        }
        else
        {
            struct Node* temp = minValueNode(root->right);
            root->key = temp->key;
            root->right = deleteNode(root->right, temp->key);
        }
    }
    if (root == NULL)
        return root;
    root->height = 1 + std::max(height(root->left),
                           height(root->right));
    int balance = Balance(root);
    if (balance > 1 && Balance(root->left) >= 0)
        return rightRotate(root);
    if (balance > 1 && Balance(root->left) < 0)
    {
        root->left =  leftRotate(root->left);
        return rightRotate(root);
    }
    if (balance < -1 && Balance(root->right) <= 0)
        return leftRotate(root);
    if (balance < -1 && Balance(root->right) > 0)
    {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }
    
    return root;
}
void DeleteTree (Node * &p )
{
    if (p==NULL)
        return;
    DeleteTree(p->left);
    DeleteTree(p->right);
    delete p;
}

bool PathToNode(Node * n,int value,vector<int>&path)
{
    if(n==NULL)
        return false;
    else
    {
        while(true)
        {
            if(value < n->key)
            {
                path.push_back(n->key);
                if(n->left)
                    n = n->left;
                else
                    return false;
            }
            else if(value > n->key)
            {
                path.push_back(n->key);
                if(n->right)
                    n = n->right;
                else
                    return false;
            }
            else
            {
                path.push_back(n->key);
                return true;
            }
        }
    }
}

int main()
{
    Node *root = NULL;
    for (int n=10000;n<100000;n+=10000)
    {
        int * arr= new int [n] ;
        GenerujTablice(arr,n);
        //czas
        for (int i=0;i<n;i++)
            root = insert(root, arr[i]);
        //czas
        delete[] arr;
        PreOrder(root);
        cout << "\n";
        InOrder(root);
        cout << "\n";
        vector<int> path;
        //czas
        for(int j=0;j<10;j++)
            {
                bool ok=PathToNode(root,rand()%n+1,path);
                if (ok==true)
                {
                    for(int i=0;i<path.size()-1;i++)
                    {
                        cout << path[i] << "->";
                        
                    }
                    cout << path[path.size()-1] << "\n";
                }
            }
        //czas
        //czas
        DeleteTree(root);
        //czas
        root = NULL;
    }
    return 0;
}

