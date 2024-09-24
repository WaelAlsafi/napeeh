import pandas as pd
import logging
from constants import student_id_column, attendence_files



def read_files(attendence_files):
    dfs = [0]
    for file in attendence_files:
        df = pd.read_csv(file)
        dfs.append(df)
    return dfs



def lst_of_student_id(df):
    student_id_list = df[student_id_column].tolist()
    for i in range(len(student_id_list)):
        student_id_list[i] = str(student_id_list[i])
        student_id_list[i] = student_id_list[i].strip()
        student_id_list[i] = student_id_list[i].lower()
    return student_id_list

# def cell_data(wanted_coulmn, key, key_coulmn,df):
#     raw_data = df[df[student_id_column] == key ]
#     cell = raw_data.iloc[0][wanted_coulmn]
#     return cell

def cell_data(wanted_column, key, key_column, df):
    try:
        # Filter the DataFrame based on the key_column
        df[student_id_column] = df[student_id_column].astype(str).str.strip().str.lower()
        raw_data = df[df[key_column] == key]

        if raw_data.empty:
            raise ValueError(f"No data found for key: {key}")

        # Access the first row and get the desired cell value
        cell = raw_data.iloc[0][wanted_column]
        return cell

    except KeyError as e:
        logging.error(f"KeyError: {e}. Check if the column '{wanted_column}' exists in the DataFrame.")
        print(f"KeyError: {e}. Check if the column '{wanted_column}' exists.")
        #context.bot.send_message(chat_id=logging_group_id, text=f"KeyError: {e}. Check if the column '{wanted_column}' exists.")
        return None

    except IndexError as e:
        logging.error(f"IndexError: {e}. The DataFrame might be empty or index out of bounds.")
        print(f"IndexError: {e}. The DataFrame might be empty or index out of bounds.")
        #context.bot.send_message(chat_id=logging_group_id, text=f"IndexError: {e}. The DataFrame might be empty or index out of bounds.")
        return None

    except ValueError as e:
        logging.error(f"ValueError: {e}")
        print(f"ValueError: {e}")
        #context.bot.send_message(chat_id=logging_group_id, text=f"ValueError: {e}")
        return None

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")
        #context.bot.send_message(chat_id=logging_group_id, text=f"Unexpected error: {e}")
        return None


df_lst = read_files(attendence_files)

