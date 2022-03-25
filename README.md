# 2022-MAI-Backend-M-Potenko


Homework 2:
------

Тестирование проводилось утилитой *ab (ab -n 1000 -c 20 -t 1 -v 2 http://127.0.0.1/)*, было сделано 1000 запросов для 20 клиентов. 
Скорость обработки составила 8064 запросов в секунду. Время ответа было от 1 до 21 ms со средним временем ответа в 2.481 ms.
Потерь пакетов не было.

```
Server Software:        nginx/1.18.0
Server Hostname:        127.0.0.1
Server Port:            80

Document Path:          /
Document Length:        14 bytes

Concurrency Level:      20
Time taken for tests:   1.000 seconds
Complete requests:      8064
Failed requests:        0
Total transferred:      1338624 bytes
HTML transferred:       112896 bytes
Requests per second:    8062.63 [#/sec] (mean)
Time per request:       2.481 [ms] (mean)
Time per request:       0.124 [ms] (mean, across all concurrent requests)
Transfer rate:          1307.03 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       4
Processing:     0    2   1.1      2      21
Waiting:        0    2   1.1      2      21
Total:          1    2   1.1      2      21

Percentage of the requests served within a certain time (ms)
  50%      2
  66%      3
  75%      3
  80%      3
  90%      3
  95%      4
  98%      5
  99%      7
 100%     21 (longest request)

```