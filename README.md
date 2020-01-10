# aiologs
### 说明是aiologs
aiologs 是对日志记录的封装，目前支持储存文档，ElasticSearch，mongodb。
aiologs 采用的是异步的方式，所以你的python版本需要至少在3.5+以上
如果对资源的使用比较敏感，aiologs亦可使用多线程的方式，但python的线程机制，我们仍然不建议使用它。除非你认为是必须的。
注意：异步不代表记录日志的操作对性能没有损耗。大量的日志依然可能使io阻塞，当然这样的情况非常罕见。如果对性能要求较高的应用，可尝试其他的方式进行日志的记录或考虑是否必要写入大量日志。
经大量测试，aiologs在任何情况下，对异步应用的性能影响非常低。
### 如何安装
```
pip install aiologs
```
### 使用前需要进行初始化
全局变量，仅在全局注册一次，多个地方可以直接使用
```
from aiologs import LoggerConfig
LoggerConfig.addConfig({
        "ifFile": 0,
        "ifConsole": 0,
        "fileName": "",
        "path": './',
        "projectName": "test_project", 
        "asyncWrite": 1,
        "dbtype": 0,
        "targetDB":['192.168.88.103'],
        "env": "develop"
    })
    #projectName:项目名称，用于区分文件夹
    #isJsonSerialize：是否进行json序列化，默认是标签模式
    #ifConsole：是否进行print，如果开发环境，可以使用此参数方便调试
    #ifFile：是否记录日志文件
    #fileName：文件名称，默认是按照时间进行创建
    #path：文件保存路径
    #asyncWrite:是否直接写入数据库，一般情况下建议使用数据库保存，可以结合配套aiologs-ui查询用
    #dbtype：存入数据库类型，当asyncWrite=1时候有效，0：ElasticSearch，1：mongodb
    #targetDB：数据库库链接 []里面放链接字符串，示例使用ElasticSearch
    #env：日志的环境，如果多个环境使用同一套数据库，需从这里区分。建议生产环境的日志单独使用数据库
```
### 全局初始化结束，就可以在全局任何地方使用保存日志
应用日志
```
from aiologs import Logger
Logger().info(module="a",category="b",sub_category="c",msg={},extra={},filter1="",filter2="",serializeEncoder=None)
Logger().warning(module="a",category="b",sub_category="c",msg={},extra={},filter1="",filter2="",serializeEncoder=None)
Logger().error(module="a",category="b",sub_category="c",msg={},extra={},filter1="",filter2="",serializeEncoder=None)
Logger().critical(module="a",category="b",sub_category="c",msg={},extra={},filter1="",filter2="",serializeEncoder=None)
Logger().debug(module="a",category="b",sub_category="c",msg={},extra={},filter1="",filter2="",serializeEncoder=None)
#module:模块 用于区分日志的模块
#category:大分类 用于区分日志
#sub_category:小分类 用于区分日志
#msg:日志内容
#extra:扩展信息
#filter1: 过滤条件1
#filter2: 过滤条件2
#serializeEncoder:序列化方式（可以自定义序列话方式，否则使用系统默认的方式）
```
### 日志查看
执行完毕后，可在初始化传入的path下查找日志。如果保存数据库了。

1. ElasticSearch，查找aiologs*下的所有文档进行日志查询，ElasticSearch的restapi查询方法可自行搜索。或者推荐使用成套开发的webui进行展示。https://github.com/beincy/aiologs-ui
2.mongodb ，如果使用mongdb，数据库连接工具打开，查找数据库aiologs，集合查找项目名称_环境。因为生产环境下可能产生大量的日志。目前建议还是使用ElasticSearch

