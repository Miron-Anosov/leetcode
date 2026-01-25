// https://leetcode.com/problems/search-insert-position/description/ 
/*
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104

*/ 
#include <stdio.h>

int searchInsert(int* nums, int numsSize, int target) {
    int l_c = 0;
    int r_c = numsSize -1;
    int mid;

    while (l_c <= r_c) {
        mid = l_c + (r_c - l_c) / 2;
        if (nums[mid] == target) {
            return mid;
        }
        else if (nums[mid] > target) {
            r_c = mid -1;       
        }
        else {
            l_c = mid + 1;
        }
    
    }

    return l_c;
}

int main(){
    int arr[] = {1, 3, 5, 6};
    int size = 4;
    int target = 0;

    int result = searchInsert(arr, size, target);

    printf("target index: %d", result);

    return 0;
}
