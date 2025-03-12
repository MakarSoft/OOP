[13 - Class and Static Methods](https://github.com/fbaptiste/python-deepdive/blob/main/Part%204/Section%2002%20-%20Classes/13%20-%20Class%20and%20Static%20Methods.ipynb)

### Class and Static Methods

Как мы видели, когда мы определяем функцию внутри класса, ее поведение (как функции или метода) зависит от того, как осуществляется доступ к функции: из класса или из экземпляра. (Мы рассмотрим, как это работает, когда рассмотрим дескрипторы позже в этом курсе).

```Python
class Person:
    def hello(arg='default'):
        print(f'Hello, with arg={arg}')

If we call `hello` from the class:
```

```Python
Person.hello()
```

```
Hello, with arg=default
```
Вы заметите, что `hello` был вызван без каких-либо аргументов, на самом деле, `hello` — это обычная функция:

```Python
Person.hello
```

```
<function __main__.Person.hello(arg='default')>
```

Но если мы вызываем `hello` из экземпляра, все по-другому:

```Python
p = Person()
```

```Python
p.hello
```

```
<bound method Person.hello of <__main__.Person object at 0x7f8f287fb860>>
```

```Python
p.hello()
```

```
Hello, with arg=<__main__.Person object at 0x7f8f287fb860>
```

```Python
hex(id(p))
```

```
'0x7f8f287fb860'
```

И как вы можете видеть, экземпляр `p` был передан в качестве аргумента `hello`.

Однако иногда мы определяем функции в классе, которые не взаимодействуют с самим экземпляром, но могут нуждаться в чем-то из класса. В таких случаях мы хотим, чтобы класс был передан функции в качестве аргумента, независимо от того, вызывается ли она из класса или из экземпляра класса.

Это называется **методами класса**. Вы заметите, что поведение должно быть разным — мы не хотим, чтобы экземпляр передавался функции при вызове из экземпляра, мы хотим, чтобы **класс** был передан ей. Кроме того, при вызове из класса мы **также** хотим, чтобы класс был передан ей (это похоже на методы `static` в Java, не путать со статическими методами в Python, как мы увидим немного позже).

Мы используем декоратор `@classmethod` для определения методов класса, и первым аргументом этих методов всегда будет класс, в котором определен метод.

Давайте сначала рассмотрим простой пример:

```Python
class MyClass:
    def hello():
        # this IS an instance method,
        # we just forgot to add a parameter
        # to capture the instance when this is called
        # from an instance - so this will fail
		# это метод экземпляра, мы просто забыли
		# добавить параметр для захвата экземпляра
		# когда это вызывается из экземпляра - так что
		# это не сработает        
        print('hello...')
        
    def instance_hello(arg):
        print(f'hello from {arg}')
        
    @classmethod
    def class_hello(arg):
        print(f'hello from {arg}')
      
```  

```Python
m = MyClass()
```

```Python
MyClass.hello()
```

```
hello...
```

Но, как и ожидалось, это не сработает:

```Python
try:
    m.hello()
except TypeError as ex:
    print(ex)
```

```
hello() takes 0 positional arguments but 1 was given
```

С другой стороны, обратите внимание на метод экземпляра, вызываемый из экземпляра и класса:

```Python
m.instance_hello()
```

```
hello from <__main__.MyClass object at 0x7f8ed87fff60>
```

```Python
try:
    MyClass.instance_hello()
except TypeError as ex:
    print(ex)
```

```
instance_hello() missing 1 required positional argument: 'arg'
```

Как вы видите, метод экземпляра должен быть вызван из экземпляра. Если мы вызываем его из класса, то аргумент не передается функции, поэтому мы получаем исключение.

Это не относится к методам класса — независимо от того, вызываем ли мы метод из класса или экземпляра, этот первый аргумент всегда будет предоставлен Python и будет объектом класса (а не экземпляром).

Обратите внимание, как различаются привязки:

```Python
MyClass.class_hello
```

```
<bound method MyClass.class_hello of <class '__main__.MyClass'>>
```

```Python
m.class_hello
```

```
<bound method MyClass.class_hello of <class '__main__.MyClass'>>
```

Как вы можете видеть в обоих случаях, `class_hello` привязан к классу.

Но с методом экземпляра привязки ведут себя по-разному:

```Python
MyClass.instance_hello
```

```
<function __main__.MyClass.instance_hello(arg)>
```

```Python
m.instance_hello
```

```
<bound method MyClass.instance_hello of <__main__.MyClass object at 0x7f8ed87fff60>>
```

Итак, всякий раз, когда мы вызываем `class_hello`, метод привязывается к **классу**, а первым аргументом является класс:

```Python
MyClass.class_hello()
```

```
hello from <class '__main__.MyClass'>
```

```Python
m.class_hello()
```

```
hello from <class '__main__.MyClass'>
```

Хотя в этом примере я использовал `arg` в качестве имени параметра в наших методах, обычное **соглашение** заключается в использовании `self` и `cls` — так все поймут, о чем мы говорим!

Иногда мы также хотим определить функции в классе и всегда делать их именно функциями, никогда не привязанными ни к классу, ни к экземпляру, как бы мы их ни называли. Часто мы делаем это, потому что нам нужно использовать функцию, специфичную для нашего класса, и мы хотим сохранить наш класс самодостаточным, или, может быть, мы пишем библиотеку функций (хотя модули и пакеты могут быть более подходящими для этого).

Они называются **статическими** методами. (Поэтому будьте осторожны, статические методы Python и статические методы Java имеют разное значение!)

Мы можем определить статические методы с помощью декоратора `@staticmethod`:

```Python
class MyClass:
    def instance_hello(self):
        print(f'Instance method bound to {self}')
        
    @classmethod
    def class_hello(cls):
        print(f'Class method bound to {cls}')
        
    @staticmethod
    def static_hello():
        print('Static method not bound to anything')
```

```Python
m = MyClass()
```

```Python
m.instance_hello()
```

```
Instance method bound to <__main__.MyClass object at 0x7f8ed8811a58>
```

```Python
MyClass.class_hello()
```

```
Class method bound to <class '__main__.MyClass'>
```

```Python
m.class_hello()
```

```
Class method bound to <class '__main__.MyClass'>
```

А статический метод может быть вызван как из класса, так и из экземпляра, но никогда не привязан:

```Python
MyClass.static_hello
```

```
<function __main__.MyClass.static_hello()>
```

```Python
m.static_hello
```

```
<function __main__.MyClass.static_hello()>
```

```Python
MyClass.static_hello()
```

```
Static method not bound to anything
```

```Python
m.static_hello()
```

```
Static method not bound to anything
```

#### Example

Давайте рассмотрим более конкретный пример использования этих различных типов методов.

Мы собираемся создать класс `Timer`, который позволит нам получать текущее время (как в формате UTC, так и в каком-либо часовом поясе), а также записывать время начала/остановки.

Мы хотим иметь один и тот же часовой пояс для всех экземпляров нашего класса `Timer` с простым способом изменения часового пояса для всех экземпляров при необходимости.

Если вам нужно работать с часовыми поясами, я рекомендую вам использовать стороннюю библиотеку `pyrz`. Здесь я просто буду использовать стандартную библиотеку, которая определенно не так проста в использовании, как `pytz`.

In [29]:

```Python
from datetime import datetime, timezone, timedelta

class Timer:
    tz = timezone.utc   # class variable to store
					    # the timezone - default to UTC
    
    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)
```

Итак, `tz` — это атрибут класса, и мы можем установить его с помощью метода класса `set_timezone` — все экземпляры будут использовать одно и то же значение `tz` (если только мы не переопределим его на уровне экземпляра).

```Python
Timer.set_tz(-7, 'MST')
```

```Python
Timer.tz
```

```
datetime.timezone(datetime.timedelta(-1, 61200), 'MST')
```

```Python
t1 = Timer()
t2 = Timer()
```

```Python
t1.tz, t2.tz
```

```
(datetime.timezone(datetime.timedelta(-1, 61200), 'MST'),
 datetime.timezone(datetime.timedelta(-1, 61200), 'MST'))
```

```Python
Timer.set_tz(-8, 'PST')
```

```Python
t1.tz, t2.tz
```

```
(datetime.timezone(datetime.timedelta(-1, 57600), 'PST'),
 datetime.timezone(datetime.timedelta(-1, 57600), 'PST'))
```

Далее мы хотим функцию, которая вернет текущее время UTC. Очевидно, что это не имеет никакого отношения ни к классу, ни к экземпляру, поэтому это главный кандидат на статический метод:

```Python
class Timer:
    tz = timezone.utc   # class variable to store
						# the timezone - default to UTC
    
    @staticmethod
    def current_dt_utc():
        return datetime.now(timezone.utc)
    
    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)
```

```Python
Timer.current_dt_utc()
```

```
datetime.datetime(2019, 6, 2, 23, 25, 59, 714761, tzinfo=datetime.timezone.utc)
```

```Python
t = Timer()
```

```Python
t.current_dt_utc()
```

```
datetime.datetime(2019, 6, 2, 23, 25, 59, 723565, tzinfo=datetime.timezone.utc)
```

Далее нам нужен метод, который будет возвращать текущее время на основе установленного часового пояса. Очевидно, что часовой пояс — это переменная класса, поэтому нам нужно будет получить к ней доступ, но нам не нужны никакие данные экземпляра, поэтому это главный кандидат на метод класса:

```Python
class Timer:
    tz = timezone.utc  # class variable to store the timezone - default to UTC
    
    @staticmethod
    def current_dt_utc():
        return datetime.now(timezone.utc)
    
    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)
        
    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)
```

```Python
Timer.current_dt_utc(), Timer.current_dt()
```

```
(datetime.datetime(2019, 6, 2, 23, 25, 59, 733420, tzinfo=datetime.timezone.utc),
 datetime.datetime(2019, 6, 2, 23, 25, 59, 733423, tzinfo=datetime.timezone.utc))
```

```Python
t1 = Timer()
t2 = Timer()
```

```Python
t1.current_dt_utc(), t1.current_dt()
```

```
(datetime.datetime(2019, 6, 2, 23, 25, 59, 741248, tzinfo=datetime.timezone.utc),
 datetime.datetime(2019, 6, 2, 23, 25, 59, 741251, tzinfo=datetime.timezone.utc))
```

```Python
t2.current_dt()
```

```
datetime.datetime(2019, 6, 2, 23, 25, 59, 745699, tzinfo=datetime.timezone.utc)
```

А если мы изменим часовой пояс (мы можем сделать это как через класс, так и через экземпляр, без разницы, так как метод `set_tz` всегда привязан к классу):

```Python
t2.set_tz(-7, 'MST')
```

```Python
Timer.__dict__
```

```
mappingproxy(
	{
		'__module__': '__main__',
        'tz': datetime.timezone(
	        datetime.timedelta(-1, 61200), 'MST'
	    ),
        'current_dt_utc': <staticmethod at 0x7f8ed8836d30>,
        'set_tz': <classmethod at 0x7f8ed8836d68>,
        'current_dt': <classmethod at 0x7f8ed8836da0>,
        '__dict__': <attribute '__dict__' of 'Timer' objects>,
	    '__weakref__': <attribute '__weakref__' of 'Timer' objects>,
        '__doc__': None
    }
)
```

```Python
Timer.current_dt_utc(), Timer.current_dt(), t1.current_dt(), t2.current_dt()
```

```
(
	datetime.datetime(
		2019, 6, 2, 23, 25, 59, 761523,
		tzinfo=datetime.timezone.utc
	),
	datetime.datetime(
		2019, 6, 2, 16, 25, 59, 761526,
		tzinfo=datetime.timezone(
			datetime.timedelta(-1, 61200), 'MST'
		)
	),
	datetime.datetime(
		2019, 6, 2, 16, 25, 59, 761526,
		tzinfo=datetime.timezone(
			datetime.timedelta(-1, 61200), 'MST'
		)
	),
	datetime.datetime(
		2019, 6, 2, 16, 25, 59, 761527,
		tzinfo=datetime.timezone(
			datetime.timedelta(-1, 61200), 'MST'
		)
	)
)
```

До сих пор нам не нужны были экземпляры для работы с этим классом!

Теперь мы добавим функционал для запуска/остановки таймера. Очевидно, мы хотим, чтобы это было основано на экземплярах, поскольку мы хотим иметь возможность создавать несколько таймеров.

```Python
class TimerError(Exception):
    """A custom exception used for Timer class"""
    # (since """...""" is a statement, we don't need to pass)
    
class Timer:
    tz = timezone.utc  # class variable to store the timezone - default to UTC
    
    def __init__(self):
        # use these instance variables to keep track of start/end times
        self._time_start = None
        self._time_end = None
        
    @staticmethod
    def current_dt_utc():
        """Returns non-naive current UTC"""
        return datetime.now(timezone.utc)
    
    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)
        
    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)
    
    def start(self):
        # internally we always non-naive UTC
        self._time_start = self.current_dt_utc()
        self._time_end = None
        
    def stop(self):
        if self._time_start is None:
            # cannot stop if timer was not started!
            raise TimerError('Timer must be started before it can be stopped.')
        self._time_end = self.current_dt_utc()
        
    @property
    def start_time(self):
        if self._time_start is None:
            raise TimerError('Timer has not been started.')
        # since tz is a class variable, we can just as easily access it from self
        return self._time_start.astimezone(self.tz)  
        
    @property
    def end_time(self):
        if self._time_end is None:
            raise TimerError('Timer has not been stopped.')
        return self._time_end.astimezone(self.tz)
    
    @property
    def elapsed(self):
        if self._time_start is None:
            raise TimerError('Timer must be started before an elapsed time is available')
            
        if self._time_end is None:
            # timer has not ben stopped, calculate elapsed between start and now
            elapsed_time = self.current_dt_utc() - self._time_start
        else:
            # timer has been stopped, calculate elapsed between start and end
            elapsed_time = self._time_end - self._time_start
            
        return elapsed_time.total_seconds()
```

```Python
from time import sleep

t1 = Timer()
t1.start()
sleep(2)
t1.stop()
print(f'Start time: {t1.start_time}')
print(f'End time: {t1.end_time}')
print(f'Elapsed: {t1.elapsed} seconds')
```

```
Start time: 2019-06-02 23:25:59.777250+00:00
End time: 2019-06-02 23:26:01.781431+00:00
Elapsed: 2.004181 seconds
```

```Python
t2 = Timer()
t2.start()
sleep(3)
t2.stop()
print(f'Start time: {t2.start_time}')
print(f'End time: {t2.end_time}')
print(f'Elapsed: {t2.elapsed} seconds')
```

```
Start time: 2019-06-02 23:26:01.787596+00:00
End time: 2019-06-02 23:26:04.792814+00:00
Elapsed: 3.005218 seconds
```
Итак, наш таймер работает. Кроме того, мы хотим использовать `MST` во всем нашем приложении, поэтому мы установим его, и поскольку это атрибут уровня класса, нам нужно изменить его только один раз:

```Python
Timer.set_tz(-7, 'MST')
```

```Python
print(f'Start time: {t1.start_time}')
print(f'End time: {t1.end_time}')
print(f'Elapsed: {t1.elapsed} seconds')
```

```
Start time: 2019-06-02 16:25:59.777250-07:00
End time: 2019-06-02 16:26:01.781431-07:00
Elapsed: 2.004181 seconds
```

```Python
print(f'Start time: {t2.start_time}')
print(f'End time: {t2.end_time}')
print(f'Elapsed: {t2.elapsed} seconds')
```

```
Start time: 2019-06-02 16:26:01.787596-07:00
End time: 2019-06-02 16:26:04.792814-07:00
Elapsed: 3.005218 seconds
```

---
