# FarmCaptchaMailru

Зависимости

pip install Selenium
pip install requests

И веб драйвер для фаерфокса, он должен лежать рядом с исполняемым скриптом

За сутки собрал при помощи данного скрипта 100_000 капч с сайта маилру, собирал датасет для обучения нейронки

Не вижу смысла особо заморачиваться над архитектурой кода, скрипт одноразовый

не смог реализовать выбор даты рождения, из за странного выпадающего списка, приходится выставлять вручную рандомную дату

выбор всех элементов происходит за счет XPatca(код элемента-копировать-XPath)

Требуется вручную выставить index в 22 строке(0 если отсутствуют капчи или последняя)

В 68 строке ограничение на колличество капч

в 70 строке период очистки кеша браузера(можно изменять от 1000 до 10000 в зависимости от доступной оперативной памяти)

в 19 строке ограничение на размер массива ссылок для скачивание(оптимально от 50 до 200 в зависимости от скорости тынтырнета)