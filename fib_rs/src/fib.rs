use std::fmt::Display;

#[derive(Debug, Clone)]
pub struct Fib {
    curr: u64,
    next: u64,
}

impl Fib {
    pub fn new() -> Self {
        Fib { curr: 0, next: 1 }
    }

    pub fn advance(&mut self) {
        let next = self.curr + self.next;
        self.curr = self.next;
        self.next = next;
    }
}

impl Iterator for Fib {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        let curr = self.curr;
        self.advance();
        Some(curr)
    }
}

impl Display for Fib {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.curr)
    }
}

#[cfg(test)]
mod tests {
    use super::Fib;

    #[test]
    fn test_fib_advance() {
        let mut dut = Fib::new();
        let expected: Vec<u64> = vec![0, 1, 1, 2, 3, 5, 8, 13, 21, 34];
        let mut actual: Vec<u64> = Vec::new();

        for _ in 0..expected.len() {
            actual.push(dut.curr);
            dut.advance();
        }

        assert_eq!(expected, actual);
    }

    #[test]
    fn test_fib_iter() {
        let dut = Fib::new();
        let expected: Vec<u64> = vec![0, 1, 1, 2, 3, 5, 8, 13, 21, 34];
        let actual: Vec<u64> = dut.take(10).collect();
        assert_eq!(expected, actual);
    }
}
