pip install isort
isort . 
выравнивает весь проект


Для работы с celery дополнительно
pip install eventlet
для запуска celery:
celery -A config worker -l INFO -P eventlet

или:
Windows does not support celery 4.0+, So To Solve this issue :
We have to install gevent using pip :
pip install gevent

Then to run celery,
celery -A <proj_name> worker -l info -P gevent