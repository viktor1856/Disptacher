import sqlite3
import os


class SqlLiteDb:
    """
    Класс для работы с БД Диспетчер
    """
    def __init__(self):
        path = os.path.abspath(os.curdir)
        if os.path.isfile(path + '\\DispatcherBase.db'):
            self.connection_db = sqlite3.connect(path + '\\DispatcherBase.db')

        else:
            print('БД не найдено')

            print('Создаю новую БД')
            self.connection_db = sqlite3.connect(path + '\\DispatcherBase.db')

    def get_task_day(self, param: str) -> list:
        """
         Возвращает список задач на указанную дату

        :param param: Дата в формате 'дд.мм.гггг'

        :return: список задач на заданное число


        """
        try:
            cursor = self.connection_db.cursor()
            sql_text = ('select task.id_task, autos.name_auto, drivers.fam, drivers.nam, drivers.patr, task.text_task, '
                        'task.begin_work, customers.name_customer '
                        'from task '
                        'join drivers  on task.id_driver = drivers.id_driver '
                        'join autos on task.id_auto = autos.id_auto '
                        'join customers on task.customer_id = customers.id_customer '                            
                        'where Calendar = :date_calendar '
                        'order by autos.name_auto')
            cursor.execute(sql_text, [param])
            task_list = cursor.fetchall()
            cursor.close()
            return task_list
        except Exception as e:
            print('Error: db_class->get_task_day ' + str(e))

    def update_customer(self, params):
        try:
            cursor = self.connection_db.cursor()
            cursor.execute("update customers set name_customer=:name_customer where "
                           "id_customer = :id_customer ", params)
            cursor.close()
            self.connection_db.commit()
        except Exception as e:
            print('Error: dbClass->update_customer() ' + str(e))

    def delete_customer(self, param):
        try:
            cursor = self.connection_db.cursor()
            cursor.execute("delete from customers where id_customer = :id_customer", [param])
            cursor.close()
            self.connection_db.commit()
        except Exception as e:
            print('Error: dbClass->delete_customer() ' + str(e))

    def insert_new_customer(self, param):
        """
        Метод добавления нового заказчика в таблицу заказчиков

        :param param: Наименование заказчика
        :type param: str
        """
        try:
            cursor = self.connection_db.cursor()
            cursor.execute("insert into customers(name_customer) "
                           "values(:name_customer)", [param])
            cursor.close()
            self.connection_db.commit()
        except Exception as e:
            print('Error: dbClass->insert_new_customer() ' + str(e))

    def select_all_customers(self):
        try:
            cursor = self.connection_db.cursor()
            cursor.execute('select * from customers')
            customers_list = cursor.fetchall()
            cursor.close()
            return customers_list
        except Exception as e:
            print('Error: db_class->select_all_customers ' + str(e))

    def select_auto_info(self, id_auto):
        try:
            cursor = self.connection_db.cursor()
            cursor.execute('select * from autos where id_auto = :id_auto', [id_auto])
            auto_info = cursor.fetchone()
            cursor.close()
            return auto_info
        except Exception as e:
            print('Error: db_class->select_auto_info ' + str(e))

    def update_auto(self, params):
        try:
            cursor = self.connection_db.cursor()
            cursor.execute("update autos set name_auto = :name_auto ,type_auto = :type_auto,"
                           " category_drivers = :category_drivers, skzi = :skzi, estr = :estr,"
                           "gos_number = :gos_number  where "
                           "id_auto = :id_auto ", params)
            cursor.close()
            self.connection_db.commit()
        except Exception as e:
            print('Error: dbClass->update_auto() ' + str(e))

    def delete_auto(self, param):
        cursor = self.connection_db.cursor()
        cursor.execute("delete from autos where id_auto = :id_auto", param)
        cursor.close()
        self.connection_db.commit()

    def insert_new_auto(self, param):
        try:
            cursor = self.connection_db.cursor()
            cursor.execute("insert into autos(name_auto,type_auto, category_drivers, skzi, estr,"
                           "gos_number ) "
                           "values(:name_auto, :type_auto, :category, :skzi, :estr,"
                           ":gos_number)", param)
            cursor.close()
            self.connection_db.commit()
        except Exception as e:
            print('Error: dbClass->insert_new_auto() ' + str(e))

    def select_category_auto(self, param):
        try:
            cursor = self.connection_db.cursor()
            if param == 'Прочее':
                cursor.execute("select name,shifr from dictionary where kod_dict in (2,3)"
                               "order by name")
            else:
                cursor.execute('select name, shifr from dictionary where id_parent =('
                               'select id_dict from dictionary where kod_dict  = 1 and '
                               ' name = :param) order by name', [param])
            list_category_type = cursor.fetchall()
            cursor.close()
            return list_category_type
        except Exception as e:
            print('Error: db_class->select_category_auto ' + str(e))

    def select_auto_type(self):
        try:
            cursor = self.connection_db.cursor()
            cursor.execute('select  name from dictionary where kod_dict = 1 order by name desc')
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
    sp = test.select_category_auto('Легковое ТС')
    print(sp)


if __name__ == '__main__':
    main()
