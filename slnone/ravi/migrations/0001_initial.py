# Generated by Django 5.0.6 on 2024-08-10 05:31

import django.core.validators
import django.db.models.deletion
import ravi.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_type', models.CharField(choices=[('HL', 'HL'), ('HLBT', 'HLBT')], max_length=10)),
                ('first_name', models.CharField(max_length=100, validators=[ravi.models.validate_only_letters])),
                ('last_name', models.CharField(max_length=100, validators=[ravi.models.validate_only_letters])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('date_of_birth', models.DateField(validators=[ravi.models.validate_date])),
                ('mobile_number', models.CharField(max_length=10, validators=[ravi.models.validate_mobile_number])),
                ('pan_card_number', models.CharField(max_length=10, validators=[ravi.models.validate_pan])),
                ('aadhar_card_number', models.CharField(max_length=12, validators=[ravi.models.validate_aadhar_number])),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], max_length=10)),
                ('email_id', models.EmailField(max_length=254, validators=[ravi.models.validate_email])),
                ('current_address', models.TextField(validators=[ravi.models.validate_address])),
                ('current_address_pincode', models.CharField(max_length=6, validators=[ravi.models.validate_pincode])),
                ('aadhar_address', models.TextField(validators=[ravi.models.validate_address])),
                ('aadhar_pincode', models.CharField(max_length=6, validators=[ravi.models.validate_pincode])),
                ('running_emis_per_month', models.CharField(max_length=10, validators=[ravi.models.validate_amount])),
                ('income_source', models.CharField(choices=[('Job', 'Job'), ('Business', 'Business')], max_length=10)),
                ('net_salary_per_month', models.CharField(blank=True, max_length=10, null=True, validators=[ravi.models.validate_amount])),
                ('company_name', models.CharField(blank=True, max_length=100, null=True, validators=[ravi.models.validate_only_letters])),
                ('company_type', models.CharField(blank=True, choices=[('Private', 'Private'), ('Public', 'Public'), ('Government', 'Government'), ('Other', 'Other')], max_length=50, null=True)),
                ('job_joining_date', models.DateField(blank=True, null=True)),
                ('job_location', models.CharField(blank=True, max_length=100, null=True)),
                ('total_job_experience', models.IntegerField(blank=True, null=True)),
                ('work_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('office_address_pincode', models.CharField(blank=True, max_length=6, null=True, validators=[ravi.models.validate_pincode])),
                ('net_income_per_month', models.CharField(blank=True, max_length=10, null=True, validators=[ravi.models.validate_amount])),
                ('business_name', models.CharField(blank=True, max_length=100, null=True, validators=[ravi.models.validate_only_letters])),
                ('business_type', models.CharField(blank=True, choices=[('Retail', 'Retail'), ('Manufacturing', 'Manufacturing'), ('Services', 'Services'), ('Other', 'Other')], max_length=50, null=True)),
                ('business_establishment_date', models.DateField(blank=True, null=True)),
                ('gst_number', models.CharField(blank=True, default='00AAAAA0000A1Z', max_length=15, null=True, validators=[ravi.models.validate_gst_number])),
                ('mother_name', models.CharField(max_length=100, validators=[ravi.models.validate_only_letters])),
                ('father_name', models.CharField(max_length=100, validators=[ravi.models.validate_only_letters])),
                ('nature_of_business', models.CharField(blank=True, max_length=100, null=True)),
                ('turnover_per_year', models.CharField(blank=True, max_length=10, null=True, validators=[ravi.models.validate_amount])),
                ('business_location', models.CharField(blank=True, max_length=100, null=True, validators=[ravi.models.validate_address])),
                ('business_address_pincode', models.CharField(blank=True, max_length=6, null=True, validators=[ravi.models.validate_pincode])),
                ('house_plot_purchase_value', models.CharField(default='eneter', max_length=10, validators=[ravi.models.validate_amount])),
                ('required_loan_amount', models.CharField(default='enter', max_length=10, validators=[ravi.models.validate_amount])),
                ('existing_loan_bank_nbfc_name', models.CharField(default='', max_length=100)),
                ('existing_loan_amount', models.CharField(default='', max_length=10, validators=[ravi.models.validate_amount])),
                ('ref1_person_name', models.CharField(default='', max_length=200, validators=[ravi.models.validate_only_letters])),
                ('ref2_person_name', models.CharField(default='', max_length=200, validators=[ravi.models.validate_only_letters])),
                ('ref1_mobile_number', models.CharField(default='', max_length=10, validators=[ravi.models.validate_mobile_number])),
                ('ref2_mobile_number', models.CharField(default='', max_length=10, validators=[ravi.models.validate_mobile_number])),
                ('coapplicant_first_name', models.CharField(default='', max_length=100, validators=[ravi.models.validate_only_letters])),
                ('coapplicant_last_name', models.CharField(default='', max_length=100, validators=[ravi.models.validate_only_letters])),
                ('coapplicant_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=10)),
                ('coapplicant_age', models.DateField(default='enter', validators=[ravi.models.validate_age])),
                ('coapplicant_relationship', models.CharField(default='', max_length=50)),
                ('coapplicant_mobile_number', models.CharField(default='', max_length=10, validators=[ravi.models.validate_mobile_number])),
                ('coapplicant_email_id', models.EmailField(max_length=254, validators=[ravi.models.validate_email])),
                ('coapplicant_occupation', models.CharField(default='', max_length=100, validators=[ravi.models.validate_only_letters])),
                ('coapplicant_net_income_per_month', models.CharField(default='', max_length=10, validators=[ravi.models.validate_amount])),
                ('random_number', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='hlbasicdetailform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25, validators=[ravi.models.validate_only_letters])),
                ('pan_number', models.CharField(max_length=10, validators=[ravi.models.validate_pan])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('email', models.EmailField(max_length=254, validators=[ravi.models.validate_email])),
                ('date_of_birth', models.DateField()),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], default='Single', max_length=10)),
                ('required_loan_amount', models.CharField(max_length=10, validators=[ravi.models.validate_amount])),
                ('terms_accepted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('random_number', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, validators=[ravi.models.validate_only_letters])),
                ('last_name', models.CharField(max_length=100, validators=[ravi.models.validate_only_letters])),
                ('gender', models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male'), ('OTHER', 'Other')], max_length=10)),
                ('father_name', models.CharField(max_length=100, validators=[ravi.models.validate_only_letters])),
                ('date_of_birth', models.DateField(validators=[ravi.models.validate_date])),
                ('mobile_number', models.CharField(max_length=10, validators=[ravi.models.validate_mobile_number])),
                ('pan_card_number', models.CharField(max_length=10, validators=[ravi.models.validate_pan])),
                ('aadhar_card_number', models.CharField(max_length=12, validators=[ravi.models.validate_aadhar_number])),
                ('marital_status', models.CharField(choices=[('SINGLE', 'Single'), ('MARRIED', 'Married')], max_length=10)),
                ('email', models.EmailField(max_length=254, validators=[ravi.models.validate_email])),
                ('current_address', models.TextField(validators=[ravi.models.validate_address])),
                ('current_address_pincode', models.CharField(max_length=6, validators=[ravi.models.validate_pincode])),
                ('aadhar_address', models.TextField(validators=[ravi.models.validate_address])),
                ('aadhar_pincode', models.CharField(max_length=6, validators=[ravi.models.validate_pincode])),
                ('running_emis', models.CharField(max_length=10, validators=[ravi.models.validate_amount])),
                ('net_salary', models.CharField(max_length=10, validators=[ravi.models.validate_amount])),
                ('company_name', models.CharField(max_length=100, validators=[ravi.models.validate_only_letters])),
                ('company_type', models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private'), ('GOVERNMENT', 'Government'), ('SELF_EMPLOYED', 'Self-employed'), ('OTHER', 'Other')], max_length=20)),
                ('job_joining_date', models.DateField()),
                ('job_location', models.CharField(max_length=100)),
                ('total_job_experience', models.IntegerField()),
                ('work_email', models.EmailField(max_length=254, validators=[ravi.models.validate_email])),
                ('office_address', models.TextField(validators=[ravi.models.validate_address])),
                ('office_address_pincode', models.CharField(max_length=6, validators=[ravi.models.validate_pincode])),
                ('required_loan_amount', models.CharField(max_length=10, validators=[ravi.models.validate_amount])),
                ('ref1_name', models.CharField(max_length=100, validators=[ravi.models.validate_only_letters])),
                ('ref1_mobile', models.CharField(max_length=10, validators=[ravi.models.validate_mobile_number])),
                ('ref2_name', models.CharField(max_length=100, validators=[ravi.models.validate_only_letters])),
                ('ref2_mobile', models.CharField(max_length=10, validators=[ravi.models.validate_mobile_number])),
                ('own_house', models.BooleanField()),
                ('random_number', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='plbasicdetailform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25, validators=[ravi.models.validate_only_letters])),
                ('pan_number', models.CharField(max_length=10, validators=[ravi.models.validate_pan])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('date_of_birth', models.DateField()),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], default='Single', max_length=10)),
                ('required_loan_amount', models.CharField(max_length=10, validators=[ravi.models.validate_amount])),
                ('terms_accepted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('random_number', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhar_card_front', models.ImageField(upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('adhar_card_back', models.ImageField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('pan_card', models.ImageField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('customer_photo', models.ImageField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('home_plot_photo_1', models.ImageField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('home_plot_photo_2', models.ImageField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('home_plot_photo_3', models.ImageField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('home_plot_photo_4', models.ImageField(blank=True, null=True, upload_to='documents/,', validators=[ravi.models.validate_image_file])),
                ('latest_3_months_banked_statement', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('latest_3_months_payslips_1', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('latest_3_months_payslips_2', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('latest_3_months_payslips_3', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('employee_id_card', models.ImageField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('business_proof_1', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('business_proof_2', models.FileField(blank=True, upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('latest_12_months_banked_statement', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('business_office_photo', models.ImageField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('latest_3_yrs_itr_1', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('latest_3_yrs_itr_2', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('latest_3_yrs_itr_3', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('current_address_proof', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('existing_loan_statement', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('other_documents_1', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('other_documents_2', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('other_documents_3', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('other_documents_4', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('co_adhar_card_front', models.ImageField(upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('co_adhar_card_back', models.ImageField(upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('co_pan_card', models.ImageField(upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('co_selfie_photo', models.ImageField(upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('random_number', models.CharField(blank=True, max_length=6, null=True)),
                ('applicant_profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ravi.customerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='HomeApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_detail_verification', models.CharField(blank=True, max_length=50)),
                ('documents_upload_status', models.CharField(blank=True, max_length=50)),
                ('kyc_documents_verification_status', models.CharField(blank=True, max_length=50)),
                ('filed_officer_visit_inspection_status', models.CharField(blank=True, max_length=50)),
                ('eligibility_check_status', models.CharField(blank=True, max_length=50)),
                ('application_fee_paid_status', models.CharField(blank=True, max_length=50)),
                ('tele_verification_status', models.CharField(blank=True, max_length=50)),
                ('bank_login_fee_paid_status', models.CharField(blank=True, max_length=50)),
                ('bank_login_done_status', models.CharField(blank=True, max_length=50)),
                ('credit_manager_visit_status', models.CharField(blank=True, max_length=50)),
                ('bank_nbfc_soft_loan_sanction_letter_issued_status', models.CharField(blank=True, max_length=50)),
                ('legal_technical_completed_status', models.CharField(blank=True, max_length=50)),
                ('final_loan_sanctioned_status', models.CharField(blank=True, max_length=50)),
                ('agreement_signatures_done_status', models.CharField(blank=True, max_length=50)),
                ('enach_auto_debit_done_status', models.CharField(blank=True, max_length=50)),
                ('disbursement_status', models.CharField(blank=True, max_length=50)),
                ('post_documentation_mortgage_status', models.CharField(blank=True, max_length=50)),
                ('cheque_issued_loan_amount_credited_status', models.CharField(blank=True, max_length=50)),
                ('applicant_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ravi.customerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_card_front', models.ImageField(upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('aadhar_card_back', models.ImageField(upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('pan_card', models.ImageField(upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('customer_photo', models.ImageField(upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('payslip_1', models.FileField(upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('payslip_2', models.FileField(upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('payslip_3', models.FileField(upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('bank_statement', models.FileField(upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('employee_id_card', models.ImageField(upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('current_address_proof', models.FileField(upload_to='documents/', validators=[ravi.models.validate_image_file])),
                ('other_document_1', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('other_document_2', models.FileField(blank=True, null=True, upload_to='documents/', validators=[ravi.models.validate_pdf_file])),
                ('personal_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ravi.personaldetail')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_detail_verification', models.CharField(blank=True, max_length=50)),
                ('documents_upload_verification', models.CharField(blank=True, max_length=50)),
                ('documents_verification', models.CharField(blank=True, max_length=50)),
                ('eligibility_check_verification', models.CharField(blank=True, max_length=50)),
                ('bank_login_verification', models.CharField(blank=True, max_length=50)),
                ('kyc_and_document_verification', models.CharField(blank=True, max_length=50)),
                ('enach_verification', models.CharField(blank=True, max_length=50)),
                ('disbursement_verification', models.CharField(blank=True, max_length=50)),
                ('verification_status', models.CharField(blank=True, max_length=100)),
                ('personal_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ravi.personaldetail')),
            ],
        ),
    ]
