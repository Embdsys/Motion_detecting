import sqlite3
"""
Created by: Juan Quintana

    Most of these error codes will make the box restart periodically (~2hr) until fixed.   

    *****error_code documentation*****
Error_code  Common cause    Description
    100     Keypad          lsusb cant detect the keypad
    110     Camera          lsusb cant detect the webcam
    111     Camera          *Cant detect colors and could be obstructed     
    102     Audio           Audio mute GPIO 24 is HIGH
    200     Ethernet        Ping to 1.1.1.1 and google failed
    300     PIC18           AACK from PIC not received by Rpi         
    400     Accelerometer   *Accel was triggered
    
    *These don't make the box reset but are warnings
"""
def log_error(date, uuid, board_model, error_code):
    con = sqlite3.connect('logs.db')
    cur = con.cursor()

    try:
        # Create table
        cur.execute('''CREATE TABLE logs
                       (date text, uuid text,  board_model text, error_code text)''')
    except:
        print("Table existed")
    # The qmark style used with executemany():
    lang_list = [
        (date, uuid, board_model, error_code),
    ]

    cur.executemany("INSERT INTO logs VALUES (?,?,?,?)", lang_list)

    # Save (commit) the changes
    con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    con.close()

#log_error("20-2-11","LVI190029","LV11","400")

if __name__ == "__main__":
    log_error()