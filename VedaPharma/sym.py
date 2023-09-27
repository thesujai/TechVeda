import streamlit as st
from data.symptoms import symptoms
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from urllib.parse import urlencode


ayurvedic_cures = {
    'Fungal infection': [
        '1. Neem leaves: Make a paste of neem leaves and apply it to the affected area.',
        '2. Turmeric: Mix turmeric powder with water to make a paste and apply it to the infection.',
        '3. Aloe vera: Apply aloe vera gel to the affected skin for its soothing properties.'
    ],
    'Allergy': [
        '1. Triphala powder: Mix triphala powder in water and consume it to detoxify the body.',
        '2. Honey and cinnamon: Mix honey and cinnamon powder and consume it to reduce allergies.',
        '3. Neti pot: Use a neti pot with saline solution for nasal allergies.'
        
        
    ],
     
    'GERD': [
        '1. Amla (Indian gooseberry): Consume amla juice to reduce acidity.',
        '2. Ginger tea: Prepare ginger tea to soothe the digestive system.',
        '3. Licorice (mulethi): Chew on licorice root or consume licorice tea.'
    ],
    'Chronic cholestasis': [
        '1. Kutki (Picrorhiza kurroa): Consume kutki powder with water for liver health.',
        '2. Bhringraj (Eclipta prostrata): Make a paste of bhringraj leaves and consume it for liver support.',
        '3. Triphala: Consume triphala churna with warm water for detoxification.'
    ],
    'Drug Reaction': [
        '1. Sandalwood paste: Apply sandalwood paste to soothe skin irritation.',
        '2. Aloe vera gel: Apply aloe vera gel to the affected area for its cooling properties.',
        '3. Coconut oil: Apply coconut oil to moisturize and heal the skin.'
    ],
    'Peptic ulcer disease': [
        '1. Licorice (mulethi): Chew on licorice root or consume licorice tea.',
        '2. Cold milk: Drink cold milk to soothe the stomach lining.',
        '3. Basil leaves: Chew on basil leaves for relief from ulcers.'
    ],
    'AIDS': [
        '1. Ashwagandha (Withania somnifera): Consume ashwagandha for immune system support.',
        '2. Tulsi (Holy Basil): Consume tulsi leaves for their immune-boosting properties.',
        '3. Triphala: Use triphala churna with warm water for detoxification.'
    ],
    'Diabetes': [
        '1. Bitter gourd (karela): Consume bitter gourd juice to manage blood sugar levels.',
        '2. Fenugreek (methi): Soak fenugreek seeds overnight and consume them in the morning.',
        '3. Cinnamon: Add cinnamon to your diet for its potential blood sugar benefits.'
    ],
    'Gastroenteritis': [
        '1. Ginger tea: Prepare ginger tea to soothe the digestive system.',
        '2. Pomegranate juice: Drink pomegranate juice for its astringent properties.',
        '3. Coconut water: Drink coconut water to stay hydrated and replenish electrolytes.'
    ],
    'Bronchial Asthma': [
        '1. Vasaka (Adhatoda vasica): Consume vasaka leaves for respiratory health.',
        '2. Ginger and honey: Mix ginger juice and honey and consume it for respiratory relief.',
        '3. Eucalyptus oil: Inhale eucalyptus oil vapor for congestion relief.'
    ],
    'Hypertension': [
        '1. Garlic: Consume raw garlic for its potential blood pressure-lowering properties.',
        '2. Arjuna (Terminalia arjuna): Use arjuna bark powder to support heart health.',
        '3. Yoga and meditation: Practice stress-reduction techniques.'
    ],
    'Migraine': [
        '1. Peppermint oil: Apply diluted peppermint oil to your temples for headache relief.',
        '2. Ginger tea: Prepare ginger tea to reduce migraine symptoms.',
        '3. Stay hydrated: Dehydration can trigger migraines, so drink plenty of water.'
    ],
    'Cervical spondylosis': [
        '1. Ashwagandha (Withania somnifera): Consume ashwagandha for its anti-inflammatory properties.',
        '2. Guggul (Commiphora wightii): Take guggul supplements for joint health.',
        '3. Gentle neck exercises: Practice neck stretches and exercises to improve mobility.'
    ],
    'Paralysis (brain hemorrhage)': [
        '1. Brahmi (Bacopa monnieri): Consume brahmi for brain health and cognitive support.',
        '2. Ashwagandha (Withania somnifera): Use ashwagandha for overall strength and vitality.',
        '3. Physical therapy: Work with a physical therapist for rehabilitation.'
    ],
    'Jaundice': [
        '1. Bhumyamalaki (Phyllanthus niruri): Consume bhumyamalaki for liver support.',
        '2. Turmeric milk: Drink turmeric milk for its detoxifying properties.',
        '3. Papaya leaves: Make a juice from papaya leaves to boost platelet count.'
    ],
    'Malaria': [
        '1. Giloy (Tinospora cordifolia): Consume giloy for its immune-boosting properties.',
        '2. Andrographis paniculata: Use andrographis supplements for fever reduction.',
        '3. Rest and hydration: Get plenty of rest and stay hydrated during recovery.'
    ],
    'Chicken pox': [
        '1. Neem leaves: Add neem leaves to your bathwater to relieve itching.',
        '2. Oatmeal bath: Take an oatmeal bath to soothe skin irritation.',
        '3. Cooling herbs: Consume cooling herbs like coriander and mint for relief.'
    ],
    'Dengue': [
        '1. Papaya leaf extract: Drink papaya leaf extract to increase platelet count.',
        '2. Barley grass juice: Consume barley grass juice for immune support.',
        '3. Stay hydrated: Drink plenty of fluids to prevent dehydration.'
    ],
    'Typhoid': [
        '1. Basil leaves: Chew on basil leaves for their antibacterial properties.',
        '2. Guava leaves: Boil guava leaves and drink the solution for fever reduction.',
        '3. Fluids and rest: Stay well-hydrated and get plenty of rest during recovery.'
    ],
    'Hepatitis A': [
        '1. Bhringaraj (Eclipta prostrata): Consume bhringaraj for liver health.',
        '2. Kutki (Picrorhiza kurroa): Take kutki supplements for liver support.',
        '3. Diet modification: Follow a healthy, easily digestible diet.'
    ],
    'Hepatitis B': [
        '1. Milk thistle (Silybum marianum): Use milk thistle supplements for liver support.',
        '2. Echinacea: Consume echinacea for immune system support.',
        '3. Rest and hydration: Get plenty of rest and stay well-hydrated.'
    ],
    'Hepatitis C': [
        '1. Phyllanthus amarus: Consume phyllanthus amarus for liver health.',
        '2. Licorice (mulethi): Chew on licorice root or consume licorice tea.',
        '3. Antiviral herbs: Consult with an Ayurvedic practitioner for antiviral herbs.'
    ],
    'Hepatitis D': [
        '1. Eclipta alba: Consume eclipta alba for liver support.',
        '2. Amla (Indian gooseberry): Consume amla for its detoxifying properties.',
        '3. Diet modification: Follow a healthy, easily digestible diet.'
    ],
    'Hepatitis E': [
        '1. Kutki (Picrorhiza kurroa): Take kutki supplements for liver support.',
        '2. Bitter gourd (karela): Consume bitter gourd for liver health.',
        '3. Hydration: Stay well-hydrated during recovery.'
    ],
    'Alcoholic hepatitis': [
        '1. Dandelion root: Consume dandelion root tea for liver detoxification.',
        '2. Kutki (Picrorhiza kurroa): Take kutki supplements for liver support.',
        '3. Abstinence: Avoid alcohol completely to support liver healing.'
    ],
    'Tuberculosis': [
        '1. Triphala: Consume triphala churna with warm water for detoxification.',
        '2. Ashwagandha (Withania somnifera): Consume ashwagandha for immune support.',
        '3. Ginger tea: Prepare ginger tea for respiratory relief.'
    ],
    'Common Cold': [
        '1. Ginger and honey: Mix ginger juice and honey and consume it for relief from cold symptoms.',
        '2. Tulsi (Holy Basil): Consume tulsi tea for its immune-boosting properties.',
        '3. Steam inhalation: Inhale steam with a few drops of eucalyptus oil for congestion relief.'
    ],
    'Pneumonia': [
        '1. Vasaka (Adhatoda vasica): Consume vasaka leaves for respiratory health.',
        '2. Turmeric milk: Drink turmeric milk for its anti-inflammatory properties.',
        '3. Rest and hydration: Get plenty of rest and stay well-hydrated during recovery.'
    ],
    'Dimorphic hemorrhoids (piles)': [
        '1. Triphala: Consume triphala churna with warm water for digestive health.',
        '2. Buttermilk: Drink buttermilk with rock salt for relief from hemorrhoids.',
        '3. Sitz bath: Take a sitz bath with warm water for comfort.'
    ],
    'Heartattack': [
        '1. Arjuna (Terminalia arjuna): Consume arjuna bark powder for heart health.',
        '2. Garlic: Consume raw garlic for potential cardiovascular benefits.',
        '3. Yoga and meditation: Practice stress-reduction techniques.'
    ],
    'Varicoseveins': [
        '1. Horse Chestnut (Aesculus hippocastanum): Use horse chestnut extract for vein health.',
        '2. Gotu Kola (Centella asiatica): Consume gotu kola for circulatory support.',
        '3. Leg elevation: Elevate your legs to reduce swelling.'
    ],
    'Hypothyroidism': [
        '1. Ashwagandha (Withania somnifera): Consume ashwagandha for thyroid support.',
        '2. Guggul (Commiphora wightii): Take guggul supplements for thyroid health.',
        '3. Iodine-rich foods: Include iodine-rich foods like seaweed in your diet.'
    ],
    'Hyperthyroidism': [
        '1. Bugleweed (Lycopus virginicus): Consume bugleweed for thyroid support.',
        '2. Stress reduction: Practice stress management techniques like yoga and meditation.',
        '3. Cooling foods: Include cooling and calming foods in your diet.'
    ],
    'Hypoglycemia': [
        '1. Amla (Indian gooseberry): Consume amla juice to stabilize blood sugar levels.',
        '2. Cinnamon: Add cinnamon to your diet for its potential blood sugar benefits.',
        '3. Frequent small meals: Eat small, balanced meals throughout the day.'
    ],
    'Osteoarthritis': [
        '1. Turmeric: Include turmeric in your diet for its anti-inflammatory properties.',
        '2. Ginger tea: Prepare ginger tea to soothe joint pain.',
        '3. Warm compress: Apply a warm compress to affected joints for relief.'
    ],
    'Arthritis': [
        '1. Triphala: Consume triphala churna with warm water for digestive health.',
        '2. Boswellia (Indian frankincense): Use boswellia supplements for joint support.',
        '3. Gentle exercise: Engage in gentle exercises like yoga for joint flexibility.'
    ],
    '(vertigo) Paroxysmal Positional Vertigo': [
        '1. Epley maneuver: Perform the Epley maneuver to reposition ear crystals.',
        '2. Gingko biloba: Use gingko biloba supplements for improved circulation.',
        '3. Avoid sudden movements: Minimize sudden head movements.'
    ],
    'Acne': [
        '1. Neem leaves: Make a paste of neem leaves and apply it to acne-prone areas.',
        '2. Aloe vera gel: Apply aloe vera gel to acne scars for skin healing.',
        '3. Turmeric and honey mask: Mix turmeric and honey to create a natural face mask.'
    ],
    'Urinary tract infection': [
        '1. Cranberry juice: Drink unsweetened cranberry juice for urinary tract health.',
        '2. Coriander seeds: Boil coriander seeds and drink the solution for relief.',
        '3. Hydration: Stay well-hydrated to flush out bacteria.'
    ],
    'Psoriasis': [
        '1. Aloe vera gel: Apply aloe vera gel to psoriasis-affected skin for its soothing properties.',
        '2. Turmeric and honey paste: Mix turmeric and honey to create a skin paste.',
        '3. Dead Sea salt bath: Soak in a bath with Dead Sea salt to relieve symptoms.'
    ],
    'Impetigo': [
        '1. Tea tree oil: Apply diluted tea tree oil to impetigo sores for its antibacterial properties.',
        '2. Goldenseal (Hydrastis canadensis): Use goldenseal ointment for skin infections.',
        '3. Keep the area clean: Practice good hygiene to prevent the spread of impetigo.'
    ]
}


disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
           'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
           'Migraine', 'Cervical spondylosis', 'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria',
           'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D',
           'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia',
           'Dimorphic hemmorhoids(piles)', 'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism',
           'Hypoglycemia', 'Osteoarthristis', 'Arthritis', '(vertigo) Paroymsal Positional Vertigo', 'Acne',
           'Urinary tract infection', 'Psoriasis', 'Impetigo']


tr = pd.read_csv("Testing.csv")
tr.replace({'prognosis': {1: 'Fungal infection', 2: 'Allergy', 3: 'GERD', 4: 'Chronic cholestasis', 5: 'Drug Reaction',
                          6: 'Peptic ulcer diseae', 7: 'AIDS', 8: 'Diabetes', 9: 'Gastroenteritis', 10: 'Bronchial Asthma',
                          11: 'Hypertension', 12: 'Migraine', 13: 'Cervical spondylosis', 14: 'Paralysis (brain hemorrhage)',
                          15: 'Jaundice', 16: 'Malaria', 17: 'Chicken pox', 18: 'Dengue', 19: 'Typhoid', 20: 'hepatitis A',
                          21: 'Hepatitis B', 22: 'Hepatitis C', 23: 'Hepatitis D', 24: 'Hepatitis E', 25: 'Alcoholic hepatitis',
                          26: 'Tuberculosis', 27: 'Common Cold', 28: 'Pneumonia', 29: 'Dimorphic hemmorhoids(piles)',
                          30: 'Heartattack', 31: 'Varicoseveins', 32: 'Hypothyroidism', 33: 'Hyperthyroidism', 34: 'Hypoglycemia',
                          35: 'Osteoarthristis', 36: 'Arthritis', 37: '(vertigo) Paroymsal Positional Vertigo', 38: 'Acne',
                          39: 'Urinary tract infection', 40: 'Psoriasis', 41: 'Impetigo'}}, inplace=True)


