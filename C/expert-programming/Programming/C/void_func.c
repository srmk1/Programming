// Program 1 (Compiles and runs fine in C, but not in C++)
void fun() {  }
int main(void)
{
    fun(10, "GfG", "GQ");
    return 0;
}


/* COMPILES SUCCESSFULLY
SRMK-M-H00U:linux srmk$ gcc void_func.c -o void_func
void_func.c:5:24: warning: too many arguments in call to 'fun'
    fun(10, "GfG", "GQ");
    ~~~                ^
1 warning generated.
*/
