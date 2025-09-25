#include <sublib1/sublib1.h>
#include "sublib2/sublib2.h"

int main(int argc, char *argv[])
{
    sublib1 hi;
    hi.print();

    sublib1 hi2;
    hi2.print();
 
    sublib2 howdy;
    howdy.print();
    
    return 0;
}
