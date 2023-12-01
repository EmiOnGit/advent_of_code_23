use std::fs;

fn main() {
    let content = fs::read_to_string("input_emi.txt").expect("File could not be read");
    let sum = part_one(&content);
    println!("part one: {sum}");
}
fn part_one(content: &str) -> u32 {
    content
        // iterate over the lines of the file content
        .lines()
        .map(|line| {
            // iterate over the characters of the line
            line.chars()
                .into_iter()
                // only keep the characters that are numbers
                .filter_map(|c| c.to_digit(10))
                // collect them into a list
                .collect::<Vec<u32>>()
        })
        // only keep the first and last element of the list
        .map(|v| [v[0] * 10, v[v.len() - 1]])
        .flatten()
        .sum()
}
