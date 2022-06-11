# **Лабораторна робота №2**

-----------------------------------
## Необхідні ресурси:
- Встановлений компілятор для Python.

## Інформація про програму:
- Виводить в терміналі "Hello World!".
- Виконує команди: ping, echo, login, list, msg, file, exit.

## Опис Команд:
### 1. Команда `ping <Address: String>`.
#### Ця команда перевіряє зєднання з сервером, сайтом чи будь-яким іншим пристроєм за вказаною IP або DNS адресою. Дані команді передається тільки один параметр - `<Address: String>`
#### Результатом виконання у разі успішного зєднання в першому рядку записується `Ping <Address: String> ...` і в наступному рядку `Ping <Address: String> request success.`.
#### Якщо ж кількість введених параметрів не буде рівна "1", то замість результату виводиться повідомлення з описом помилки в дужках`PING ERROR (Incorect input argument)`

### Приклад виконання команди:
```text

Hello World!
========================================
Input Command: ping google.com
Entered command = "ping", parameters = ['google.com']
----------------------------------------

Results:
Ping google.com ...
Ping google.com request success.
========================================
Input Command: ping 192.168.1.1
Entered command = "ping", parameters = ['192.168.1.1']
----------------------------------------

Results:
Ping 192.168.1.1 ...
Ping 192.168.1.1 request success.
========================================
Input Command: ping
Entered command = "ping", parameters = []
----------------------------------------

Results:
PING ERROR (Incorect input argument)
========================================
Input Command: ping google.com youtube.com
Entered command = "ping", parameters = ['google.com', 'youtube.com']
----------------------------------------

Results:
PING ERROR (Incorect input argument)
```

### 2. Команда `echo <anyText: String> <anyText: String> ...`.
#### Ця команда виводить на екрані текст з вхідних параметрів - `<anyText: String>`. Ця команда може отримувати будь-яку кількість параметрів. Кожний параметр відображається в новому рядку.

### Приклад виконання команди:
```text

Hello World!
========================================
Input Command: echo hello
Entered command = "echo", parameters = ['hello']
----------------------------------------

Results:
hello
========================================
Input Command: echo Hello Lab2
Entered command = "echo", parameters = ['Hello', 'Lab2']
----------------------------------------

Results:
Hello
Lab2
========================================
Input Command: echo "Hello World"
Entered command = "echo", parameters = ['Hello World']
----------------------------------------

Results:
Hello World
```

### 3. Команда `login <login: String> <password: String>`.
#### Ця команда дозволяє користувачу залогінитися. Дані команді передається два параметри - `<login: String>` і `<password: String>`.
#### Результатом виконання команди буде:
- Якщо логін даного користувача немає в базі даних, то в консолі виводиться `LOGIN ERROR (Incorect input login or password)`.
- Якщо логін даного користувача є в базі даних, але відповідний до нього пароль введений неправильно, то в консолі виводиться `LOGIN ERROR (Incorect input login or password)`.
- Якщо логін даного користувача є в базі даних, і відповідний до нього пароль введений правильно, то в першому рядку консолі виводиться - `LOGIN SUCCESS:`, а в наступному рядку - `Hello, <nameUsers: String>`.
- Якщо кількість введених параметрів не дорівнює 2, то в консолі виводиться `LOGIN ERROR (Incorect input argument)`.

### Приклад виконання команди:
```text

Hello World!
========================================
Input Command: login Pudge_std std101
Entered command = "login", parameters = ['Pudge_std', 'std101']
----------------------------------------

Results:
LOGIN SUCCESS:
 Hello, Pudge
========================================
Input Command: login Ogre_std student
Entered command = "login", parameters = ['Ogre_std', 'student']
----------------------------------------

Results:
LOGIN ERROR (Incorect input login or password)
========================================
Input Command: login pavlo 123
Entered command = "login", parameters = ['pavlo', '123']
----------------------------------------

Results:
LOGIN ERROR (Incorect input login or password)
========================================
Input Command: login Oleg
Entered command = "login", parameters = ['Oleg']
----------------------------------------

Results:
LOGIN ERROR (Incorect input argument)
```

### 4. Команда `list`.
#### Ця команда виводить на екран список назв всіх зареєстрованих користувачів які знаходяться в базі даних. Для цієї команди не потрібно вводити параметри, якщо було введено параметри то вони ігноруються. Назва кожного користувача відображається в новому рядку з його поряковим номером - `<№Users: Int>. <nameUsers: String>` .
#### База даних:
- user_names = `Pudge`, `Cm`, `Wisp`, `Ogre`
- user_logins = `Pudge_std`, `Cm_std`, `Wisp_std`, `Ogre_std`
- user_passwords = `std101`, `std102`, `std103`, `std104`

