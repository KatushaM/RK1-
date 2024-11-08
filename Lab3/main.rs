use std::env;
use rand::Rng;



fn discriminate(a: i32, b: i32, c: i32) -> f64 {
    (b * b) as f64 - 4.0 * (a * c) as f64
}

fn calc_solutions(discr: f64, a: i32, b: i32) -> Vec<f64> {
    let mut roots = Vec::new();
    if discr == 0.0 {
        roots.push(-b as f64 / (2.0 * a as f64));
    }
    if discr > 0.0 {
        roots.push((-b as f64 + discr.sqrt()) / (2.0 * a as f64));
        roots.push((-b as f64 - discr.sqrt()) / (2.0 * a as f64));
    }
    roots
}

fn get_abc(index: usize, text: &str) -> f64 {
    env::args().nth(index).map_or_else(
        || {
            println!("{}", text);
            let mut input = String::new();
            std::io::stdin().read_line(&mut input).unwrap();
            input.trim().parse::<f64>().unwrap()
        },
        |arg| arg.parse::<f64>().unwrap(),
    )
}

fn main() {
    println!("Do you want to set the coefficients yourself?");
    println!("1-yes, 2-no");
    let mut koef = String::new();
    std::io::stdin().read_line(&mut koef).unwrap();
    let koef: i32 = koef.trim().parse().unwrap();

    let (a, b, c);
    if koef == 1 {
        a = get_abc(1, "A: ") as i32;
        b = get_abc(2, "B: ") as i32;
        c = get_abc(3, "C: ") as i32;
    } else {
        let mut rng = rand::thread_rng();
        a = rng.gen_range(1..=100);
        b = rng.gen_range(1..=100);
        c = rng.gen_range(1..=100);
        println!("A = {}\nB = {}\nC = {}", a, b, c);
    }

    let discr = discriminate(a, b, c);
    let solutions = calc_solutions(discr, a, b);
    
    match solutions.len() {
        0 => println!("No roots. Discriminate < 0"),
        1 => {
            println!("1 Solution:");
            println!("{:?}", solutions);
        }
        _ => {
            println!("2 Solutions:");
            println!("{:?}", solutions);
        }
    }
}


