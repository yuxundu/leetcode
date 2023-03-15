class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> groupMap = new HashMap<>();
        for(String str : strs){
            int[] counts = new int[26];
            for(char c : str.toCharArray()){
                int index = c - 'a';
                counts[index] += 1;
            }
            String key = Arrays.toString(counts);
            List<String> list = groupMap.getOrDefault(key,new ArrayList<String>());
            list.add(str);
            groupMap.put(key,list);
        }
        List<List<String>> ans = new ArrayList<>();
        for(List<String> list : groupMap.values()){
            ans.add(list);
        }
        return ans;
        
    }
}