df = pd.read_csv("Training.csv")
df.replace({'prognosis': {1: 'Fungal infection', 2: 'Allergy', 3: 'GERD', 4: 'Chronic cholestasis', 5: 'Drug Reaction',
                         6: 'Peptic ulcer diseae', 7: 'AIDS', 8: 'Diabetes', 9: 'Gastroenteritis', 10: 'Bronchial Asthma',
                         11: 'Hypertension', 12: 'Migraine', 13: 'Cervical spondylosis', 14: 'Paralysis (brain hemorrhage)',
                         15: 'Jaundice', 16: 'Malaria', 17: 'Chicken pox', 18: 'Dengue', 19: 'Typhoid', 20: 'hepatitis A',
                         21: 'Hepatitis B', 22: 'Hepatitis C', 23: 'Hepatitis D', 24: 'Hepatitis E', 25: 'Alcoholic hepatitis',
                         26: 'Tuberculosis', 27: 'Common Cold', 28: 'Pneumonia', 29: 'Dimorphic hemmorhoids(piles)',
                         30: 'Heartattack', 31: 'Varicoseveins', 32: 'Hypothyroidism', 33: 'Hyperthyroidism', 34: 'Hypoglycemia',
                         35: 'Osteoarthristis', 36: 'Arthritis', 37: '(vertigo) Paroymsal Positional Vertigo', 38: 'Acne',
                         39: 'Urinary tract infection', 40: 'Psoriasis', 41: 'Impetigo'}}, inplace=True)


