// Задаем дату, до которой нужно узнать количество дней
const endDate = new Date('2023-12-31');

// Получаем текущую дату
const today = new Date();

// Вычесляем разницу в миллисекундах между текущей датой и заданной датой
const diffInMs = endDate - today;

// Вычесляем кол-во дней, оставшихся до заданной даты, округляяя до целых с помощью Math.floor()
const remainingDays = Math.floor(diffInMs / (1000 * 60 * 60 *24));

//Выводим результат в консоль
console.log('До ${endDate.toLocaleDateString()} осталось ${remainingDays} дней.');
