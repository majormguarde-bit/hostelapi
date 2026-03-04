@echo off
echo Обновление приложения...
git pull
echo Обновление зависимостей...
.venv\Scripts\pip install -r requirements.txt
echo Обновление завершено.
pause