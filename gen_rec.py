def get_recommendations(age=None, sex=None, ancestry=None, pack_years=None, smoking=None, quit_within_past_15_years=None, overweight_or_obesity=None, cardiovascular_risk=None, cardiovascular_risk_7_5_to_10=None, rh_d_negative=None, pregnant=None, new_mother=None, substance_abuse_risk=None, skin_type=None):
    recommendations = []

    # B - Recommended (39)
    if (sex == 'female') and (age is not None) and (age >= 21 and age <= 65):
    	recommendations.append("Cervical Cancer: Screening -- Women aged 21 to 65 years")
    if age is not None and (age >= 50 and age <= 75):
        recommendations.append("Colorectal Cancer: Screening -- Adults aged 50 to 75 years")
    if sex == 'female' and (ancestry is not None and ancestry == 'BRCA1/2 gene mutation'):
        recommendations.append("BRCA-Related Cancer: Risk Assessment, Genetic Counseling, and Genetic Testing -- Women with a personal or family history of breast, ovarian, tubal, or peritoneal cancer or an ancestry associated with BRCA1/2 gene mutation")
    if sex == 'female' and age >= 35:
        recommendations.append("Breast Cancer: Medication Use to Reduce Risk -- Women at increased risk for breast cancer aged 35 years or older")
    if age is not None and (age >= 50 and age <= 74):
        recommendations.append("Breast Cancer: Screening -- Women aged 50 to 74 years")
    if (sex == 'pregnant' or (new_mother is not None and new_mother)):
        recommendations.append("Breastfeeding: Primary Care Interventions -- Pregnant women, new mothers, and their children")
    if sex == 'female':
        recommendations.append("Chlamydia and Gonorrhea: Screening -- Sexually active women, including pregnant persons")
    if age is not None and (age >= 45 and age <= 49):
        recommendations.append("Colorectal Cancer: Screening -- Adults aged 45 to 49 years")
    if age is not None and (age >= 8 and age <= 18):
        recommendations.append("Anxiety in Children and Adolescents: Screening -- Children and adolescents aged 8 to 18 years")
    if (sex == 'pregnant' or (pregnant is not None and pregnant)):
        recommendations.append("Aspirin Use to Prevent Preeclampsia and Related Morbidity and Mortality: Preventive Medication -- Pregnant persons at high risk for preeclampsia")
    if sex == 'pregnant':
        recommendations.append("Asymptomatic Bacteriuria in Adults: Screening -- Pregnant persons")
    if sex == 'male' and (ancestry is not None and ancestry == 'BRCA1/2 gene mutation'):
        recommendations.append("BRCA-Related Cancer: Risk Assessment, Genetic Counseling, and Genetic Testing -- Men with a personal or family history of breast, ovarian, tubal, or peritoneal cancer or an ancestry associated with BRCA1/2 gene mutation")
    if sex == 'male' and age >= 65 and (pack_years is not None and pack_years > 0):
        recommendations.append("Abdominal Aortic Aneurysm: Screening -- Men aged 65 to 75 years who have ever smoked")
    if age is not None and (age >= 12 and age <= 18):
        recommendations.append("Depression and Suicide Risk in Children and Adolescents: Screening -- Adolescents aged 12 to 18 years")
    if age is not None and (age >= 65):
        recommendations.append("Falls Prevention in Community-Dwelling Older Adults: Interventions -- Adults 65 years or older")
    if (sex == 'pregnant' or (pregnant is not None and pregnant)) and (age is not None and (age >= 24)):
        recommendations.append("Gestational Diabetes: Screening -- Asymptomatic pregnant persons at 24 weeks of gestation or after")
    if overweight_or_obesity is not None:
        recommendations.append("Healthy Diet and Physical Activity for Cardiovascular Disease Prevention in Adults With Cardiovascular Risk Factors: Behavioral Counseling Interventions -- Adults with cardiovascular disease risk factors")
    if (sex == 'pregnant' or (pregnant is not None and pregnant)):
        recommendations.append("Healthy Weight and Weight Gain In Pregnancy: Behavioral Counseling Interventions -- Pregnant persons")
    if sex == 'female' and (age is not None and (age >= 18)):
        recommendations.append("Hepatitis B Virus Infection in Adolescents and Adults: Screening -- Adolescents and adults at increased risk for infection")
    if sex == 'male' and (age is not None and (age >= 18 and age <= 79)):
        recommendations.append("Hepatitis C Virus Infection in Adolescents and Adults: Screening -- Adults aged 18 to 79 years")
    if sex == 'female' and (age is not None and (age >= 14)):
        recommendations.append("Intimate Partner Violence, Elder Abuse, and Abuse of Vulnerable Adults: Screening -- Women of reproductive age")
    if age is not None and (age >= 6 and age <= 60):
        recommendations.append("Latent Tuberculosis Infection in Adults: Screening -- Asymptomatic adults at increased risk of latent tuberculosis infection (LTBI)")
    if (sex == 'male' or (sex == 'female' and (pregnant is not None and pregnant))) and (age is not None and (age >= 50 and age <= 80) and (pack_years is not None and pack_years >= 20) and (smoking is not None and smoking)):
        recommendations.append("Lung Cancer: Screening -- Adults aged 50 to 80 years who have a 20 pack-year smoking history and currently smoke or have quit within the past 15 years")
    if age is not None and (age >= 6 and age <= 18):
        recommendations.append("Obesity in Children and Adolescents: Screening -- Children and adolescents 6 years and older")
    if sex == 'female' and (age is not None and (age < 65)):
        recommendations.append("Osteoporosis to Prevent Fractures: Screening -- Postmenopausal women younger than 65 years at increased risk of osteoporosis")
    if sex == 'female' and (age is not None and (age >= 65)):
        recommendations.append("Osteoporosis to Prevent Fractures: Screening -- Women 65 years and older")
    if (sex == 'pregnant' or (pregnant is not None and pregnant) or (new_mother is not None and new_mother)):
        recommendations.append("Perinatal Depression: Preventive Interventions -- Pregnant and postpartum persons")
    if age is not None and (age >= 35 and age <= 70) and (overweight_or_obesity is not None and overweight_or_obesity):
        recommendations.append("Prediabetes and Type 2 Diabetes: Screening -- Asymptomatic adults aged 35 to 70 years who have overweight or obesity")
    if (sex == 'pregnant' or (pregnant is not None and pregnant)):
        recommendations.append("Preeclampsia: Screening -- Pregnant woman")
    if age is not None and (age < 5):
        recommendations.append("Prevention of Dental Caries in Children Younger Than 5 Years: Screening and Interventions -- Children younger than 5 years")
    if (sex == 'pregnant' or (pregnant is not None and pregnant)) or (new_mother is not None and new_mother):
        recommendations.append("Prevention of Dental Caries in Children Younger Than 5 Years: Screening and Interventions -- Children younger than 5 years")
    if (sex == 'pregnant' or (pregnant is not None and pregnant)) and (rh_d_negative is not None and not rh_d_negative):
        recommendations.append("Rh(D) Incompatibility: Screening -- Unsensitized Rh(D)-negative pregnant women")
    if sex == 'male' or (sex == 'female' and (pregnant is not None and pregnant) or (new_mother is not None and new_mother)):
        recommendations.append("Screening for Depression in Adults -- General adult population, including pregnant and postpartum women")
    if sex == 'male' or (sex == 'female' and (pregnant is not None and pregnant)) or (new_mother is not None and new_mother):
        recommendations.append("Sexually Transmitted Infections: Behavioral Counseling -- Sexually active adolescents and adults at increased risk")
    if (age is not None and (age >= 25)) or (new_mother is not None and new_mother) or (sex == 'male' and (substance_abuse_risk is not None and substance_abuse_risk)):
        recommendations.append("Skin Cancer Prevention: Behavioral Counseling -- Young adults, adolescents, children, and parents of young children")
    if (age is not None and (age >= 40 and age <= 75)) and (cardiovascular_risk is not None and cardiovascular_risk) and (cardiovascular_risk_7_5_to_10 is None or not cardiovascular_risk_7_5_to_10):
        recommendations.append("Statin Use for the Primary Prevention of Cardiovascular Disease in Adults: Preventive Medication -- Adults aged 40 to 75 years who have 1 or more cardiovascular risk factors and an estimated 10-year cardiovascular disease (CVD) risk of 10% or greater")
    if sex == 'female' and (pregnant is not None and pregnant) and (ancestry is not None and ancestry == 'BRCA1/2 gene mutation'):
        recommendations.append("BRCA-Related Cancer: Risk Assessment, Genetic Counseling, and Genetic Testing -- Women with a personal or family history of breast, ovarian, tubal, or peritoneal cancer or an ancestry associated with BRCA1/2 gene mutation")
    if (age is not None and (age >= 6 and age <= 18)) or (sex == 'pregnant' or (pregnant is not None and pregnant)):
        recommendations.append("Tobacco Use in Children and Adolescents: Primary Care Interventions -- School-aged children and adolescents who have not started to use tobacco")
    if age is not None and (age >= 18) and (substance_abuse_risk is not None and substance_abuse_risk):
        recommendations.append("Unhealthy Alcohol Use in Adolescents and Adults: Screening and Behavioral Counseling Interventions -- Adults 18 years or older, including pregnant women")
    if age is not None and (age >= 18):
        recommendations.append("Unhealthy Drug Use: Screening -- Adults age 18 years or older")
    if age is not None and (age >= 18):
        recommendations.append("Unhealthy Drug Use: Screening -- Adolescents age 12 to 17 years")
    if age is not None and (age >= 18) and (substance_abuse_risk is not None and substance_abuse_risk):
        recommendations.append("Unhealthy Drug Use: Screening -- Pregnant persons")
    if skin_type is not None:
        recommendations.append("Skin Cancer: Counseling -- Fair-skinned individuals aged 6 months to 24 years with a family history of skin cancer or personal history of skin cancer, or who are at increased risk of skin cancer")
    return recommendations


# Getting user inputs
age = int(input("Enter your age: "))
sex = input("Enter your sex (male/female): ")

# Generating recommendations
recommendations = get_recommendations(age, sex)

# Printing recommendations
print("Recommended screenings/interventions:")
for recommendation in recommendations:
    print("- " + recommendation)

