import os
import csv
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='my_notes'
)

mycursor = mydb.cursor()
sql_check_row = "SELECT * FROM notes WHERE id = %s"


class Note:
    def create_note(self, title, description):
        sql = "INSERT INTO notes (title, description) VALUES (%s, %s)"
        val = title, description
        mycursor.execute(sql, val)
        mydb.commit()
        print('Note created successfully!')


    def show_notes(self):
        sql = "SELECT * FROM notes"
        mycursor.execute(sql)
        notes = mycursor.fetchall()
        if notes:
            # sql = 'SELECT * FROM notes'
            # mycursor.execute(sql)
            # notes = mycursor.fetchall()
            for note in notes:
                print(note)
        else:
            print('There are no notes to be shown!')


    def delete_note(self, id):
        val = (id,)
        mycursor.execute(sql_check_row, val)
        if mycursor.fetchone():
            sql = 'DELETE FROM notes WHERE id = %s'
            mycursor.execute(sql, val)
            mydb.commit()
            print('Note deleted successfully!')
        else:
            print('Note does not exist!')


    def update_title(self, title, id):
        val_id = (id,)
        mycursor.execute(sql_check_row, val_id)
        if mycursor.fetchall():
            sql = 'UPDATE notes SET title = %s WHERE id = %s'
            val_title_id = (title, id)
            mycursor.execute(sql, val_title_id)
            mydb.commit()
            print('Note(s) updated!')
        else:
            print('Note does not exist')


    def update_description(self, description, id):
        val_id = (id,)
        mycursor.execute(sql_check_row, val_id)
        if mycursor.fetchall():
            sql = 'UPDATE notes SET description = %s WHERE id = %s'
            val_desc_id = (description, id)
            mycursor.execute(sql, val_desc_id)
            mydb.commit()
            print('Note(s) updated!')
        else:
            print('Note does not exist')

    def save_to_csv(self):
        sql = "SELECT * FROM notes"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        id_to_row = {}

        for row in rows:
            row_dict = {
                mycursor.description[i][0]: value
                for i, value in enumerate(row)
            }
            id_to_row[row[0]] = row_dict

        filename = 'my_notes.csv'
        file_exists = os.path.isfile(filename)

        with open(filename, mode='w', newline='') as file:
            fieldnames = [i[0] for i in mycursor.description]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            for row_dict in id_to_row.values():
                writer.writerow(row_dict)


        print('Notes saved to csv!')
