# Dokumentacja dla użytkownika końcowego: Język Pseudo

**Autorzy**: Maciej Jamroży, Robert Jacak, Kacper Gałek  
**Data**: Czerwiec 2025  

## Spis treści
- [Wstęp](#wstęp)
- [Instalacja i uruchomienie](#instalacja-i-uruchomienie)
- [Hello World](#hello-world)
- [Podstawowe cechy języka](#podstawowe-cechy-języka)
  - [Typy podstawowe](#typy-podstawowe)
  - [Deklaracja i przypisanie zmiennych](#deklaracja-i-przypisanie-zmiennych)
  - [Konwersje typów](#konwersje-typów)
  - [Zakresy i widoczność zmiennych (Scope)](#zakresy-i-widoczność-zmiennych-scope)
    - [Zakres globalny i lokalny](#zakres-globalny-i-lokalny)
    - [Shadowing – przesłanianie zmiennych](#shadowing--przesłanianie-zmiennych)
  - [Instrukcje sterujące](#instrukcje-sterujące)
    - [if](#if)
    - [Pętla while](#pętla-while)
    - [Pętla for](#pętla-for)
  - [Funkcje](#funkcje)
  - [Przykłady zaawansowane](#przykłady-zaawansowane)
    - [Rekurencja](#reakurencja)
    - [Tabliczka mnożenia](#tabliczka-mnożenia)
  - [Wyświetlanie błędów](#wyświetlanie-błędów)
- [Podsumowanie](#podsumowanie)

## Wstęp
Język `Pseudo` został zaprojektowany jako ogólny język programowania, szczególnie przydatny do prototypowania algorytmów. Łączy prostotę pseudokodu z elastyczną składnią i silnym typowaniem, dzięki czemu jest odpowiedni zarówno dla początkujących, jak i bardziej zaawansowanych programistów.

## Instalacja i uruchomienie
1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/MaciejJamrozy/projectPseudo.git
   ```
2. Zainstaluj zależności:
   ```bash
   pip install -r requirements.txt
   ```
3. Sprawdź, że w katalogu są pliki:
   - `Pseudo.g4`
   - `PseudoInterpreter.py`
   - `Stack.py`
   - `StackFrame.py`
   - `Functions.py`
   - `Variables.py`
   - `PseudoExceptions.py`
4. Uruchom interpreter:
   ```bash
   python3 PseudoInterpreter.py program.pseudo
   ```

## Hello World
Najprostszy program:
```pseudo
print("Hello, world!");
```
Wynik:
> Hello, world!

## Podstawowe cechy języka

### Typy podstawowe
Silnie i statycznie typowany język. Dostępne typy:
- `int` – liczby całkowite (np. `-42`, `0`, `123`)
- `float` – liczby zmiennoprzecinkowe (np. `3.14`, `-0.001`)
- `string` – ciągi znaków w pojedynczych lub podwójnych cudzysłowach
- `boolean` – wartości logiczne `True` i `False`

### Deklaracja i przypisanie zmiennych
Możesz używać różnych operatorów:
- `=` (standardowo): `int x = 5;`
- `is`: `float pi is 3.14;`
- `<<`: `string s << "foo";`
- `<-`: `boolean flag <- True;`

### Konwersje typów
Wbudowane rzutowania:
- `int(expr)` – np. `int("123") → 123`
- `float(expr)` – np. `float("3.14") → 3.14`
- `string(expr)` – np. `string(42) → "42"`
- `boolean(expr)` – traktuje 0/False jako `False`, inne jako `True`

### Zakresy i widoczność zmiennych (Scope)
Każdy program napisany w języku Pseudo działa w tzw. **zakresach** (ang. *scopes*), które definiują, gdzie dana zmienna jest widoczna i dostępna. Dzięki temu można tworzyć bezpieczne funkcje, które nie wpływają przypadkowo na zmienne z innych części programu.

#### Zakres globalny i lokalny
- **Globalny zakres** – każda zmienna zadeklarowana poza funkcją lub blokiem (np. pętlą) należy do zakresu globalnego i może być dostępna z każdego miejsca w programie.
- **Lokalny zakres** – każda zmienna zadeklarowana wewnątrz funkcji lub bloku (np. w pętli) istnieje tylko w tym i zagnieżdzonych zakresach, nie wpływając na zmienne o tej samej nazwie poza tym zakresem. Można się do niej odwołać z zagnieżdżonego bloku poprzez wyrażenie: `parent::`

#### Shadowing – przesłanianie zmiennych
Jeśli wewnątrz funkcji lub pętli utworzysz zmienną o tej samej nazwie, co istniejąca zmienna globalna lub zmienna z wyższego scope, lokalna wartość ją **przesłania**. Przykład:

```pseudo
global int x = 10;
function void test():
    int x = 6;
    {
    int x = 5;
    print(x); // wypisze 5 - lokalna zmienna
    print(parent::x) // wypisze 6 - wyższy scope
    print(parent::parent::x) // wypisze 10 - globalna
    }
end function;
test();
print(x); // wypisze 10 - globalna zmienna
```

### Instrukcje sterujące

#### if
```pseudo
if x > 0:
    print("Plus");
elseif x == 0 then
    print("Zero");
else:
    print("Minus");
end if;
```

#### Pętla while
```pseudo
while (i < 10):
    shout(i);
    i = i + 1;
end loop;
```

#### Pętla for
```pseudo
for (int i = 0; i < 5; i = i + 1):
    print(i);
end loop;
```

### Funkcje
Definicje funkcji można tworzyć z użyciem różnych aliasów: `function`, `fun` oraz `def`. Każdy z nich jest równoważny i może być użyty zamiennie.

```pseudo
function int max(int a, int b):
    if a > b:
        return a;
    else:
        return b;
    end if;
end function;
```
Wywołanie: `int m = max(10, 20);`

```pseudo
fun boolean even(boolean n):
    return n;
end fun;
```
Wywołanie: `boolean b = even(True);`

```pseudo
def string greet(string name):
    return name;
end def;
```
Wywołanie: `string msg = greet("Hello");`

**Uwaga:** Każda funkcja musi kończyć się słowem kluczowym `end function`, `end fun` lub `end def`, odpowiednio do użytego aliasu na początku. Zachowanie spójności aliasu na początku i końcu definicji jest obowiązkowe.

### Przykłady zaawansowane

#### Rekurencja
```pseudo
function int factorial(int n):
    if n <= 1: 
        return 1; 
    end if;
    return n * factorial(n - 1);
end function;
print(factorial(5)); // 120
```

#### Tabliczka mnożenia
```pseudo
for (int i = 1; i <= 10; i = i + 1):
    for (int j = 1; j <= 10; j = j + 1):
        print(i + " * " + j + " = " + (i * j));
    end loop;
end loop;
```

### Wyświetlanie błędów
Dodano bardziej czytelny i precyzyjny system raportowania błędów, który wskazuje dokładne miejsce wystąpienia problemu w kodzie. Komunikaty zawierają m.in. numer linii, kolumny oraz szczegółowy opis błędu, co znacznie ułatwia debugowanie.

Przykład błędu dla wielokrotnej deklaracji tego samego argumentu w definicji funkcji:

```pseudo
def void foo(int c, float c):
                          ^
Error in line: 1, column 26: argument 'c' was already declared at column 17, in this function definition.
```

**Zalety nowego systemu błędów:**
- Precyzyjne wskazanie linii i kolumny wystąpienia błędu.
- Opis błędu zawierający lokalizację poprzedniego konfliktu (np. wcześniejszej deklaracji).
- Lepsze zrozumienie błędów składniowych i semantycznych.

Dzięki temu programista może szybciej identyfikować i poprawiać błędy, zwłaszcza w bardziej złożonych definicjach funkcji czy struktur.

## Podsumowanie
`Pseudo` to elastyczny język edukacyjny, łączący prostotę pseudokodu z realnym wykonaniem. Oferuje rozbudowane instrukcje sterujące, silne typowanie i czytelną obsługę błędów.
