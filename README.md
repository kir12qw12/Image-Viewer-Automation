# Image Viewer Automation

Простой проект на Python с использованием Playwright и PIL/Tkinter.  
Проект демонстрирует базовую автоматизацию действий в браузере и работу с изображениями.

## Что делает
- Заходит на сайт с рандомными картинками (`https://picsum.photos/`)  
- Скачивает случайную картинку  
- Показывает её на полный экран на 5 секунд  

## Используемые библиотеки
- [Playwright](https://playwright.dev/python/) — автоматизация браузера  
- [Requests](https://pypi.org/project/requests/) — скачивание картинки  
- [Pillow](https://pillow.readthedocs.io/) — работа с изображениями  
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — полноэкранное отображение  

## Как запустить
Запустите main.exe
Для продвинутых пользователей:
1. Установить зависимости:

```bash
pip install playwright pillow requests
playwright install chromium

Запустите скрипт:
python main.py

