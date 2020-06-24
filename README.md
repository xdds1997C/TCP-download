# TCP-download
TCP协议设计一个文件下载服务协议，客户端发送要下载的文件路径给服务器，服务器将对应的文件内容送给客户端，客户端将文件存储到本地磁盘。<br>
1，运行服务端<br>
 ![](https://github.com/xdds1997C/TCP-download/blob/master/1.png)<br>
2，运行客户端<br>
 ![](https://github.com/xdds1997C/TCP-download/blob/master/2.png)<br>
发现返回结果是file download success<br>
3，查看download目录下的1.lock内容，对比原文件composer.lock<br>
1.lock内容如下：<br>
 ![](https://github.com/xdds1997C/TCP-download/blob/master/3.png)<br>
原文件内容如下：<br>
![](https://github.com/xdds1997C/TCP-download/blob/master/4.png)<br>	 
发现内容完全相同，文件下载成功。<br>
