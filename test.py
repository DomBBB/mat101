"""
1P: DE: Welche der folgenden Expressions sind für die gegebenen Variablen 'lst' und 'tpl' gültig?
"""

lst = ['a', 1, var1]
tpl = (2,)

x = del(lst[0])
x = del(lst[3])
tpl[0] = lst[0]
lst.append(tpl[0])#THIS


"""
1P: DE: Mit welchen Werten für 'a' und 'b' wird die folgende Expression als True evaluiert?
"""

a = 'Something'
b = not None #THIS

a = not -2
b = 0

a = True
b = 0 #THIS

a = False
b = 0


bool(a or b)


"""
7P: DEUTSCH

Implementieren sie eine Funktion namens no_unlucky, die zwei Parameter annimmt: Eine Liste von ganzen Zahlen values, und eine ganze Zahl unlucky.

Die Funktion soll die Summe jener Werte in values berechnen, die nicht durch unlucky teilbar sind. Falls unlucky 0 ist, sollen alle Werte in values aufaddiert werden. Die Funktion soll die resultierende Summe zurückgeben.

Sie können davon ausgehen, dass die Funktion nur mit gültigen Parametern aufgerufen wird.
"""

def no_unlucky(values, unlucky):
    res = []
    if unlucky == 0:
        return sum(values)
    else:
        for value in values:
            if value%unlucky != 0:
                res.append(value)
        return sum(res)

assert(no_unlucky([10, 24, 1], 13) == 35)
assert(no_unlucky([13, 25], 13) == 25)
assert(no_unlucky([13, 26], 13) == 0)
assert(no_unlucky([13, 26], 0) == 39)



"""
7P: DEUTSCH

Implementieren sie eine Funktion namens shout, die einen String als parameter text annimmt. Die Funktion soll diesen String in Grossbuchstaben zurückgeben, und dabei ein oder mehrere Ausrufezeichen anhängen. Wenn text keine Ausrufezeichen enthält, soll ein Ausrufezeichen angehängt werden. Wenn text ein oder mehrere Ausrufezeichen enthält, soll dieselbe Anzahl Ausrufezeichen zusätzlich angehängt werden.

Sie können davon ausgehen, dass die Funktion nur mit gültigen Parametern aufgerufen wird.
"""

def shout(text):
    res = ""
    c = 0
    for char in text:
        res += char.upper()
        if char == "!":
            c += 1
    if c == 0:
        res += "!"
    else:
        res += "!" * c
    return res

assert(shout("Hello, God") == "HELLO, GOD!")
assert(shout("Hello, World!") == "HELLO, WORLD!!")
assert(shout("Hello!! World?") == "HELLO!! WORLD?!!")


"""
2P: DE: Welche der folgenden Codesnippets können benutzt werden um die Länge einer beliebigen Liste zu berechnen?
"""
def func(l):
   def inner(l, n):
       return n + 1 if not l else inner(l[1:], n + 1)
   return inner(l, 0)

def func(l):
   return 1 + func(l[1:]) if l else 0  #THIS

def func(l):
   x = 0
   for _ in l:
       x += 1
   return x   #THIS

def func(l):
   return 2 + len(l[2:])


func([1,2,3,4,5,6,7,8])



"""
2P: DE: Welche der folgenden Expressions generieren folgenden String: 'Josh bought a 1 gallon bottle of milk.'
"""

'Josh bought' + 'a' + '1' + 'gallon bottle of milk.'
f'{'Josh'} bought a {1} gallon bottle of {'milk'}.'
'%s bought a %d gallon %s of milk' % ('Josh', 1, 'bottle')#THIS
'Josh bought {} {} {} bottle of milk.'.format('a', 1, 'gallon')   #THIS


"""
18P:DEUTSCH

Implementieren Sie eine Funktion min_max_of, welche eine Liste von beliebigen Werten values, annimmt und ein Tupel zurückgibt, welches den maximalen und minimalen numerischen Wert enthält, sofern solche Werte in der Liste vorkommen. Falls keine entsprechenden numerischen Werte vorkommen, soll ein Tupel zurückgegeben werden, wo beide Werte None sind. Falls die minimalen und maximalen Werte identisch sind, soll nur der Minimalwert im Tupel vorkommen und das zweite Tupelelement soll None sein. Beachten Sie die Assertions als Beispiele für die Anwendung von min_max_of.
"""

def min_max_of(values):
    if not isinstance(values, list):
        return (None, None)
    res = []
    for value in values:
        if isinstance(value, (int, float, complex)) and not isinstance(value, bool):
            res.append(value)
    if len(res) == 0:
        return (None, None)
    else:
        minim = min(res)
        maxim = max(res)
        if minim == maxim:
            return (minim, None)
        else:
            return (minim, maxim)


