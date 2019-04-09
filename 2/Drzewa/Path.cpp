#include <iostream>
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
