mod fib;
use fib::Fib;

fn main() {
    println!("Naive");
    let fib: u64 = 0;
    println!("{fib}");
    let fib: u64 = 1;
    println!("{fib}");
    let fib: u64 = 1;
    println!("{fib}");
    let fib: u64 = 2;
    println!("{fib}");
    let fib: u64 = 3;
    println!("{fib}");

    println!("functional tuple");
    fn fib_next_tuple(curr: u64, next: u64) -> (u64, u64) {
        (next, curr + next)
    }

    let (mut curr, mut next) = (0, 1);
    println!("{}", curr);

    for _ in 0..=5 {
        (curr, next) = fib_next_tuple(curr, next);
        println!("{}", curr);
    }

    println!("functional struct");

    struct FibStruct {
        curr: u64,
        next: u64,
    }
    fn fib_next_struct(fib: FibStruct) -> FibStruct {
        FibStruct {
            curr: fib.next,
            next: fib.curr + fib.next,
        }
    }

    let mut fib = FibStruct { curr: 0, next: 1 };
    println!("{}", fib.curr);

    for _ in 0..=5 {
        fib = fib_next_struct(fib);
        println!("{}", fib.curr);
    }

    println!("method struct");

    let mut fib = Fib::new();
    println!("{fib}");

    for _ in 0..=5 {
        fib.advance();
        println!("{fib}");
    }

    println!("iterator");

    let fib = Fib::new();

    fib.clone().take(5).for_each(|f| println!("{f}"));

    for f in fib.take(5) {
        println!("{f}")
    }
}