### Приклад виконання команди:
```text

Hello World!
========================================
Input Command: list
Entered command = "list", parameters = []
----------------------------------------

Results:
1. Pudge
2. Cm
3. Wisp
4. Ogre
========================================
Input Command: list lab
Entered command = "list", parameters = ['lab']
----------------------------------------

Results:
1. Pudge
2. Cm
3. Wisp
4. Ogre
```

### 5. Команда `msg <destinationUser: String> <text: String>`.
#### Ця команда надсилає текстове повідомлення іншому користувачу. Дані команді передається два параметри - `<destinationUser: String>` і ` <text: String>`.
#### Результатом виконання команди буде:
- Якщо назви даного користувача немає в базі даних, то в консолі виводиться `MESSAGE SENDING ERROR (This user not found)`.
- Якщо назва даного користувача є в базі даних, то в консолі виводиться `MESSAGE SENDING SUCCESS`.
- Якщо кількість введених параметрів не дорівнює 2, то в консолі виводиться `MESSAGE SENDING ERROR (Incorect input argument)`.

### Приклад виконання команди:
```text

Hello World!
========================================
Input Command: msg Cm 'Lab2 Hello'
Entered command = "msg", parameters = ['Cm', 'Lab2 Hello']
----------------------------------------

Results:
MESSAGE SENDING SUCCESS
========================================
Input Command: msg Pavlo "No Name"
Entered command = "msg", parameters = ['Pavlo', 'No Name']
----------------------------------------

Results:
MESSAGE SENDING ERROR (This user not found)
========================================
Input Command: msg Wisp 
Entered command = "msg", parameters = ['Wisp']
----------------------------------------

Results:
MESSAGE SENDING ERROR (Incorect input argument)
```

### 6. Команда `file <destinationUser: String> <filename: String>`.
#### Ця команда надсилає файлове повідомлення іншому користувачу. Дані команді передається два параметри - `<destinationUser: String>` і ` <filename: String>`.
#### Результатом виконання команди буде:
- Якщо назви даного користувача немає в базі даних, то в консолі виводиться `FILE SENDING ERROR (User not found)`.
- Якщо назва даного користувача є в базі даних, але даного файлу немає, то в консолі виводиться `FILE SENDING ERROR (File not found)`.
- Якщо назва даного користувача є в базі даних, і цей файл існує, то в консолі виводиться `FILE SENDING SUCCESS`.
- Якщо кількість введених параметрів не дорівнює 2, то в консолі виводиться `FILE SENDING ERROR (Incorect input argument)`.

### Приклад виконання команди:
```text

Hello World!
========================================
Input Command: file Ogre README.md
Entered command = "file", parameters = ['Ogre', 'README.md']
----------------------------------------

Results:
FILE SENDING SUCCESS
========================================
Input Command: file Cm Laba
Entered command = "file", parameters = ['Cm', 'Laba']
----------------------------------------

Results:
FILE SENDING ERROR (File not found)
========================================
Input Command: file Oleg Lab2.py
Entered command = "file", parameters = ['Oleg', 'Lab2.py']
----------------------------------------

Results:
FILE SENDING ERROR (User not found)
========================================
Input Command: file naturlich
Entered command = "file", parameters = ['naturlich']
----------------------------------------

Results:
FILE SENDING ERROR (Incorect input argument)
```

### 7. Команда `exit`.
#### Ця команда виходить з циклу для опитування введення команд. Для цієї команди не потрібно вводити параметри, якщо було введено параметри то вони ігноруються.
- Результатом виконання команди буде - `Exit from cycle`

### Приклад виконання команди:
```text

Hello World!
========================================
Input Command: list
Entered command = "list", parameters = []
----------------------------------------

Results:
1. Pudge
2. Cm
3. Wisp
4. Ogre
========================================
Input Command: exit nash
Entered command = "exit", parameters = ['nash']
----------------------------------------

Results:
Exit from cycle

Hello World!
========================================
Input Command: list 
Entered command = "list", parameters = []
----------------------------------------

Results:
1. Pudge
2. Cm
3. Wisp
4. Ogre
========================================
Input Command: exit
Entered command = "exit", parameters = []
----------------------------------------

Results:
Exit from cycle

```

### Примітка: щоб ввести текст в якому містяться символ " " потрібно використовувати адинарні або подвійні дужки в кінці і на початку тексту.
### Примітка: Якщо було некоректно введено команду або її не існує, то в консолі виводиться `No Command = "<comand>"`.

### Приклад спроби виконання іншої команди:
```text

Hello World!
========================================
Input Command: comand
Entered command = "comand", parameters = []
----------------------------------------

Results:
No Command = "comand"
========================================
Input Command: echo test 'nasha laba' "Hello World"
Entered command = "echo", parameters = ['test', 'nasha laba', 'Hello World']
----------------------------------------

Results:
test
nasha laba
Hello World
```
