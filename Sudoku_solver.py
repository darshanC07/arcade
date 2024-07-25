#include <stdio.h>

// void convert(int sudoku[9][9]){
//     //for converting all dots to numbers
//     for(int i=0;i<9;i++){
//         for(int j=0;j<9;j++){
//             if(sudoku[i][j]==0){
//                 sudoku[i][j]=1;
//             }
//         }
//     }
// }

void print(int sudoku[9][9]){
    //for printing sudoku
    for(int m=0;m<9;m++){
        for(int n=0;n<9;n++){
            printf("%d \t",sudoku[m][n]);
        }
        printf("\n");
    }
}

void remove_arr(int sudoku[9][9],int t,int arr[9][9]){
    
    for(int m=0;m<9;m++){
        for(int n=0;n<9;n++){
            if(sudoku[t][m]==arr[t][n]){
                arr[t][n]=0;
            }
            else{
                continue;
            }
        }
        
    }

}

void col(int sudoku[9][9],int t,int arr[9][9]){
    for(int i=0;i<9;i++){
        if(sudoku[t][i]==0){
            for(int j=0;j<9;j++){
                if(arr[t][j]==0){
                    continue;
                }
                else{
                    sudoku[t][i]=arr[t][j];
                    arr[t][j]=0;
                    break;
                }
            }
        }
        else{
            continue;
        }

    }

}

//by default ,min value will always be 1......something is wrong
int check_horizontally(int sudoku[9][9]){
    int count=0;
    for(int i=0;i<9;i++){
        for(int j=0, m=0;j<9,m<9;j++,m++){
            if(sudoku[0][i]==sudoku[0][j] || sudoku[0][i]==sudoku[m][0]){
                count++;
                break;
            }
        }
    }
    return count;
}

int main(){
    
    int sudoku[9][9] = {{5,3,0,0,7,0,0,0,0},
    {6,0,0,1,9,5,0,0,0},
    {0,9,8,0,0,0,0,6,0},
    {8,0,0,0,6,0,0,0,3},
    {4,0,0,8,0,3,0,0,1},
    {7,0,0,0,2,0,0,0,6},
    {0,6,0,0,0,0,2,8,0},
    {0,0,0,4,1,9,0,0,5},
    {0,0,0,0,8,0,0,7,9}};

    int arr[9][9];
    for(int i=0;i<9;i++){
        for(int a=0,x=1;a<9,x<=9;a++,x++){
            arr[i][a]=x;
        }
        
    }
    printf("Original Sudoku\n");
    print(sudoku);
    printf("\n");
    
    //below loop for getting array of elements not present in sudoku

    for(int t=0;t<9;t++){
        remove_arr(sudoku,t,arr);
    }
    printf("arr\n");
    print(arr);
    printf("\n");

    //below loop for inserting elements from arr to sudoku
    for(int t=0;t<9;t++){
        col(sudoku,t,arr);
    }
    printf("updated sudoku\n");
    print(sudoku);
    printf("\n");
    
    printf("%d",check_horizontally(sudoku)-1);
}
