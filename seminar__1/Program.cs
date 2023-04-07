// Нахождение квадрата числа
//Console.WriteLine ("Введите число");
//int number = Convert.ToInt32(Console.ReadLine());
//number = number*number;
//number*=number
//Console.WriteLine(number);

Console.WriteLine ("Введите первое число");
int firstnumber = Convert.ToInt32(Console.ReadLine());
Console.WriteLine ("Введите втрое число");
int secondnumber = Convert.ToInt32(Console.ReadLine());
if (firstnumber == secondnumber*secondnumber)
{
     Console.WriteLine ("Число один является квадратом числа два");  
}
else
{
    Console.WriteLine ("Число один не является квадратом чисда два");
}