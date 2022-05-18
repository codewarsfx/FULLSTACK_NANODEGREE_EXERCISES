import psycopg2

connection= psycopg2.connect('dbname=codewarsfx')

cursor= connection.cursor()

cursor.execute('drop table if exists table2')

cursor.execute(''' 

create table table2(id bigserial primary key not null , name varchar(30) unique not null)


''')

cursor.execute('insert into table2 (name) values (%(hi)s)',{'hi':'ibrahim'})
connection.commit()

cursor.close()
connection.close()