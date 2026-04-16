import psycopg2

class PostgresQueryExecutor:
    def __init__(self, host='localhost', database='距离方位问答', user='postgres', password='1234', port="5432"):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cur = self.conn.cursor()
        except psycopg2.Error as e:
            print(f"Database connection error: {e}")
            raise

    def execute_sql(self, sql_statement):
        if not self.conn or not self.cur:
            self.connect()
        try:
            self.cur.execute(sql_statement)
            result = self.cur.fetchall()  # 获取执行结果
            headers = [desc[0] for desc in self.cur.description]
            self.conn.commit()  # 提交事务
            
            return headers, result
        except Exception as e:
            #print(f"Error executing SQL statement: {e}")
            return None, None

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()