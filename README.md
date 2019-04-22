基于Flask的简易mock平台

环境部署
---------------

1. git clone 或者 checkout至本地目录
2. 修改：MockServer/config.py 数据库相关配置
    ```
    USERNAME = 'root'
    PASSWORD = 'xxxx'
    HOST = '127.0.0.1'
    DB = 'MockServer'
    ```
3. 安装相应依赖库
    ```bash
    pip install -r requirements.txt
    ```
4. 创建MockServer数据库, 默认DB是MockServer
5. 生成数据库迁移脚本，应用表结构
    ```bash
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    ```
6. Start Server
    ```bash
    python run.py
    ```# mock
