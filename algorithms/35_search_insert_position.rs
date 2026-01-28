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

fn search_insert(nums: &[i32], target: i32) -> usize {
    let mut l = 0;
    let mut r = nums.len(); // r — за пределами, поэтому тип usize

    while l < r {
        let mid = l + (r - l) / 2;

        if nums[mid] < target {
            l = mid + 1; // ищем справа
        } else {
            r = mid; // nums[mid] >= target → ищем слева (включая mid)
        }
    }

    l // в конце l == r — это и есть позиция вставки
}

fn main() {
    let nums: [i32; 5] = [1, 3, 4, 5, 6];
    let target: i32 = 2;

    let ans = search_insert(&nums, target);
    assert_eq!(ans, 1);
    let nums: [i32; 5] = [1, 2, 3, 4, 5];
    let target: i32 = 0;
    let ans = search_insert(&nums, target);
    assert_eq!(ans, 0);
    println!("{:?}", nums);
}
