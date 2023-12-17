pub struct Solution;

use std::collections::HashMap;

// https://leetcode.cn/problems/find-words-that-can-be-formed-by-characters/
impl Solution {
    pub fn count_characters(words: Vec<String>, chars: String) -> i32 {
        let mut letters = HashMap::new();
        chars.chars().for_each(|ch| {
            letters
                .entry(ch)
                .and_modify(|counter| *counter += 1)
                .or_insert(1);
        });
        dbg!(&letters);

        // let mut letters = HashMap::<_, i32>::new();
        // chars
        //     .chars()
        //     .for_each(|ch| *letters.entry(ch).or_default() += 1);
        // dbg!(&letters);
        //
        // let mut letters = HashMap::new();
        // chars
        //     .chars()
        //     .for_each(|ch| *letters.entry(ch).or_insert(0i32) += 1);
        // dbg!(&letters);

        words
            .iter()
            .filter(|word| -> bool {
                let mut letters = letters.clone();
                !word.chars().any(|ch| -> bool {
                    letters
                        .entry(ch)
                        .and_modify(|counter| *counter -= 1)
                        .or_insert(-1)
                        < &mut 0
                })
            })
            .map(String::len)
            .sum::<usize>() as i32
    }
}
