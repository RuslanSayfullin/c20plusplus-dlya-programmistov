/**Memoization - это техника оптимизации производительности, 
*которая заключается в сохранении результатов выполнения функции 
*для последующих вызовов с теми же аргументами. 
*Это позволяет избежать повторных вычислений и уменьшить нагрузку на процессор и память.
*/
function fibonacci(n, memo = {}) {
	if (n in memo) {
		return memo[n];
	}
	if (n <= 1){
		return n;
	}
	memo[n] = fibonacci(n-1, memo) + fibonacci(n - 2, memo);
	return memo[n];
}

console.log(fibonacci(10)); //55
console.log(fibonacci(15)); //610
