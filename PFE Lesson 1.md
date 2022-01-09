# Python-for-everybody
<ins>**Introduction**</ins>

- <ins>Why do we do programming</ins> <br />
  skip

- <ins>Computer's inside structure</ins> <br /><br />
  **Define** <br />
  - CPU: <br />
    CPU has surpassing processing power that operates the program and constantly ask users. <br />
  
  - Input Device: <br />
    Input device is device that gets input by people such as mouse and keyboard. <br />
  
  - Output Device: <br />
    Output device is device that shows outputed results such as screen and speaker. <br />
  
  - Main Memory: <br />
    Main Memory is volatile memory that is very fast and stores a small amount of information such as Ram. The memory disappears after the computer is shuted down. <br />
  
  - Auxiliary Memory: <br />
    Auxiliary Memory stores memory that doesn't get erased such as SSD and HDD. <br /><br />
  
  
  **Relation of each** <br />
  - In sequence, CPU ask -> people answer with programming -> saved in Auxiliary Memory -> computer change program in binary and understand -> computer answer <br /><br /><br />
    


- <ins>Python as an language</ins> <br /><br />
  **Syntax Error** <br />
  - As you do programming in python, you will encounter syntax error (grammer error in programming language) a lot. Programming language can only understand accurate content. <br /><br /><br />



- <ins>Reserved Word, Sequenctial, Conditional, and Repeated</ins> <br /><br />
  **Reserved Word and creating sentence** <br />
  - Reserved Word: <br />
    Reserved words are python's designated words that can't be used as the name of variable, function, and identifier. <br /><br>
    For example, <br>
    we can make variable like
    ``` python
    x = 2
    ``` 
    
    However, we can't make variable that starts with number or uppercase. Also we can't use python's designated names like
    
    ``` python
    2jk = 2
    X = 2
    function = 2
    ```
    <br />
    
  **How to program: interactive style and script style** <br />
    - Interactive: <br />
      Interactive is writing and executing the code one by one. <br />
      
    - Script: <br />
      Writing multiple codes and then executing at final. Script style is further efficient than interactive style if the code gets longer. <br />
    
    - We usually write codes as script and save them to Auxiliary Memory, then execute. <br /><br />


  **Controlling the flow of program** <br />
    1. Sequential <br />
      Sequential flow of code. <br /><br />
      For Example: 
        ```python
        n = 5
        while n > 0:
          print(n) # 5,4,3,2,1을 출력합니다.
          n = n - 1
        print('Blastoff!') # Blastoff를 출력합니다.
        ```
        <br />
      
    2. Conditional <br />
      The code activates when condition is true. We use if statement to do this. <br /><br />
      For Example: 
        ```python
        x = 5
        if x < 10: 
          print('Smaller') # Smaller가 출력됩니다.
        if x > 20: 
          print('Bigger')
        print('Finis') # Finis가 출력됩니다.
        ```
        <br />
      
    3. iteration <br />
      While the condition is true, repeatedly trigger the inner codes. <br /><br />
      For Example: <br />
        ```python
        n = 5
        while n > 0:
          print(n) # 5,4,3,2,1을 출력합니다.
          n = n - 1
        print('Blastoff!') # Blastoff를 출력합니다.
        ```
        
<br /><br /><br /><br />




<ins>**Variable, Expression, Code**</ins>
      
- <ins>Variable, Expression, Sentences</ins> <br /><br />
  **Constants** <br />
  - Constant doesn't change <br />
    ```python
    print(123) #123으로 출력, 123이 상수
    print(98.6) # 98.6으로 출력, 98.6이 상수
    print('Hello World') # Hello World로 출력, Hello World가 상수
    ```
  <br />
  
  **Reserved Words** <br />
  - Reserved Words are the special words that python has chose its function. For example, if python encounters reserved word "if", the conditional operates. <br /><br />

  **Variables** <br />
  - We can assign data with a comprehensible name into the memory as variable. <br />
    For Example: 
      ```python
      x = 12.2
      print(x) # 12.2가 출력됩니다.
      y = 14
      x = 100 
      print(x) # 100이 출력됩니다.
      ```
      - x, y: name of variable <br />
      - =: allocator that assigns specific value(s) to the relevant variable <br />
      - 12.2, 14: values we inputed in the variable <br /><br />

    After declaring as a variable, we can reassign the value in that variable.
   
  
    
