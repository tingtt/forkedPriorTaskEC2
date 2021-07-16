# Prior task about docker in EC2

## Build and up containers

```shell
$ docker-compose build
$ docker-compose up
```

or

```shell
$ docker-compose up -d --build
```

---

## Incomplete

- pythonでMySQLからSELECTした時の値が文字化けするためコード側でデコードしている。
  - mysql-connector-python（ライブラリ）での接続処理時の文字コード指定を変更しても変わらなかった。