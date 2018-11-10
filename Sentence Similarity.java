public class Solution {
    /**
     * @param words1: a list of string
     * @param words2: a list of string
     * @param pairs: a list of string pairs
     * @return: return a boolean, denote whether two sentences are similar or not
     */
    public boolean isSentenceSimilarity(String[] words1, String[] words2, List<List<String>> pairs) {
        // write your code here
        HashMap<String, String> relation = new HashMap<String, String>();

        
        for (List<String> s: pairs) {
            relation.put(s.get(0), s.get(1));
        }
        boolean res = true;
        for (int i = 0; i < words1.length; i++) {
            if(words1[i] == words2[i]) {
                continue;
            }
            else if(relation.containsKey(words1[i])) {
                if(!relation.get(words1[i]).equals(words2[i])){
                    res = false;
                } else {
                    res = true;
                }
            } 
            if(relation.containsKey(words2[i])) {
                if(!relation.get(words2[i]).equals(words1[i])) {
                    res = false;
                } else {
                    res = true;
                }
            } 
        }
        return res;
    }
}