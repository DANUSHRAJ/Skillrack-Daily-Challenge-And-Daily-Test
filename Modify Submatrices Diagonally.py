Modify Submatrices Diagonally
The program must accept an integer matrix of size R*C and an integer K as the input. 
The values of R and C are always divisible by K. The given R*C matrix contains only 0s and 1s. 
The program must form an alphabet matrix of size (R/K)*(C/K) starting from "a" being present in the bottom left corner.
Then the program must modify the submatrices of size K*K diagonally. In each integer submatrix of size K*K, all 1s must be replaced with the related 
upper case alphabet in the alphabet matrix and all 0s must be replaced with the related lower case alphabet in the alphabet matrix.
If "z" has reached while filling the alphabet matrix then "a" must be considered as the next alphabet in circular fashion while forming the alphabet matrix.
Finally, the program must print the integer matrix replaced with the corresponding alphabets as the output.

Boundary Condition(s):
2 <= R, C <= 50

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integer values separated by a space.
The (R+2)nd line contains K.

Output Format:
The first R lines, each contains C alphabets separated by a space.

Example Input/Output 1:
Input:
9 9
0 0 1 0 0 0 0 1 1
0 0 1 1 1 1 1 0 1
0 1 1 1 1 1 0 1 1
1 1 1 1 1 0 1 1 1
0 1 1 0 0 0 1 1 0
0 0 0 1 0 1 1 0 0
0 0 1 1 0 1 1 1 1
0 1 1 0 1 1 1 0 0
0 0 1 1 1 1 0 1 1
3

Output:
d d D g g g i I I
d d D G G G I i I
d D D G G G i I I
B B B E E e H H H
b B B e e e H H h
b b b E e E H h h
a a A C c C F F F
a A A c C C F f f
a a A C C C f F F

Explanation:
Here R = 9, C = 9 and K = 3.
So the size of the alphabet matrix to be formed is (9/3)*(9/3).
The alphabet matrix of size 3*3 is given below.
d g i
b e h
a c f
In the above alphabet matrix, the alphabets starting from 'a' are filled diagonally in the top-left to bottom-right diagonals starting the bottom-left corner.
After replacing the submatrices with their corresponding alphabets based on the given conditions, the matrix becomes
d d D g g g i I I
d d D G G G I i I
d D D G G G i I I
B B B E E e H H H
b B B e e e H H h
b b b E e E H h h
a a A C c C F F F
a A A c C C F f f
a a A C C C f F F

Example Input/Output 2:
Input:
6 8
1 0 1 0 0 1 0 0
0 1 1 1 1 1 0 1
0 0 0 0 1 0 1 0
1 1 1 0 0 0 1 1
1 0 1 1 1 0 0 0
1 1 1 0 0 1 1 0
2

Output:
D d G g j J l l
d D G G J J l L
b b e e H h K k
B B E e h h K K
A a C C F f i i
A A C c f F I i

Explanation:
Here R = 6, C = 8 and K = 2.
So the size of the alphabet matrix to be formed is (6/2)*(8/2).
The alphabet matrix of size 3*4 is given below.
d g j l
b e h k
a c f i
In the above alphabet matrix, the alphabets starting from 'a' are filled diagonally in the top-left to bottom-right diagonals starting the bottom-left corner.
After replacing the submatrices with their corresponding alphabets based on the given conditions, the matrix becomes
D d G g j J l l
d D G G J J l L
b b e e H h K k
B B E e h h K K
A a C C F f i i
A A C c f F I i

Example Input/Output 3:
Input:
10 12
0 1 0 1 0 1 0 1 1 0 0 1
0 0 0 1 0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 1 0 0 0 0
0 0 0 0 0 0 0 1 1 0 1 0
1 1 0 1 0 1 0 0 1 0 1 0
1 0 1 0 1 1 0 0 0 1 0 1
0 1 0 0 1 0 0 0 1 1 1 0
1 1 0 1 0 0 1 0 0 0 0 0
0 1 1 0 0 1 0 1 1 0 0 0
1 0 0 1 0 0 0 0 1 0 1 0
2

Output:
k K p P u U y Y B b d D
k k p P u u y y B B d d
g g l l Q Q v V z z c c
g g l l q q v V Z z C c
D D h H m M r r W w A a
D d H h M M r r w W a A
b B e e I i n n S S X x
B B e E i i N n s s x x
a A C c f F j J O o t t
A a c C f f j j O o T t

SOLUTION:
def fun(op,l,sr,sc,er,ec,ch):
    for k in range(sr,er+1):
        for h in range(sc,ec+1):
            if l[k][h]=='1':op[k][h]=chr(ch).upper()
            else:op[k][h]=chr(ch).lower()
            
x,y=map(int,input().split());l=[input().split() for k in range(x)]
op=[['0' for h in range(y)] for k in range(x)]
a=int(input());l1=[];sr=x-a;sc=0;ch=96
while(sr>=0):
    sc=0;r=sr;c=sc
    while(1):
        if r>=x or c>=y:break
        fun(op,l,r,c,r+a-1,c+a-1,ch+1);ch+=1
        if ch==122:ch=96
        r+=a;c+=a
    sr-=a
sr,sc=0,a
while(sc<=y-1):
    sr=0
    r=sr;c=sc
    while(1):
        if r>=x or c>=y:break
        fun(op,l,r,c,r+a-1,c+a-1,ch+1);ch+=1
        if ch==122:ch=96
        r+=a;c+=a
    sc+=a

for k in op:print(*k)