#include <iostream>
#include <windows.h>
#include <Shellapi.h>

using namespace std;

/* emptying the trash */
void clear_trash(void) { // silent trash emptying
    SHEmptyRecycleBin(NULL, NULL, SHERB_NOCONFIRMATION + SHERB_NOPROGRESSUI + SHERB_NOSOUND);
}