use std::collections::HashMap;

pub struct Solution;

//https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        let num_to_chars: HashMap<i32, Vec<char>> = [
            (2, vec!['a', 'b', 'c']),
            (3, vec!['d', 'e', 'f']),
            (4, vec!['g', 'h', 'i']),
            (5, vec!['j', 'k', 'l']),
            (6, vec!['m', 'n', 'o']),
            (7, vec!['p', 'q', 'r', 's']),
            (8, vec!['t', 'u', 'v']),
            (9, vec!['w', 'x', 'y', 'z']),
        ]
        .into();

        if digits.len() == 0 {
            return vec![];
        }
        let digits: Vec<i32> = digits
            .chars()
            .map(|c| c.to_string().parse::<i32>().unwrap())
            .collect();
        let mut wip: Vec<char> = vec![];
        let mut result: Vec<String> = vec![];

        fn combinations(
            num_to_chars: &HashMap<i32, Vec<char>>,
            digits: &[i32],
            wip: &mut Vec<char>,
            fixed_n_digits: usize,
            result: &mut Vec<String>,
        ) {
            if fixed_n_digits == digits.len() {
                result.push(wip.iter().collect::<String>());
                return;
            }
            for &candidate_on_current_digit in &num_to_chars[&digits[fixed_n_digits]] {
                wip.push(candidate_on_current_digit);
                combinations(num_to_chars, digits, wip, fixed_n_digits + 1, result);
                wip.pop();
            }
        }
        combinations(&num_to_chars, &digits, &mut wip, 0, &mut result);
        result
    }
}
