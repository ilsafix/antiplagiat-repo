# Антиплагиат
Утилита для антиплагиата, которая сравнивает два текста программ на Python и выдает оценку их похожести.
Задача решается с использованием расстояния Левенштейна.

Пример запуска:
```
python3 compare.py input.txt scores.txt
```

Пример входного файла input.txt:
```
files/main.py plagiat1/main.py
files/lossy.py plagiat2/lossy.py
files/lossy.py files/lossy.py
```

Пример выходного файла scores.txt:
```
0.948
0.313
1.000
```