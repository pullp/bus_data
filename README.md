1. 数据可用于用于哈工大18春软件构造实验二问题三 
2. output.csv是已经生成的数据
3. 如果想用别的数据可以去这个[网站](https://www.transitwiki.org/TransitWiki/index.php/Publicly-accessible_public_transportation_data)下载原始数据然后用程序处理, 具体流程可以参考我的[博客](https://www.jianshu.com/p/288a9b71a124)

4. 程序环境是win10, python3.6, 用了anaconda集成环境, 不过只要有pandas应该也能运行
5. 车次的到站时间为距离该线路的第一辆车(first trip of the route)发车时间对应的那天的00:00的秒数. 比如一辆车00:01:00发车, 00:10:00到a站, 而该条线路的第一辆车的发车时间为前一天的22:00:00, 那么这个车次到达a站对应的时间的值为87000(一天共86400秒)
6. 发现bug欢迎pr
