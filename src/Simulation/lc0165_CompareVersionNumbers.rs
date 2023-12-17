use std::cmp;

pub struct Solution;

//https://leetcode.cn/problems/compare-version-numbers/
impl Solution {
    pub fn compare_version(version1: String, version2: String) -> i32 {
        fn cast(s: &str) -> i32 {
            s.parse::<i32>().unwrap()
        }
        let mut version1 = version1.split('.').map(cast);
        let mut version2 = version2.split('.').map(cast);
        loop {
            let (v1, v2) = (version1.next(), version2.next());
            if v1.is_none() && v2.is_none() {
                return 0;
            }
            match v1.unwrap_or_default().cmp(&v2.unwrap_or_default()) {
                cmp::Ordering::Less => return -1,
                cmp::Ordering::Greater => return 1,
                cmp::Ordering::Equal => continue,
            }
        }
    }
}
