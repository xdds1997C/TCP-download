# TCP-download
TCP协议设计一个文件下载服务协议，客户端发送要下载的文件路径给服务器，服务器将对应的文件内容送给客户端，客户端将文件存储到本地磁盘。
1，运行服务端
 
2，运行客户端
 
发现返回结果是file download success
3，	查看download目录下的1.lock内容，对比原文件composer.lock
1.lock内容如下：
 
原文件内容如下：
	 
发现内容完全相同，文件下载成功。
