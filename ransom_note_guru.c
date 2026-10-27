// checking if ransomnote has made of the letters magazine
# include<stdio.h>
# include<string.h>
int main(){
    int count;
    char ransomnote[10];
    char magazine[10];
    printf("enter the letters for ransomnote: ");
    scanf("%s",ransomnote);
    printf("enter the letters for magazine: ");
    scanf("%s",magazine);
    count = 0;
    for(int i = 0, i < 10, i=i+1){
        ransomnote[i];
        if (i in magazine){
            count = count+1;
        }
    if (count == strlen(ransomnote[10])){
        printf("true");
    }    
    else{
        printf("false");
    }
    }   

    return 0;

}