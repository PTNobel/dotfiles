
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int usage(char *argv[] ) 
{
    printf(argv[0]);
    printf(" {toggle|next|back|stop}\n");
    return 0;
}

int main( int argc, char *argv[] )
{
    if ( argc != 2 ) {
        usage(argv);
        return 1;
    }

    else if( strcmp(argv[1],"toggle") == 0 )
    {
      setuid(1000);
      system( "/bin/bash -i -c '/usr/bin/env HOME=/home/parth PATH=/usr/bin/ python3 /usr/local/bin/musicctl.py pause'" );
      return 0;
    }

    else if(strcmp(argv[1],"next") == 0 )
    {
      setuid(1000);
      system( "/bin/bash -i -c '/usr/bin/env HOME=/home/parth PATH=/usr/bin/ python3 /usr/local/bin/musicctl.py next'" );
      return 0;
    }

    else if(strcmp(argv[1],"back") == 0 )
    {
      setuid(1000);
      system( "/bin/bash -i -c '/usr/bin/env HOME=/home/parth PATH=/usr/bin/ python3 /usr/local/bin/musicctl.py back'" );
      return 0;
    }

    else if( strcmp(argv[1],"stop") == 0 )
    {
      setuid(1000);
      system( "/bin/bash -i -c '/usr/bin/env HOME=/home/parth PATH=/usr/bin/ python3 /usr/local/bin/musicctl.py stop'" );
      return 0;
    }

    else if(strcmp(argv[1],"-h") == 0 )
    {
      usage(argv);
      return 0;
    }

    else
    {
      usage(argv);
      return 1;
    }
}
