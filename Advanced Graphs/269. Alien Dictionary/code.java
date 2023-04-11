class Solution {
    public String alienOrder(String[] words) {

        Map<Character,Set<Character>> adj = new HashMap<>();

        for(String word : words){
            for(Character c : word.toCharArray()){
                adj.put(c, new HashSet());
            }
        }

        for(int i = 0; i < words.length - 1; i++){
            String first = words[i];
            String second = words[i+1];
            int minLen = Math.min(first.length(),second.length());
            if(first.substring(0,minLen).equals(second.substring(0,minLen)) && first.length() > second.length()){
                return "";
            }
            for(int j = 0; j < minLen; j++){
                if(first.charAt(j) != second.charAt(j)){
                    adj.get(first.charAt(j)).add(second.charAt(j));
                    break;
                }
            }
        }  

        StringBuffer sb = new StringBuffer();
        Map<Character,Boolean> visiting = new HashMap<>();

        for(Character c : adj.keySet()){
            if(dfs(visiting,c,sb,adj)){
                return "";
            }
        }
        
        return sb.reverse().toString();
    }

    public boolean dfs(Map<Character,Boolean> visiting, Character c, StringBuffer sb,Map<Character,Set<Character>> adj){
        if(visiting.containsKey(c)){
            return visiting.get(c);
        }
        visiting.put(c,true);

        for(Character neighbour : adj.get(c)){
            if(dfs(visiting, neighbour, sb, adj)){
                return true;
            }
        }

        visiting.put(c,false);
        sb.append(c);
        return false;
    }
}