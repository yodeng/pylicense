# license for python2 codes

### 说明

+ 通过`AES`加密算法, 结合本地计算机硬件`(ip, mac, cpu, disk, hostname...)`以及其他自定义信息`(expiration date, pwd, workdir...)`等对`python`程序进行运行限定；
+ 加密信息根据实际需求写入[`license_info.DATA`](./license_info.py#12), 需根据加密信息调整`check_license.calibrator`的`check`规则；
+ 主程序非核心代码位置调用`check_license.check_license`进行`license`校验；
+ 依赖`pycrypto, netifaces`包，使用`pip2 install pycrypto netifaces`进行安装；
+ 若使用`python3`须做一些简单语法修改。

#### 注: 使用`Cython`接口`from Cython.Build import cythonize`进行模块扩展编译为`so`动态库文件, 加密代码


### 示例

```
$ python2 main.py  
license file path: /xx/xx/xx/license.lic, please copy this file to client.
license assess：True
```
