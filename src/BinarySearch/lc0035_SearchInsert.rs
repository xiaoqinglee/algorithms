pub struct Solution;

// https://leetcode.cn/problems/search-insert-position/
// 也许找到0个, 1个, 或多个.
impl Solution {
    //// 如果找多个匹配的元素时, 允许返回任意一个匹配元素的索引.
    //
    // pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
    //     // pub fn binary_search(&self, x: &T) -> Result<usize, usize>
    //     // Binary searches this slice for a given element.
    //     // If the slice is not sorted, the returned result is unspecified and meaningless.
    //     //
    //     // If the value is found then Result::Ok is returned, containing the index of the matching element.
    //     // If there are multiple matches, then any one of the matches could be returned.
    //     // The index is chosen deterministically, but is subject to change in future versions of Rust.
    //     // If the value is not found then Result::Err is returned, containing the index where a matching element could be inserted while maintaining sorted order.
    //     nums.binary_search(&target).unwrap_or_else(|x| x) as i32
    // }

    // 如果找多个匹配的元素时, 只允许返回第一个匹配元素的索引. 也即返回第一个大于等于target的元素的索引.
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        //// partition_point用法:
        //
        // let s = [0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55];
        //
        // let low = s.partition_point(|x| x < &1);
        // assert_eq!(low, 1);
        // let high = s.partition_point(|x| x <= &1);
        // assert_eq!(high, 5);
        // let r = s.binary_search(&1);
        // assert!((low..high).contains(&r.unwrap()));
        //
        // assert!(s[..low].iter().all(|&x| x < 1));
        // assert!(s[low..high].iter().all(|&x| x == 1));
        // assert!(s[high..].iter().all(|&x| x > 1));
        //
        // // For something not found, the "range" of equal items is empty
        // assert_eq!(s.partition_point(|x| x < &11), 9);
        // assert_eq!(s.partition_point(|x| x <= &11), 9);
        // assert_eq!(s.binary_search(&11), Err(9));
        nums.partition_point(|x| x < &target) as i32
    }
}
