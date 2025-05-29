# Dokumentacja Techniczna Języka Programowania Pseudo

## Wprowadzenie

Pseudo++ to niestandardowy język programowania stworzony z myślą o prostocie składni oraz solidnych podstawach, odpowiednich zarówno do celów edukacyjnych, jak i małych projektów. Język wspiera podstawowe konstrukcje programistyczne, takie jak deklaracje zmiennych, struktury sterujące (`if`, `while`, `for`) oraz definicje funkcji, kładąc szczególny nacisk na bezpieczeństwo typów i obsługę błędów.

Dokumentacja ta ma na celu zapewnienie pełnego przeglądu języka Pseudo, obejmującego jego cechy, składnię, semantykę, kluczowe komponenty, sposób użycia, obsługę błędów oraz praktyczne przykłady.

## Spis Treści

- [Instalacja](#instalacja)
- [Cechy Języka](#cechy-języka)
- [Składnia](#składnia)
- [Semantyka](#semantyka)
- [Kluczowe Komponenty](#kluczowe-komponenty)
- [Użycie](#użycie)
- [Obsługa Błędów](#obsługa-błędów)
- [Przykłady](#przykłady)

## Instalacja

Aby uruchomić interpreter Pseudo, należy zainstalować następujące zależności:

- **Python 3.x**: Język bazowy dla interpretera.
- **ANTLR4**: Biblioteka do parsowania składni (wymagana wersja `antlr4-python3-runtime`).

### Kroki instalacji:

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/yourusername/pseudo.git
   cd pseudo
   ```
2. Zainstaluj wymagane pakiety:
   ```bash
   pip install antlr4-python3-runtime
   ```
3. Upewnij się, że pliki `Pseudo.g4`, `PseudoInterpreter.py`, `Listener.py`, `Memory.py` oraz `PseudoExceptions.py` są dostępne w katalogu roboczym.

## Cechy Języka

Pseudo oferuje następujące funkcjonalności:

- **Bezpieczeństwo typów**: Zmienne muszą być deklarowane z określonym typem (`int`, `float`, `string`, `boolean`).
- **Struktury sterujące**: Obsługuje instrukcje `if`, `while` oraz `for`.
- **Funkcje**: Umożliwia definiowanie i wywoływanie niestandardowych funkcji.
- **Wejście/Wyjście**: Zawiera polecenia `print`/`shout` do wyświetlania danych oraz `input`/`scan`/`listen` do pobierania danych od użytkownika.
- **Obsługa błędów**: Dedykowane wyjątki dla niezgodności typów, niezadeklarowanych zmiennych i niewłaściwego użycia operatorów.

## Składnia

Składnia Pseudo jest zdefiniowana w pliku gramatyki `Pseudo.g4` przy użyciu ANTLR4. Poniżej przedstawiono kluczowe reguły składniowe.

### Struktura programu

- **`program`**: Sekwencja instrukcji zakończona znacznikiem końca pliku (EOF).

### Instrukcje (`statement`)

- **Deklaracja zmiennej**: `typ ID = expr ;`
- **Przypisanie**: `ID = expr ;`
- **Wyświetlanie**: `print(expr) ;` lub `shout(expr) ;`
- **Warunek**: `if (expr) : statement* end if ;`
- **Pętla while**: `while (expr) : statement* end loop ;`
- **Pętla for**: `for (typ ID = expr ; expr ; ID = expr) : statement* end loop ;`
- **Definicja funkcji**: (szczegóły w sekcji poniżej)

### Wyrażenia (`expr`)

- **Literały**: Liczby (`NUMBER`), ciągi znaków (`STRING`), wartości logiczne (`BOOL`).
- **Operatory arytmetyczne**: `+`, `-`, `*`, `/`.
- **Operatory porównania**: `>`, `<`, `>=`, `<=`, `==`, `!=`.
- **Operatory logiczne**: `&&`, `||`, `!`.

### Przykłady składni

1. Deklaracja i wyświetlenie:
   ```pseudo
   int x = 5;
   print(x);
   ```
2. Warunek:
   ```pseudo
   string msg = "Hello";
   if (x > 0) : print(msg); end if;
   ```
3. Pętla for:
   ```pseudo
   for (int i = 0; i < 5; i = i + 1) : print(i); end loop;
   ```

## Semantyka

### Ewaluacja wyrażeń

Interpreter Pseudo (`PseudoInterpreter.py`) używa wzorca wizytatora do przetwarzania drzewa parsowania. Wyrażenia są oceniane zgodnie z typami operandów:

- **Arytmetyka**: Operacje są dozwolone tylko między zgodnymi typami (np. `int + int`, `float + float`).
- **Porównania**: Zwracają wartości logiczne (`boolean`).
- **Logika**: Operatory `&&`, `||`, `!` działają na wartościach `boolean`.

### Struktury sterujące

- **If**: Wykonuje blok kodu, jeśli warunek jest prawdziwy.
- **While**: Powtarza blok kodu, dopóki warunek jest prawdziwy.
- **For**: Inicjalizuje zmienną, sprawdza warunek i aktualizuje zmienną w każdej iteracji.

### System typów

- Typy są statycznie sprawdzane podczas deklaracji i przypisania.
- Niedozwolone są operacje między niezgodnymi typami (np. `int + string` powoduje wyjątek).

## Kluczowe Komponenty

### 1. Lexer i Parser (`Pseudo.g4`)

- Definiuje tokeny (np. `ID`, `NUMBER`, `STRING`, `BOOL`) i reguły gramatyczne.
- Generuje drzewo parsowania na podstawie kodu źródłowego.

### 2. Interpreter (`PseudoInterpreter.py`)

- Implementuje wzorzec wizytatora do ewaluacji drzewa parsowania.
- Obsługuje zarządzanie zmiennymi, ewaluację wyrażeń i struktury sterujące.
- Wprowadza przeciążanie operatorów w zależności od typów operandów.

### 3. Listener (`Listener.py`)

- Nasłuchuje zdarzeń drzewa parsowania, zarządzając deklaracjami i inicjalizacjami zmiennych.
- Wymusza ograniczenia typów podczas deklaracji.

### 4. Pamięć (`Memory.py`)

- Przechowuje zmienne w słowniku, śledząc ich wartości i typy.

### 5. Wyjątki (`PseudoExceptions.py`)

- Definiuje niestandardowe wyjątki dla błędów runtime, takie jak:
  - `throw_var_redeclaration_exception`
  - `throw_wrong_type_exception`
  - `throw_undefined_name_exception`
  - `throw_unknown_operator_exception`

## Użycie

1. Napisz kod w pliku (np. `program.pseudo`).
2. Uruchom interpreter:
   ```bash
   python PseudoInterpreter.py
   ```
3. Interpreter odczyta plik, wykona kod i wyświetli wyniki lub komunikaty o błędach.

## Obsługa Błędów

Pseudo implementuje solidny system obsługi błędów:

- **Ponowna deklaracja zmiennej**: Wywołuje `throw_var_redeclaration_exception`, jeśli zmienna jest zadeklarowana więcej niż raz.
- **Niezgodność typów**: Wywołuje `throw_wrong_type_exception`, jeśli operacja lub przypisanie narusza reguły typów.
- **Niezdefiniowana nazwa**: Wywołuje `throw_undefined_name_exception`, jeśli użyto niezadeklarowanej zmiennej.
- **Nieznany operator**: Wywołuje `throw_unknown_operator_exception`, jeśli operator nie jest zgodny z typami operandów.

## Przykłady

### Przykład 1: Deklaracja zmiennej

```pseudo
int count = 10;
print(count);
```

**Wynik**: `10`

### Przykład 2: Instrukcja if

```pseudo
int x = 5;
if (x > 0) : print("Positive"); end if;
```

**Wynik**: `Positive`

### Przykład 3: Pętla for

```pseudo
for (int i = 0; i < 5; i = i + 1) : print(i); end loop;
```

**Wynik**:

```
0
1
2
3
4
```
