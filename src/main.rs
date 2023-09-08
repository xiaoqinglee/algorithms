use algorithms::Simulation::lc0165_CompareVersion::Solution;

fn main() {
    dbg!(Solution::compare_version(
        String::from("1.1"),
        String::from("1.1.0")
    ));
}
