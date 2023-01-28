class Solution {
    public int strStr(String haystack, String needle) {
        int lengthH = haystack.length();
        int lengthN = needle.length();
        int[] lps = computerLPS(needle,lengthN);

        int i = 0, j = 0;
        while(i < lengthH){
            char haystackC = haystack.charAt(i);
            char needleC = needle.charAt(j);
            if(haystackC == needleC){
                i++;
                j++;
            }
            else{
                if(j != 0 ){
                    j = lps[j-1];
                }
                else{
                    j=0;
                    i++;
                }
            }
            if(j == lengthN){
                return i - lengthN;
            }


        }
        return -1;
        
    }

    public int[] computerLPS(String needle,int lengthN){
        int[] lps = new int[lengthN];
        int len = 0, i = 1;
        lps[0] = 0;
        while(i < lengthN){
            char prevC = needle.charAt(len);
            char currC = needle.charAt(i);
            if(prevC == currC){
                lps[i] = len+1;
                i++;
                len++;
            }
            else{
                if(len!=0){
                    len = lps[len-1];
                }
                else{
                    lps[i] = 0;
                    i++;
                }

            }
        }
        return lps;

    }
}