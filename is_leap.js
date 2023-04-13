function isLeap(year) {
    if (year % 4 === 0) {
        if (year % 100 === 0) {
            if (year % 400 === 0) {
                return true;
            }
            else {
                return false;
            }
        }
        return true;
    }
    else {
        return false;
    }
}

// isLeap(1993);
// isLeap(2000);
// isLeap(1900);
console.log(isLeap(2400));
