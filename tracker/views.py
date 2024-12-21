from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Attendance
from django.utils.timezone import now
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def home(request):
    students = Student.objects.all()
    return render(request, 'tracker/home.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    attendance = Attendance.objects.filter(student=student)
    
    return render(request, 'tracker/student_detail.html', {
        'student': student,
        'attendance': attendance
    })

def attendance_view(request):
    students = Student.objects.all()  # Fetch all students only once

    if request.method == "POST":
        # Handle date input, default to today's date
        date = request.POST.get('date')
        if not date:
            date = now().date()

        for student in students:
            attendance_status = request.POST.get(f'attendance_{student.id}')

            if attendance_status:
                # Update or create attendance record
                Attendance.objects.update_or_create(
                    student=student,
                    date=date,
                    defaults={'status': attendance_status},
                )

                # Send email if marked absent
                if attendance_status == "Absent" and student.email:
                    try:
                        send_mail(
                            subject="Attendance Alert: Absent Notification",
                            message=(
                                f"Dear {student.name},\n\n"
                                f"You have been marked as absent on {date}.\n"
                                f"If you believe this is a mistake, please contact the school administration.\n\n"
                                f"Regards,\nSchool Admin"
                            ),
                            from_email=settings.EMAIL_HOST_USER,
                            recipient_list=[student.email],
                            fail_silently=False,
                        )
                    except Exception as e:
                        # Log email error (optional, for debugging)
                        print(f"Failed to send email to {student.email}: {e}")

        # Redirect to avoid form resubmission on page refresh
        return redirect('attendance')

    # Render attendance form
    return render(request, 'tracker/attendance.html', {'students': students})
