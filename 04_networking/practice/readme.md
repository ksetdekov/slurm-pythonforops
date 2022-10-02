# Проект по сетям
## Инфо по запуску

Если ругается при запуске контейнера на недоступность портов на Windows:
```bash
net stop winnat
net start winnat
```

Полная инструкция по окружению [инструкция](https://edu.slurm.io/courses/python-for-ops-4-resident/units/1675/lessons/6286/steps/21104)

Вот ссылка на [adminer](http://localhost:8080/?pgsql=postgres&username=postgres&db=postgres&ns=usage_stats&select=resources&columns%5B0%5D%5Bfun%5D=&columns%5B0%5D%5Bcol%5D=&where%5B0%5D%5Bcol%5D=&where%5B0%5D%5Bop%5D=%3D&where%5B0%5D%5Bval%5D=&order%5B0%5D=&limit=50&text_length=100)

docker-compose up
docker-compose down