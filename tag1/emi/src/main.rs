use std::fs;

fn main() {
    let content = fs::read_to_string("input_emi.txt").expect("File could not be read");
    let sum = part_one(&content);
    println!("part one: {sum}");
    let sum = part_two(&content);
    println!("part two: {sum}");
}
fn begins_with_number(input: &str) -> Option<u32> {
    let words = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ];
    let first_char = input.chars().next().unwrap();
    let maybe_digit = first_char.to_digit(10);
    if maybe_digit.is_some() {
        return maybe_digit;
    }
    for (index, word) in words.into_iter().enumerate() {
        if input.starts_with(word) {
            return Some(index as u32 + 1);
        }
    }
    return None;
}
fn part_two(content: &str) -> u32 {
    let mut sum = 0;
    for line in content.lines() {
        let mut first = None;
        let mut last = None;
        for i in 0..line.len() {
            let res = begins_with_number(&line[i..]);
            if first.is_none() {
                first = res;
            }
            if res.is_some() {
                last = res;
            }
        }
        sum += first.unwrap() * 10 + last.unwrap();
    }
    sum
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
