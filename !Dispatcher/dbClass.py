import sqlite3
import os


class SqlLiteDb:
    def __init__(self):
        path = os.path.abspath(os.curdir)
        if os.path.isfile(path + '\\DispatcherBase.db'):
            self.connection_db = sqlite3.connect(path + '\\DispatcherBase.db')

        else:
            print('БД не найдено')

            print('Создаю новую БД')
            self.connection_db = sqlite3.connect(path + '\\DispatcherBase.db')

    def select_category_auto(self, param):
        try:
            cursor = self.connection_db.cursor()
            if param == 'Прочее':
                cursor.execute("select name from dictionary where kod_dict in (2,3)"
                               "order by name")
            else:
                cursor.execute('select name from dictionary where id_parent =('
                               'select id_dict from dictionary where kod_dict  = 1 and '
                               ' name = :param) order by name', [param])
            list_category_type = []
            for category in cursor.fetchall():
                list_category_type.append(category[0])
            cursor.close()
            return list_category_type
        except Exception as e:
            print('Error: db_class->select_category_auto ' + str(e))

    def select_auto_type(self):
        try:
            cursor = self.connection_db.cursor()
            cursor.execute('select name from dictionary where kod_dict = 1 order by name desc')
            list_auto_type = []
            for auto_type in cursor.fetchall():
                list_auto_type.append(auto_type[0])
            cursor.close()
            return list_auto_type
        except Exception as e:
            print('Error: db_class->select_auto_type ' + str(e))

    def select_driver_info(self, id_driver):
        try:
            cursor = self.connection_db.cursor()
            cursor.execute('select * from drivers where id_driver = :id_driver', [id_driver])
            driver_info = cursor.fetchone()
            cursor.close()
            return driver_info
        except Exception as e:
            print('Error: db_class->select_driver_info ' + str(e))

    def delete_driver(self, param):
        cursor = self.connection_db.cursor()
        cursor.execute("delete from drivers where id_driver = :id_driver", param)
        cursor.close()
        self.connection_db.commit()

    def select_all_drivers(self):
        cursor = self.connection_db.cursor()
        cursor.execute("select id_driver, fam, nam, patr, date_birth from drivers")
        all_drivers = cursor.fetchall()
        cursor.close()
        return all_drivers

    def select_all_autos(self):
        cursor = self.connection_db.cursor()
        cursor.execute("select id_auto, gos_number, name_auto from autos")
        all_autos = cursor.fetchall()
        cursor.close()
        return all_autos

    def insert_new_driver(self, param):
        try:
            cursor = self.connection_db.cursor()
            cursor.execute("insert into drivers(fam, nam, patr, date_birth, end_drivers_document,"
                           "skzi, skzi_date, estr, estr_date, category_auto, category_tractor) "
                           "values(:fam, :nam, :patr, :date_birth, :end_drivers_document,"
                           ":skzi, :skzi_date, :estr, :estr_date, :category_auto, :category_tractor)", param)
            cursor.close()
            self.connection_db.commit()
        except Exception as e:
            print('Error: dbClass->insert_new_driver() ' + str(e))

    def update_driver(self, params):
        try:
            cursor = self.connection_db.cursor()
            cursor.execute("update drivers set fam = :fam, nam = :nam, patr = :patr, date_birth = :date_birth,"
                           "end_drivers_document = :end_drivers_document,"
                           "skzi = :skzi, skzi_date = :skzi_date, estr = :estr, estr_date = :estr_date,"
                           "category_auto = :category_auto, category_tractor = :category_tractor where "
                           "id_driver = :id_driver ", params)
            cursor.close()
            self.connection_db.commit()
        except Exception as e:
            print('Error: dbClass->update_driver() ' + str(e))


def main():

    test = SqlLiteDb()
    sp = test.select_category_auto('')
    print(sp)


if __name__ == '__main__':
    main()
