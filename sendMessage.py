import time
import pywhatkit
# import pyautogui
# from pynput.keyboard import Key, Controller
import keyboard


# keyboard = Controller()


def send_whatsapp_message(phone_no: str, file_path: str):
    try:
        # pywhatkit.sendwhatmsg_instantly(
        #     phone_no="<phone-number>",
        #     message=msg,
        #     tab_close=True
        # )
        print("sending message to " + phone_no)
        caption = """
        You are cordially invited for Guru Puja event on 30 July 2023. Please show this invitation card having your Registration Number for entry in the event. 
        - RVK Bangalore

    Venue - Ramana Maharshi Heritage Auditorium https://maps.app.goo.gl/iu4oDAX4LchZZuG78
        """
        pywhatkit.sendwhats_image(phone_no, file_path, caption)
        time.sleep(33)
        keyboard.press_and_release('cmd+w')
        print("message sent to " + phone_no)
    except Exception as e:
        print(str(e))


# if __name__ == "__main__":
#     send_whatsapp_message(msg="Test message from a Python script!")
