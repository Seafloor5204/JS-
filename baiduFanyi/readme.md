
### 1.打开浏览器工具 NetWork 可查看到Api链接以及参数

	https://fanyi.baidu.com/v2transapi?from=zh&to=en //post
	
### 参数

	from: zh
	to: en
	query:早上好
	transtype:translang ==》 手动点击翻译transtype:realtime ==》 自动翻译
	simple_means_flag:3
	sign: 643048.863449 //变     ==>window.gtk = '320305.131321201'(固定的?) 
	token: a2555c16f0476fcc3a544a0df9b0d96a //不变 查看， Network中点击All进行搜索， 如搜索不到，刷新浏览器  source:https://fanyi.baidu.com/
	domain: common

分析可得： gtk与token可从https://fani.baidu.com进行正则匹配得到
      sign： 而sign通过执行js可得

### 2. 由于网页存在Cookie, 使用Session 来进行请求
	
	```
	session = requests.session();

	session.get(url)
	response = session.get(url) 
	```
### 3. Python 中执行JS
	模块安装  pip install PyExecJs
	模块使用
		在py文件中引入模块， 使用open()读取JS文件到content
		使用execjs.compile(content).call("js函数名",[参数])；






