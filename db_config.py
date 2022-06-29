import datetime
import os
from dotenv import load_dotenv
from playhouse.db_url import connect
from peewee import Model, IntegerField, CharField, TimestampField

# .envの読み込み
load_dotenv()

# 実行したSQLをログで出力する設定
# logger = logging.getLogger("peewee")
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)

# データベースへの接続設定
# db = SqliteDatabase('peewee_db.sqlite')  # SQLite固定の場合
db = connect(os.environ.get("DATABASE"))  # 環境変数に合わせて変更する場合
# db = connect(os.environ.get('DATABASE') or 'sqlite:///peewee_db.sqlite')  # 環境変数が無い場合にデフォルト値として値を設定することも可能

# 接続NGの場合はメッセージを表示
if not db.connect():
    print("接続NG")
    exit()


class Message(Model):
    """Message Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    Name = CharField()
    Age = IntegerField()
    pub_date = TimestampField(default=datetime.datetime.now())

    class Meta:
        database = db
        table_name = "user_info"


db.create_tables([Message])
