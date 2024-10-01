

#bot =Bot(token=TOKEN)

name_column = 'الاسم كما تودون أن يظهر في شهادة الحضور'
student_id_column = 'البريد الإلكتروني أو رقم الهاتف'
sex_column = "الجنس"

start_message = """السلام عليكم ورحمة الله وبركاته
حياك الله وبياك <a href="tg://user?id={user_id}">{first_name}</a> ✨

أي شهادة تريد؟
"""


#message_handler constants
choose_message ="قم بإرسال رقم هاتفك أو بريدك الإلكتروني الذي سجلت به في استمارة الحضور لأتمكن من إرسال شهادتك لك."
restart_message = "اضغط هنا للعودة إلى البداية /start"
invalid_student_id_message = "البيانات التي أدخلتها غير مطابقة لقاعدة بياناتنا، الرجاء التأكد من صحة البيانات والمحاولة مرة أخرى، أو اضغط هنا للعودة إلى البداية /start"


workshops_info = {
    1:{
        "name":"تهيئة الأطفال لدخول الصف الأول الابتدائي في المدرسة",
        "youtube_link":None,
        "form_link": None, 
        "male_img": "male.jpg",
        "female_img": "female.jpg"

    },
    2:{
        "name":"تقنيات إبداعية في دعم تميز الأبناء",
        "youtube_link":None,
        "form_link": None, 
        "male_img": "male2.jpg",
        "female_img": "female2.jpg"
    },
    3:{
        "name":"خطوات لرفع المعنويات مع بداية عام دراسي مميز",
        "youtube_link":None,
        "form_link": None, 
    },
    4:{
        "name":"فنون إكساب المهارات",
        "youtube_link":None,
        "form_link": None, 
        "male_img": "male4.jpg",
        "female_img": "female4.jpg"
    }
}

sheet_id = "***"
specific_sheet_id = "****"
attendence_file = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&{specific_sheet_id}"

sheet_id2 = "***"
specific_sheet_id2 = ""
attendence_file2 = f"https://docs.google.com/spreadsheets/d/{sheet_id2}/export?format=csv"

sheet_id3 = "***"
specific_sheet_id3 = ""
attendence_file3 = f"https://docs.google.com/spreadsheets/d/{sheet_id2}/export?format=csv"

sheet_id4 = "***"
specific_sheet_id4 = ""
attendence_file4 = f"https://docs.google.com/spreadsheets/d/{sheet_id4}/export?format=csv"

attendence_files = [attendence_file, attendence_file2, attendence_file3, attendence_file4]
user_data = {}

# folder_path = "/home/waelalsafi/napeeh/"
folder_path = "certificates_templates_and_fonts/"
arabic_font = "ArabicUIDisplayMedium.otf"
english_font = "LibreBaskerville-Bold.ttf"