import MotionDetector1
import ColorDetect
import Error_database
from datetime import datetime
# Still shows windows for demonstration

now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
uuid = "LVI-100234" #Use that one enviromental var to do this part
board_model = "GEN2" #Use another one of the enviromental variables (lame)

# Press q to exit the windows, represents accelerometer
MotionDetector1.DetectMotion()

# Color detect for camera obstruction
if not ColorDetect.DetectColors():
    # Log into error database as a warning
    Error_database.log_error(date_time,uuid,board_model, error_code=111)
