[06 - Function Attributes](https://github.com/fbaptiste/python-deepdive/blob/main/Part%204/Section%2002%20-%20Classes/06%20-%20Function%20Attributes.ipynb)

### Function Attributes

До сих пор мы имели дело с невызываемыми атрибутами. Когда атрибуты на самом деле являются функциями, все ведет себя по-другому.

```Python
class Person:
    def say_hello():
        print('Hello!')
```

```Python
Person.say_hello
```

```
<function __main__.Person.say_hello()>
```

```Python
type(Person.say_hello)
```

```
function
```

Как мы видим, это просто простая функция, которая вызывается как обычно:

```Python
Person.say_hello()
```

```
Hello!
```

Теперь давайте создадим экземпляр этого класса:

```Python
p = Person()
```

```Python
hex(id(p))
```

```
'0x7f88a06937b8'
```

Мы знаем, что можем получить доступ к атрибутам класса через экземпляр, поэтому мы также должны иметь возможность получить доступ к атрибуту функции таким же образом:

```Python
p.say_hello
```

```
<bound method Person.say_hello of <__main__.Person object at 0x7f88a06937b8>>
```

```Python
type(p.say_hello)
```

```
method
```

Хм, тип изменился с `function` на `method`, а представление функции гласит, что это **связанный метод** **конкретного объекта** `p`, который мы создали (обратите внимание на адрес памяти).

А если мы попытаемся вызвать функцию из экземпляра, вот что произойдет:


```Python
try:
    p.say_hello()
except Exception as ex:
    print(type(ex).__name__, ex)
```

```
TypeError say_hello() takes 0 positional arguments but 1 was given
```
TypeError say_hello() принимает 0 позиционных аргументов, но был задан 1

`method` является фактическим типом в Python, и, как и функции, они являются вызываемыми, но у них есть одна отличительная черта. Их необходимо привязать к объекту, и эта ссылка на объект передается базовой функции.

Часто, когда мы определяем функции в классе и вызываем их из экземпляра, нам нужно знать, какой **конкретный** экземпляр использовался для вызова функции. Это позволяет нам взаимодействовать с переменными экземпляра.

Для этого Python автоматически преобразует обычную функцию, определенную в классе, в метод, когда она вызывается из экземпляра класса.

Кроме того, он «привязывает» метод к экземпляру, то есть экземпляр будет передан как **первый** аргумент вызываемой функции.

Он делает это с помощью **дескрипторов**, к которым мы вернемся подробно позже.

А пока давайте просто рассмотрим это немного подробнее:

```Python
class Person:
    def say_hello(*args):
        print('say_hello args:', args)
```

```Python
Person.say_hello()
```

```
say_hello args: ()
```

Как мы видим, вызов `say_hello` из **класса** просто вызывает функцию (это просто функция).

Но когда мы вызываем ее из экземпляра:

```Python
p = Person()
hex(id(p))
```

```
'0x7f88d0428748'
```

```Python
p.say_hello()
```

```
say_hello args: (<__main__.Person object at 0x7f88d0428748>,)
```

Вы можете видеть, что объект `p` был передан как аргумент функции класса `say_hello`.

Очевидным преимуществом является то, что теперь мы можем легко взаимодействовать с атрибутами экземпляра:


```Python
class Person:
    def set_name(instance_obj, new_name):
        instance_obj.name = new_name  # or setattr(instance_obj, 'name', new_name)
```

```Python
p = Person()
```

```
p.set_name('Alex')
```

```Python
p.__dict__
```

```
{'name': 'Alex'}
```

По сути, это имеет тот же эффект, что и следующее:

```Python
Person.set_name(p, 'John')
```

```Python
p.__dict__
```

```
{'name': 'John'}
```

По сути, это имеет тот же эффект, что и следующее:
>по соглашению первый аргумент обычно называется `self`, но, как вы только что видели, мы можем назвать его как угодно — он просто будет в экземпляре, когда вызывается вариант метода функции — и он называется **методом экземпляра**.

Но **методы** — это объекты, создаваемые Python при вызове функций класса из экземпляра.

У них также есть свои собственные уникальные атрибуты:

```Python
class Person:
    def say_hello(self):
        print(f'{self} says hello')
```

```Python
p = Person()
```

```Python
p.say_hello
```

```
<bound method Person.say_hello of <__main__.Person object at 0x7f88d0428c18>>
```

```Python
m_hello = p.say_hello
```

```Python
type(m_hello)
```

```
method
```

Например, у него есть атрибут `__func__`:

```Python
m_hello.__func__
```

```
<function __main__.Person.say_hello(self)>
```

которая является функцией класса, используемой для создания метода (базовой функции).

Но помните, что метод привязан к экземпляру. В этом случае мы получили метод из объекта `p`:


```Python
hex(id(p))
```

```
'0x7f88d0428c18'
```

```Python
m_hello.__self__
```

```
<__main__.Person at 0x7f88d0428c18>
```

Как вы можете видеть, метод также имеет ссылку на объект, к которому он **привязан**.

Поэтому думайте о методах как о функциях, которые были привязаны к определенному объекту, и этот объект передается в качестве первого аргумента вызова функции. Остальные аргументы затем передаются после этого.

Методы экземпляра создаются автоматически для нас, когда мы определяем функции внутри определений наших классов.

Это справедливо даже если мы применяем обезьяний патч к нашим классам во время выполнения ([[06_1 - Monkey paching]]):

```Python
class Person:
    def say_hello(self):
        print(f'instance method called from {self}')
```

```Python
p = Person()
hex(id(p))
```

```
'0x7f88d0435f28'
```

```Python
p.say_hello()
```

```
instance method called from <__main__.Person object at 0x7f88d0435f28>
```

```Python
Person.do_work = lambda self: f"do_work called from {self}"
```

```Python
Person.__dict__
```

```
mappingproxy(
	{
		'__module__': '__main__',
        'say_hello': <function __main__.Person.say_hello(self)>,
        '__dict__': <attribute '__dict__' of 'Person' objects>,
        '__weakref__': <attribute '__weakref__' of 'Person' objects>,
        '__doc__': None,
        'do_work': <function __main__.<lambda>(self)>
    }
)
```

Хорошо, обе функции находятся в классе `__dict__`.

давайте создадим экземпляр и посмотрим, что произойдет:

```Python
p.say_hello
```

```
<bound method Person.say_hello of <__main__.Person object at 0x7f88d0435f28>>
```

```Python
p.do_work
```

```
<bound method <lambda> of <__main__.Person object at 0x7f88d0435f28>>
```

```Python
p.do_work()
```

```
'do_work called from <__main__.Person object at 0x7f88d0435f28>'
```

Но будьте осторожны, если мы добавим функцию к **экземпляру** напрямую, это будет работать не так — мы создадим функцию в экземпляре, поэтому она не будет считаться методом (так как она не была определена в классе):

```Python
p.other_func = lambda *args: print(f'other_func called with {args}')
```

```Python
p.other_func
```

```
<function __main__.<lambda>(*args)>
```

```Python
'other_func' in Person.__dict__
```

```
False
```

```Python
p.other_func()
```

```
other_func called with ()
```

Как видите, `other_func` является и ведет себя как обычная функция.

Короче говоря, функции, определенные в классе, преобразуются в методы при вызове из экземпляров класса. Поэтому, конечно, мы должны учитывать этот дополнительный аргумент, который передается методу.

---
