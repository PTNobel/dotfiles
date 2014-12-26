#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main( int argc, char *argv[] )
{
    if ( argc != 2 ) {
      printf("Needs one argument\n");
      return 1;
    }
    else if( strcmp(argv[1],"mlocate") == 0 )
    {
      setuid( 0 );   // you can set it at run time also
	  system( "/usr/bin/updatedb" );
      return 0;
    }
    else if( strcmp(argv[1],"pkgfile") == 0 )
    {
      setuid( 0 );
      system( "/usr/bin/pkgfile -u" );
      return 0;
    }
    else if(strcmp(argv[1],"man") == 0 )
    {
      setuid( 0 );
      system( "/usr/bin/mandb" );
      return 0;
    }
  
}
