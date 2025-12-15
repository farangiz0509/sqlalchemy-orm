from datetime import datetime
from school.create_tables import init_db
from school.crud import (
    create_student,
    get_students,
    get_one_student,
    search_students_by_first_name,
    search_students_by_name,
    update_student,
    filter_students_by_gender,
    filter_students_by_gpa,
    get_sorted_students_by_gpa,
    add_score,
    get_scores,
    get_student_with_scores,
    # Sertifikat CRUD funksiyalari keyin qo'shilsa shu yerga import qilamiz
)

# Bazani yaratish
init_db()

# 1. Insert - Studentlar uchun sertifikatlar qo'shish (Misol uchun student_id 1 va 2 bor deb faraz qilamiz)

# student 1 uchun sertifikat qo'shish (agar Certificate modeli qo'shilgan bo'lsa)
# from school.crud import add_certificate  # agar add_certificate yozilgan bo'lsa import qilamiz
# add_certificate(student_id=1, title="Python Basics", content="Completed course", certificate_code="CERT123ABC")

# student 2 uchun 2 ta sertifikat qo'shish
# add_certificate(student_id=2, title="Data Science", content="Completed DS course", certificate_code="CERT456DEF")
# add_certificate(student_id=2, title="AI Basics", content="Completed AI course", certificate_code="CERT789GHI")

# 2. Query
print("Barcha certificate larni oling")
# certificates = get_all_certificates()
# print(certificates)

print("is_verified=False bo'lgan certificate lar")
# unverified_certificates = get_certificates_by_verification(False)
# print(unverified_certificates)

print("Berilgan student_id uchun barcha certificate lar (student_id=2)")
# certificates_student_2 = get_certificates_by_student_id(2)
# print(certificates_student_2)

print("certificate_code bo‘yicha certificate qidirish (masalan CERT123ABC)")
# certificate = get_certificate_by_code("CERT123ABC")
# print(certificate)

print("issued_at bo‘yicha 5 ta oxirgi certificate")
# last_5_certificates = get_last_n_certificates(5)
# print(last_5_certificates)

# 3. Update
print("certificate_code bo‘yicha is_verified=True qilamiz (CERT123ABC)")
# update_certificate_verification("CERT123ABC", True)

# 4. Aggregation
print("Studentlar bo‘yicha certificate soni")
# cert_count_per_student = count_certificates_per_student()
# print(cert_count_per_student)

print("Eng ko‘p certificate olgan student")
# top_student = get_student_with_most_certificates()
# print(top_student)

print("is_verified bo‘lgan certificate larni count qil")
# verified_count = count_verified_certificates()
# print(verified_count)

# Shuningdek, Student va Scorelar bilan ishlashni tekshirish uchun quyidagilarni qo'shishingiz mumkin:

# Yangi student yaratish (agar studentlar hali yo'q bo'lsa)
# create_student('Ali', 'Valiyev', datetime(2005, 9, 3), bio='Python enthusiast')
# create_student('Bob', 'Smith', datetime(2004, 6, 15))

# Studentlarni olish
students = get_students()
print(f"Students: {students}")

# Studentni yangilash
# update_student(1, last_name='Nimadir')

# Ball qo'shish
# add_score(1, 'English', 88)
# add_score(2, 'Math', 95)

# Ballar va natijalarni ko'rish
scores = get_student_with_scores()
print(f"Students with scores: {scores}")
