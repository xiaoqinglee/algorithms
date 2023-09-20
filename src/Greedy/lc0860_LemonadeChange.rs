use std::collections::BTreeMap;

pub struct Solution;

//https://leetcode.cn/problems/lemonade-change/
impl Solution {
    pub fn lemonade_change(bills: Vec<i32>) -> bool {
        //使用面额的负数作为 key 以便 treemap 元素的迭代顺序符合我们的需求
        let mut bill_counter = BTreeMap::from([(-20, 0), (-10, 0), (-5, 0)]);
        let (&smallest_neg, _) = bill_counter.last_key_value().unwrap();
        for received in bills {
            *bill_counter.get_mut(&-received).unwrap() += 1;
            if received == -smallest_neg {
                continue;
            }
            let mut remains = received - (-smallest_neg);
            for (k, count) in &mut bill_counter {
                let return_candidate = -*k;
                if return_candidate > remains {
                    continue;
                }
                let div = remains / return_candidate;
                let return_candidate_count = div.min(*count);
                *count -= return_candidate_count;
                remains -= return_candidate * return_candidate_count;
                if remains == 0 {
                    break;
                }
            }
            if remains != 0 {
                return false;
            }
        }
        true
    }
}
