import psycopg2
from psycopg2.extras import DictCursor

def getConn ():
     conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="microblog",
                        password="micro",
                        port="5432")
     
     return conn

def readTimeline (login):

    conn = getConn()
    
    cursor = conn.cursor(cursor_factory= DictCursor)

    sql = """SELECT 
                p.id,	
                uo.login,
                p.text,
                p.create_date
            from post p
            join user_follow uf on p.user_id = uf.user_id_following
            join users u on uf.user_id_follower = u.id
            join users uo on p.user_id = uo.id
            where u.login = %s
            ORDER BY p.create_date DESC;"""


    
    cursor.execute(sql, (login,))

    resultado = cursor.fetchall()

    conn.close()

    return resultado