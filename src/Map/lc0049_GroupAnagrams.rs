use std::collections::HashMap;

pub struct Solution;

impl Solution {
    // pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
    //     let mut out: HashMap<Vec<char>, Vec<String>> = HashMap::new();
    //     for s in strs {
    //         let mut key: Vec<char> = s.chars().collect();
    //         key.sort_unstable();
    //         out.entry(key).or_insert(vec![]).push(s)
    //     }
    //     // out.into_iter().map(|(_, v)| v).collect()
    //     out.into_values().collect()
    // }

    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        strs.into_iter()
            .fold(HashMap::new(), |mut acc, item| {
                let mut key: Vec<char> = item.chars().collect();
                key.sort_unstable();
                acc.entry(key).or_insert(vec![]).push(item);
                acc
            })
            .into_values()
            .collect()
    }
}
