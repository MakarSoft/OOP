[11 - Read-Only and Computed Properties](https://github.com/fbaptiste/python-deepdive/blob/main/Part%204/Section%2002%20-%20Classes/11%20-%20Read-Only%20and%20Computed%20Properties.ipynb)

### Read-Only and Computed Properties

Хотя свойства только для записи не так распространены, свойства только для чтения (т. е. те, которые определяют геттер, но не сеттер) довольно распространены для ряда вещей.

Конечно, мы можем создавать свойства только для чтения, но поскольку ничто не является закрытым, в лучшем случае мы «предлагаем» пользователям нашего класса, что они должны рассматривать свойство как свойство только для чтения. Конечно, всегда есть способ обойти это.

Но все же хорошо иметь возможность хотя бы явно указать пользователю, что свойство предназначено только для чтения.

Вариант использования, на котором я собираюсь сосредоточиться в этом видео, — это вычисляемые свойства. Это свойства, которые на самом деле могут не иметь резервной переменной, но вместо этого вычисляются на лету.

Рассмотрим этот простой пример класса `Circle`, где мы можем читать/записывать радиус круга, но хотим вычисляемое свойство для площади. Нам не нужно хранить значение площади, мы всегда можем рассчитать его, зная текущее значение радиуса.

```Python
from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    @property
    def area(self):
        print('calculating area...')
        return pi * (self.radius ** 2)
```


```Python
c = Circle(1)
c.area
```

```
calculating area...
```

```
3.141592653589793
```

Конечно, мы могли бы просто использовать метод класса `area()`, но площадь — это скорее свойство круга, поэтому имеет больше смысла просто извлечь его как свойство, без дополнительного `()` для вызова.

Преимущество того, как мы это сделали, заключается в том, что если радиус круга когда-либо изменится, свойство площади немедленно это отразит.

```Python
c.radius = 2
c.area
```

```
calculating area...
```

```
12.566370614359172
```

С другой стороны, это также является недостатком — каждый раз, когда нам нужна площадь круга, она пересчитывается, даже если радиус не изменился!

```Python
c.area
c.area
```

```
calculating area...
calculating area...
```

```
12.566370614359172
```

Теперь мы можем использовать свойства, чтобы исправить эту проблему, не нарушая наш интерфейс!

Мы собираемся кэшировать значение площади и пересчитывать его только в случае изменения радиуса.

Чтобы узнать, изменился ли радиус, мы сделаем его свойством, а сеттер будет отслеживать, установлен ли радиус, и в этом случае он аннулирует кэшированное значение площади.

```Python
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        # if radius value is set
        # we invalidate our cached _area value
        # we could make this more intelligent and
        # see if the radius has actually changed
        # but keeping it simple
        self._area = None
        # we could even add validation here,
        # like value has to be numeric, non-negative, etc
        self._radius = value
        
    @property
    def area(self):
        if self._area is None:
            # value not cached - calculate it
            print('Calculating area...')
            self._area = pi * (self.radius ** 2)
        return self._area
```


```Python
c = Circle(1)
```

```Python
c.area
```

```
Calculating area...
```

```
3.141592653589793
```


```Python
c.area
```

```
3.141592653589793
```


```Python
c.radius = 2
```

```Python
c.area
```

```
Calculating area...
```

```
12.566370614359172
```


```Python
c.area
```

```
12.566370614359172
```

Существует множество других применений для вычисляемых свойств.

Некоторые свойства могут даже выполнять много работы, например, извлекать данные из базы данных, выполнять вызов внешнего API и т. д.

### Example

Давайте напишем класс, который принимает URL-адрес, загружает веб-страницу для этого URL-адреса и предоставляет нам некоторые метрики по этому URL-адресу — например, сколько времени заняла загрузка, размер (в байтах) страницы.

Хотя я собираюсь использовать для этого модуль `urllib`, я настоятельно рекомендую вам использовать вместо него стороннюю библиотеку `requests`:
[http://docs.python-requests.org](http://docs.python-requests.org/)


```Python
import urllib
from time import perf_counter


class WebPage:
    def __init__(self, url):
        self.url = url
        self._page = None
        self._load_time_secs = None
        self._page_size = None
        
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, value):
        self._url = value
        self._page = None
        # we'll lazy load the page - i.e.
        # we wait until some property is requested
		# мы будем лениво загружать страницу - т.е.
		# мы ждем, пока не будет запрошено какое-то свойство  
        
    @property
    def page(self):
        if self._page is None:
            self.download_page()
        return self._page
    
    @property
    def page_size(self):
        if self._page is None:
            # need to first download the page
            self.download_page()
        return self._page_size
        
    @property
    def time_elapsed(self):
        if self._page is None:
            self.download_page()
        return self._load_time_secs
            
    def download_page(self):
        self._page_size = None
        self._load_time_secs = None
        start_time = perf_counter()
        with urllib.request.urlopen(self.url) as f:
            self._page = f.read()
        end_time = perf_counter()
        
        self._page_size = len(self._page)
        self._load_time_secs = end_time - start_time
```

```Python
urls = [
    'https://www.google.com',
    'https://www.python.org',
    'https://www.yahoo.com'
]

for url in urls:
    page = WebPage(url)
    print(f'{url} \tsize={format(page.page_size, "_")} \telapsed={page.time_elapsed:.2f} secs')
```

```
https://www.google.com 	size=11_489 	elapsed=0.20 secs
https://www.python.org 	size=49_132 	elapsed=0.18 secs
https://www.yahoo.com 	size=524_548 	elapsed=0.77 secs
```


---
