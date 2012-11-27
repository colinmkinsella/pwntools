

mysql_tables = 'SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema <> "information_schema" AND table_schema <> "mysql"'

def mysql_columns(table):
    return 'SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name = "%s"' % table

def mysql_dump(table, columns, rows = -1):
    return 'SELECT GROUP_CONCAT(CONCAT_WS("|",%s) SEPARATOR "\\n") from %s' % \
        (','.join(columns), table)

mysql_fulldump = ''