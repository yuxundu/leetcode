class Solution {
    public int reverse(int x) {
        int res = 0;
        int k = (x>=0)?1:-1;
        x = Math.abs(x);
        int min = (int)Math.pow(2,31);
        int max = min - 1;
        while(x > 0){
            int digit = x % 10;
            x = x / 10;
            if(k==1){
                if(res > max/10 || (res == max/10 && digit >  max%10)){
                    return 0;
                }
            }
            else{
                if(res > min/10 || (res == min/10 && digit >  min%10)){
                    return 0;
                }
            }
            res = res*10 + digit;
        }

        

        return res*k;
    }
}