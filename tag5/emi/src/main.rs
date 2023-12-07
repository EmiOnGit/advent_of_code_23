use rayon::iter::IntoParallelIterator;
use rayon::iter::ParallelIterator;
use std::{error::Error, fs::read_to_string, ops::Range};

fn main() -> Result<(), Box<dyn Error>> {
    let input = read_to_string("../input_emi.txt")?;
    let (seeds, layers) = parse(&input).unwrap();
    let seed_count: usize = seeds.0.iter().map(|r| r.clone().count()).sum();
    println!("count: {seed_count}");
    let min = seeds
        .0
        .into_iter()
        .flat_map(|seed_range| {
            seed_range
                .into_par_iter()
                .map(|seed| layers.apply(seed))
                .min()
        })
        .min()
        .unwrap();
    println!("result: {min:?}");

    Ok(())
}
#[derive(Debug)]
pub struct Map {
    pub from: u32,
    pub to: u32,
    pub range: u32,
}
#[derive(Debug)]
pub struct Layer {
    pub maps: Vec<Map>,
}
#[derive(Debug)]
pub struct Seeds(Vec<Range<u32>>);
#[derive(Debug)]
pub struct Layers(Vec<Layer>);
impl Map {
    pub fn map(&self, v: u32) -> Option<u32> {
        if self.from <= v && self.from + self.range > v {
            Some(v + (self.to - self.from))
        } else {
            None
        }
    }
    pub fn parse(v: &[u32]) -> Self {
        Self {
            to: v[0],
            from: v[1],
            range: v[2],
        }
    }
}
impl Layer {
    pub fn new(maps: Vec<Map>) -> Self {
        Self { maps }
    }
    pub fn apply(&self, v: u32) -> u32 {
        self.maps.iter().find_map(|map| map.map(v)).unwrap_or(v)
    }
}
impl Layers {
    pub fn apply(&self, value: u32) -> u32 {
        self.0
            .iter()
            .fold(value, |current, layer| layer.apply(current))
    }
}
fn parse(input: &str) -> Option<(Seeds, Layers)> {
    let mut categories = input.split(':');
    categories.next(); // skip "seeds:"
    let to_numbers = |input: &str| -> Vec<u32> {
        input
            .split_whitespace()
            .filter_map(|n| n.parse::<u32>().ok())
            .collect()
    };
    let numbers: Vec<u32> = to_numbers(categories.next()?);

    let seeds: Vec<Range<u32>> = numbers.chunks(2).map(|n| n[0]..(n[0] + n[1])).collect();

    let layers: Vec<Layer> = categories
        .map(to_numbers)
        .map(|n| n.chunks(3).map(Map::parse).collect::<Vec<Map>>())
        .map(Layer::new)
        .collect();
    Some((Seeds(seeds), Layers(layers)))
}
