# Stacks-and-Queues-Homework

1.	Напишете програма която чете от конзолата поредица от числа разделени със (, )запетая и спейс и ги печата на конзолата в обратен ред, разделени само със спейс – използвайте стек
Пример: 1, 2, 3, 4, 5 -> 5 4 3 2 1

2.	Напишете програма която извършва различни манипулации със стек, който първоначално е празен. 
-	На първия ред ще прочетете n-цяло число и след това за n-пъти ще получавате команди:
•	1 {число} – поставете числото най-отзад на стека
•	2 - изтрий числото което е най-отгоре на стека
•	3 – принтирай най-голямото число в стека
•	4 – принтирай най малкото число в стека
•	5  - принтирай дължината на стека
Накрая принтирайте стека като започнете от последния добавен елемент и стигнете до първия
Примерни входове
Input	Output
10
1 97
2
1 20
2
1 26
1 20
5
3
1 91
4	2
26
20
91, 20, 26

11
2
1 47
1 66
1 32
4
3
5
1 25
1 16
1 8
4	32
66
3
8
8, 16, 25, 32, 66, 47

3.	Имате заведение за бързо хранене, като храната, която предлагате е предварително приготвена. Напишете програма, която проверява дали имате достатъчно храна, за да сервирате обяд на всички ваши клиенти. Също така искате да знаете кой е клиентът с най-голяма поръчка за този ден. 
•	Първо ще ви бъде дадено количеството храна, което имате за деня (цяло число). След това ще ви бъде дадена поредица от цели числа (разделени с един интервал), всяко от които представлява количеството храна във всяка поръчка. Съхранявайте поръчките на опашка.
•	Намерете най-голямата поръчка и я отпечатайте. След това ще започнете да обслужвате клиентите си от първия до последния по ред на идване. Преди всяка поръчка проверявайте дали имате достатъчно храна, за да я изпълните:
o	Ако имате, премахнете поръчката от опашката и намалете количеството храна в ресторанта.
o	 В противен случай спрете сервирането.
Входни данни:
• На първия ред ще ви бъде дадено количеството на вашата храна - цяло число
• На втория ред ще получите поредица от цели числа, представляващи всяка поръчка, разделени с един интервал
Изходни данни:
• На първия ред отпечатайте количеството на най-голямата поръчка
• На втория ред:
o Ако сте успели да обслужите всичките си клиенти, отпечатайте: „Orders complete“.
o В противен случай отпечатайте: „Оставащи поръчки: {order1}, {order2} .... {orderN}“.

Вход	Изход
348
20 54 30 16 7 9	54
Orders complete
499
57 45 62 70 33 90 88 76 100 50	100
Orders left: 76, 100, 50



4.	Вие притежавате моден бутик и получавате доставка едно пале с дрехи, представен като последователност от цели числа. На следващия ред ще ви бъде дадено цяло число, представляващо капацитета на един стелаж във вашия магазин. Трябва да подредите дрехите в магазина и да използвате стелажите, за да подредите всяка дреха. Започвате от най-горните дрехи на палето. Използвайте стек. От всяка дреха има количество (цяло число). Трябва да сумирате техните стойности, докато ги премахвате от палето:
• Ако сборът стане равен на капацитета на текущия стелаж, трябва да започнете нов за следващите дрехи (ако има останали на палето).
• Ако сборът стане по-голям от капацитета, не поставяйте дрехите на текущия стелаж. Вземете нов.
Накрая отпечатайте колко стелажи сте използвали за подреьдане на дрехите.
Входни данни:
• На първия ред ще ви бъде дадена поредица от цели числа, представляващи дрехите на палето, разделени с един интервал.
• На втория ред ще ви бъде дадено цяло число, представляващо капацитета на стелажа.
Изходни данни:
• Отпечатайте броя на стелажите, необходими за подредба на дрехите от палето.
Подсказка:
• Нито едно от целите числа от кутията няма да бъде по-голямо от стойността на капацитета
Вход	Изход
5 4 8 6 3 8 7 7 9
16	5
1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
20	5