data = {'disease': 'No result yet'}


def NaiveBayes(symptom1, symptom2, symptom3, symptom4, symptom5):

    X_train = df[symptoms]
    y_train = df[["prognosis"]]
    X_test = tr[symptoms]
    y_test = tr[["prognosis"]]


    gnb = MultinomialNB()
    gnb.fit(X_train, np.ravel(y_train))

    
    psymptoms = [symptom1, symptom2, symptom3, symptom4, symptom5]
    l2 = [0] * len(symptoms)

    for k in range(0, len(symptoms)):
        for z in psymptoms:
            if z == symptoms[k]:
                l2[k] = 1

    inputtest = [l2]
    predicted_disease_name = gnb.predict(inputtest)[0]  

    return predicted_disease_name 






def mainFunc():
    st.title("Disease Prediction App")

    
    symptom1 = st.selectbox("Symptom 1", ["Select a Symptom"] + symptoms)
    symptom2 = st.selectbox("Symptom 2", ["Select a Symptom"] + symptoms)
    symptom3 = st.selectbox("Symptom 3", ["Select a Symptom"] + symptoms)
    symptom4 = st.selectbox("Symptom 4", ["Select a Symptom"] + symptoms)
    symptom5 = st.selectbox("Symptom 5", ["Select a Symptom"] + symptoms)

    if st.button("Submit"):
        
        print(f"printed:{symptom1}")

        predicted_disease = NaiveBayes(symptom1, symptom2, symptom3, symptom4, symptom5)

        
        data['disease'] = predicted_disease

    
    st.write(f"Predicted Disease: {data['disease']}")
    st.write(f'Ayurvedic Cure:')
    l=ayurvedic_cures[data['disease']]
    for i in l:
        i_parts = i.split(":", 1)
        searchUrl=urlencode({"q":{i_parts[0]}})
        st.markdown(f"{i}(https://www.google.com/search?q={searchUrl})")


