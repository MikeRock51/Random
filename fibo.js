function fibGen(n) {
    var fib = []

    for (let i = 0; i < n; i++) {
        if (i === 0 || i === 1) {
            fib.push(i);
        }
        else {
            fib.push(fib[i - 1] + fib[i - 2])
        }
    }
    return fib;
}

console.log(fibGen(1))