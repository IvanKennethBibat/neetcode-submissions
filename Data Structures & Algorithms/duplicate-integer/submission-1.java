class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        for (int i = 0; i < nums.length; i++){

            int currentNum = nums[i];
            if(!seen.contains(currentNum)){
                seen.add(currentNum);
            }
            else{
                return true;
            }
        }
        return false;
    }
}