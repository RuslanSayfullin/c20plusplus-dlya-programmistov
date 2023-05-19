const watchList = new Set(['Сияние', 'Интерстеллар', 'Казино'])
const values = watchList.values()
console.log(values)

for (const key of values){
	console.log(key)
}

const movies = [...values]
console.log(movies)
