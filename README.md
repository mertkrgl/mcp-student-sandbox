# mystery_module

İkinci derece (quadratic) denklem çözücü modül.

## Fonksiyon: `fn_x(a, b, c)`

`ax² + bx + c = 0` denkleminin köklerini ikinci derece denklem formülü ile hesaplar.

**Formül:**
```
x = (-b ± √(b² - 4ac)) / 2a
```

### Parametreler

| Parametre | Tip   | Açıklama                        |
|-----------|-------|---------------------------------|
| `a`       | float | x² katsayısı (0 olamaz)        |
| `b`       | float | x katsayısı                     |
| `c`       | float | sabit terim                     |

### Dönüş Değeri

- `(x1, x2)` — iki gerçel kök bulunursa tuple döner
- `None` — diskriminant (`b² - 4ac`) negatifse gerçel kök yoktur

### Örnek Kullanım

```python
from mystery_module import fn_x

# x² - 5x + 6 = 0  →  kökleri: 3 ve 2
result = fn_x(1, -5, 6)
print(result)  # (3.0, 2.0)

# x² + 1 = 0  →  gerçel kök yok
result = fn_x(1, 0, 1)
print(result)  # None
```
