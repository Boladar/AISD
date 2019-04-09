//
//  GeneratorTablic.cpp
//  Drzewa
//
//  Created by Kacper Trzeciak on 06/04/2019.
//  Copyright © 2019 Kacper Trzeciak. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <ctime>
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
