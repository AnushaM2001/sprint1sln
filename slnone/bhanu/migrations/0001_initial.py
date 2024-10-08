# Generated by Django 5.0.7 on 2024-08-02 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Educationalloan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('mail_id', models.EmailField(max_length=254, unique=True)),
                ('mobile_number', models.CharField(max_length=10, unique=True)),
                ('country', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('university_name', models.CharField(max_length=100)),
                ('score_card', models.FileField(upload_to='score_cards/')),
                ('GRE_score', models.DecimalField(decimal_places=2, max_digits=15)),
                ('IELTS_score', models.DecimalField(decimal_places=2, max_digits=15)),
                ('TOEFL_score', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Duolingo_score', models.DecimalField(decimal_places=2, max_digits=15)),
                ('PTE_score', models.DecimalField(decimal_places=2, max_digits=15)),
                ('student_work_experience', models.TextField()),
                ('cibil_score', models.IntegerField()),
                ('loan_required', models.DecimalField(decimal_places=2, max_digits=15)),
                ('backlogs', models.PositiveIntegerField()),
                ('residence_location', models.CharField(max_length=200)),
                ('permanent_location', models.CharField(max_length=200)),
                ('co_applicant_type', models.CharField(choices=[('SALARIEDEMPLOYEE', 'Salariedemployee'), ('SELFEMPLOYEED', 'SelfEmployeed')], max_length=20)),
                ('co_applicant_parent_name', models.CharField(blank=True, max_length=100, null=True)),
                ('co_applicant_company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('co_applicant_salaried_designation', models.CharField(blank=True, max_length=100, null=True)),
                ('co_applicant_salaried_net_pay', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('co_applicant_salaried_emis', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('co_applicant_salaried_cibil_score', models.IntegerField(blank=True, null=True)),
                ('co_applicant_self_employed_business_name', models.CharField(blank=True, max_length=100, null=True)),
                ('co_applicant_self_employed_itr_mandatory', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, null=True)),
                ('co_pplicant_self_employed_itr_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('co_applicant_self_employed_business_licence', models.FileField(blank=True, null=True, upload_to='business_licences/')),
                ('property_location', models.CharField(max_length=200)),
                ('co_applicant_property_details', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('property_type', models.CharField(choices=[('House', 'House'), ('Plot', 'Plot'), ('Flat', 'Flat'), ('Apartment', 'Apartment'), ('Open Land', 'Open Land')], max_length=50)),
                ('property_market_value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('property_govt_value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('property_local_government_body', models.CharField(max_length=100)),
                ('application_id', models.CharField(blank=True, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_detail_verifaction', models.CharField(blank=True, max_length=50)),
                ('documents_upload_verification', models.CharField(blank=True, max_length=50)),
                ('documents_verification', models.CharField(blank=True, max_length=50)),
                ('eligibility_check_verification', models.CharField(blank=True, max_length=50)),
                ('bank_login_verification', models.CharField(blank=True, max_length=50)),
                ('kyc_and_document_verification', models.CharField(blank=True, max_length=50)),
                ('enach_verification', models.CharField(blank=True, max_length=50)),
                ('field_verification', models.CharField(blank=True, max_length=50)),
                ('income_verification', models.CharField(blank=True, max_length=50)),
                ('verification_status', models.CharField(blank=True, max_length=100)),
                ('loan', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicationverification', to='bhanu.educationalloan')),
            ],
        ),
        migrations.CreateModel(
            name='Educationloan_document_upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhar_card_front', models.ImageField(upload_to='EDUdocuments/adhar_card/front/')),
                ('adhar_card_back', models.ImageField(upload_to='EDUdocuments/adhar_card/back/')),
                ('pan_card', models.ImageField(upload_to='EDUdocuments/pan_card/')),
                ('customer_photo', models.ImageField(upload_to='EDUdocuments/customer_photo/')),
                ('pay_slip_1', models.FileField(upload_to='EDUdocuments/pay_slips/')),
                ('pay_slip_2', models.FileField(upload_to='EDUdocuments/pay_slips/')),
                ('pay_slip_3', models.FileField(upload_to='EDUdocuments/pay_slips/')),
                ('bank_statement', models.FileField(upload_to='EDUdocuments/bank_statements/')),
                ('employee_id_card', models.FileField(upload_to='EDUdocuments/employee_id_cards/')),
                ('loan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='personal_details', to='bhanu.educationalloan')),
            ],
        ),
    ]
