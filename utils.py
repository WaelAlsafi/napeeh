



def get_user_info(update):
    user = update.message.from_user
    user_id = user.id
    username = user.username
    first_name = user.first_name
    last_name = user.last_name

    name = ""
    if first_name:
        name = first_name
    if last_name:
        name = name + " " + last_name

    info = {
        "user_id":user_id,
        "username":username,
        "first_name":first_name,
        "last_name":last_name,
        "name":name
    }
    return info


def get_workshop_number_by_name(workshop_name, data_dict):
    for number, details in data_dict.items():
        if details["name"] == workshop_name:
            return number
    
    return None



import sys
import importlib
import re
import time
import tele

def detect_reload_expression(text):
    # Regular expression to match importlib.reload(module_name)
    pattern = r'^importlib\.reload\(\s*([\w\.]+)\s*\)\s*$'
    
    match = re.match(pattern, text.strip())
    
    if match:
        # Extract and return the module name if matched
        module_name = match.group(1)
        print("module_name", module_name)
        return module_name
    print("module_name", None)
    return None

def reload_module(module_name):
    if module_name in sys.modules:
        print("module found in sys.modules")
        module = sys.modules[module_name]
    else:
        try:
            importlib.import_module(module_name)
            module = module_name
            print("lib not in sys.modules but imported")
        except:
            print("lib not in sys.modules and cant be imported")
            module = None

    if module:
        importlib.reload(module)
        print(f'Module {module_name} reloaded successfully.')
        return True
    else:
        print(f'Module {module_name} not found.')
    return False




async def importlib_handler(user_response,update, context):
        # try:
            module_name = detect_reload_expression(user_response)
            if module_name:
                message = await update.message.reply_text("detecting the module...")
                context.chat_data["message_id"] = message.message_id
                time.sleep(0.5)
                message_id = context.chat_data.get("message_id")
                chat_id = update.message.chat.id
                await tele.edit_message( chat_id, message_id, f"reloading {module_name}...", context)
                if reload_module(module_name):
                    time.sleep(0.5)
                    await tele.edit_message( chat_id, message_id, f"{module_name} has been reloaded successfully ✅", context)
                else:
                    await tele.edit_message( chat_id, message_id, f"{module_name} can't reloaded  ", context)
                return True