assert(min_max_of(None) == (None, None))
assert(min_max_of([]) == (None, None))
assert(min_max_of([True]) == (None, None))
assert(min_max_of([0, 0.0]) == (0, None))
assert(min_max_of([0, 0.0]) == (0.0, None))
assert(min_max_of([-1, 0, 1]) == (-1, 1))
assert(min_max_of(['a', 'A', 1]) == (1, None))


"""
2P: DE: Welche der folgenden Aussagen treffen auf dieses Python script zu?
"""

lst = [[2]]

def func1(lst):
   lst = lst + [1, 2]
   print(lst)

def func2(lst):
   lst.append([1, 2])
   print(lst)

func1([])

lst
len(lst)

DE: Wenn man 'func2' mit '[]' aufruft, wird 'lst' (deklariert auf Zeile 1) am Ende des Scripts die Länge 1 haben. #THIS

DE: Wenn man 'func2' mit 'lst' (deklariert auf Zeile 1) aufruft, wird 'lst' (deklariert auf Zeile 1 am Ende des Scripts die Länge 2 haben. #THIS

DE: Wenn man 'func1' mit '[]' aufruft, wird 'lst' (deklariert auf Zeile 1) am Ende des Scripts die Länge 2 haben.

DE: Wenn man 'func1' mit 'lst' (deklariert auf Zeile 1) aufruft, wird 'lst' (deklariert auf Zeile 1 am Ende des Scripts die Länge 3 haben.




"""
2P:
DE: Welche der folgenden Aussage treffen auf dieses Pythonscript zu?
"""

str_freq = {}
def func(str_list):
    str_freq = {}
    for s in str_list:
        str_freq[s] = str_freq[s] + 1
    return str_freq

func(a, a)

DE: Ein Aufruf von 'func([a], a)' am Ende des Scripts würde eine Liste der Länge 3 zurückgeben.

DE: Das Script stürzt ab wenn man 'func(a, True) am Ende des Scripts ausführen würde. #TRUE

DE: Ein Aufruf von 'func((a), (a,))' am Ende des Scripts würde eine Liste der Länge 3 zurückgeben.

DE: Das Script stürzt ab wenn man 'func(a, a)' am Ende des Scripts ausführen würde. #TRUE



"""
"""
P18:  Implementieren Sie eine Funktion bill, welche folgende Parameter annimmt:

    per_hour: eine Gleitkommazahl die den Stundensatz eines Arbeiters angibt und
    parts_prices_hours: ein Dictionary in der Form {part: (price, hours)}, wo part der Name eines Bauteils ist, price den Preis des Bauteils repräsentiert, und hours die Anzahl Stunden als Gleitkommazahl repräsentiert, die benötigt werden, um das Bauteil zu installieren. price und hours können für gewisse Einträge in parts_prices_hours None sein.

Die Funktion soll ein Tupel mit zwei Elementen zurückgeben, wo das erste Element die totalen Kosten für den Kauf und die Installation aller Teile angibt, und das zweite Element ein boolean ist, welcher angibt, ob irgendwelche Informationen für die Berechnung fehlten. Die Kosten für die Installation eines einzelnen Teil soll wie folgt berechnet werden: part_price + (parts_hours * per_hour) und die totalen Kosten berechnen sich aus der Summe der Kosten für die Installation aller Teile. Wenn price eines Teils None, ist, soll ein Preis von 0 für dieses Teil angenommen werden, und wenn hours, für ein Teil None ist, soll eine Stunde angenommen werden. Beachten Sie die Assertions als Beispiele für die Anwendung von bill.
"""

def bill(per_hour, parts_prices_hours):
    res = []
    missing = False
    for part, value in parts_prices_hours.items():
        item_price = value[0]
        if item_price == None:
            item_price = 0
            missing = True
        item_hours = value[1]
        if item_hours == None:
            item_hours = 1
            missing = True
        cost = item_price + (item_hours * per_hour)
        res.append(cost)
    return (sum(res), missing)

assert(bill(0, {'Door': (23.33, 2.50)}) == (23.33, False))
assert(bill(0, {}) == (0, False))
assert(bill(0, {'Door': (None, 3.0)}) == (0, True))
assert(bill(50, {'Door': (None, 3.0)}) == (150, True))
assert(bill(50, {'Door': (10, None)}) == (60, True))
assert(bill(10.5, {'Door': (None, 3.0), 'Window': (22.22, 0.5)}) == (58.97, True))
assert(bill(10.5, {'Window': (22.22, 0.5)}) == (27.47, False))
