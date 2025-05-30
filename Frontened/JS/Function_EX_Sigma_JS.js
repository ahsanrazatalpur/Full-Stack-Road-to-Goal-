//Qno 1
function isPrime(number) {
    if(number %1 == 0 && number %2 == 0){
        return true;
    }
    else{
        return false;
    }

}
console.log(isPrime(10));
console.log(isPrime(7));
//Qno 2 
function EvenOdd(number){
    if(number %2 == 0)
    console.log("Even Number");
    else
     console.log("Odd number");
}
EvenOdd(2);
EvenOdd(8);
EvenOdd(9);
EvenOdd(17);

// Qno 3
function IsPalindrome(str) {
    let reverse = "";
    for (let i = str.length - 1; i >= 0; i--) {
        reverse += str[i];
    }
    if (str === reverse)
        console.log("Palindrome");
    else
        console.log("Not Palindrome");
}

IsPalindrome("madam");
IsPalindrome("tibet");
IsPalindrome("civic");
IsPalindrome("brother");
IsPalindrome("car");


