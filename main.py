import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu
from explore import show_data_frame, rfa
from PIL import Image
import pandas as pd

def show_predict_page():
    with st.sidebar:
        selected = option_menu(
            menu_title = '',
            options=['Home','Predict','Explore','Team'],
            icons=['house','book','meta','people'] ,
            menu_icon='cast',
            default_index=0,
            orientation='horizontal',          
        )
    
    if selected == 'Home':
        home()
    if selected == 'Predict':
        predict_page()
    if selected == 'Explore':
        explore()
    if selected == 'Team':
        team()

def home():
    st.write("This website  is to predict the price of  new  cars based on various features.")

    st.title('Prediction Accuracy')
    st.write('')
    st.write()

    rfa()
def predict_page():
    st.title('Enter & Predict!')

    model = pickle.load(open('carpricemodel.pkl', 'rb'))

    make_array = ['BMW', 'Audi', 'FIAT', 'Mercedes-Benz', 'Chrysler', 'Nissan',
       'Volvo', 'Mazda', 'Mitsubishi', 'Ferrari', 'Alfa Romeo', 'Toyota',
       'McLaren', 'Maybach', 'Pontiac', 'Porsche', 'Saab', 'GMC',
       'Hyundai', 'Plymouth', 'Honda', 'Oldsmobile', 'Suzuki', 'Ford',
       'Cadillac', 'Kia', 'Bentley', 'Chevrolet', 'Dodge', 'Lamborghini',
       'Lincoln', 'Subaru', 'Volkswagen', 'Spyker', 'Buick', 'Acura',
       'Rolls-Royce', 'Maserati', 'Lexus', 'Aston Martin', 'Land Rover',
       'Lotus', 'Infiniti', 'Scion', 'Genesis', 'HUMMER', 'Tesla',
       'Bugatti']
    model_array = ['1 Series M', '1 Series', '100', '124 Spider', '190-Class',
       '2 Series', '200', '200SX', '240SX', '240', '2',
       '3 Series Gran Turismo', '3 Series', '300-Class', '3000GT', '300',
       '300M', '300ZX', '323', '350-Class', '350Z', '360', '370Z', '3',
       '4 Series Gran Coupe', '4 Series', '400-Class', '420-Class',
       '456M', '458 Italia', '4C', '4Runner', '5 Series Gran Turismo',
       '5 Series', '500-Class', '500e', '500', '500L', '500X', '550',
       '560-Class', '570S', '575M', '57', '599', '5',
       '6 Series Gran Coupe', '6 Series', '600-Class', '6000',
       '612 Scaglietti', '626', '62', '650S Coupe', '650S Spider', '6',
       '7 Series', '718 Cayman', '740', '760', '780', '8 Series', '80',
       '850', '86', '9-2X', '9-3 Griffin', '9-3', '9-4X', '9-5', '9-7X',
       '9000', '900', '90', '911', '928', '929', '940', '944', '960',
       '968', 'A3', 'A4 allroad', 'A4', 'A5', 'A6', 'A7', 'A8',
       'Acadia Limited', 'Acadia', 'Accent', 'Acclaim',
       'Accord Crosstour', 'Accord Hybrid', 'Accord Plug-In Hybrid',
       'Accord', 'Achieva', 'ActiveHybrid 5', 'ActiveHybrid 7',
       'ActiveHybrid X6', 'Aerio', 'Aerostar', 'Alero', 'Allante',
       'allroad quattro', 'allroad', 'ALPINA B6 Gran Coupe', 'ALPINA B7',
       'Alpina', 'Altima Hybrid', 'Altima', 'Amanti', 'AMG GT', 'Armada',
       'Arnage', 'Aspen', 'Aspire', 'Astro Cargo', 'Astro', 'ATS Coupe',
       'ATS-V', 'ATS', 'Aurora', 'Avalanche', 'Avalon Hybrid', 'Avalon',
       'Avenger', 'Aventador', 'Aveo', 'Aviator', 'Axxess', 'Azera',
       'Aztek', 'Azure T', 'Azure', 'B-Class Electric Drive',
       'B-Series Pickup', 'B-Series Truck', 'B-Series', 'B9 Tribeca',
       'Baja', 'Beetle Convertible', 'Beetle', 'Beretta',
       'Black Diamond Avalanche', 'Blackwood', 'Blazer', 'Bolt EV',
       'Bonneville', 'Borrego', 'Boxster', 'Bravada', 'Breeze',
       'Bronco II', 'Bronco', 'Brooklands', 'Brougham', 'BRZ', 'C-Class',
       'C-Max Hybrid', 'C30', 'C36 AMG', 'C43 AMG', 'C70', 'C8',
       'Cabriolet', 'Cabrio', 'Cadenza', 'Caliber', 'California T',
       'California', 'Camaro', 'Camry Hybrid', 'Camry Solara', 'Camry',
       'Canyon', 'Caprice', 'Captiva Sport', 'Caravan', 'Carrera GT',
       'Cascada', 'Catera', 'Cavalier', 'Cayenne', 'Cayman S', 'Cayman',
       'CC', 'Celebrity', 'Celica', 'Century', 'Challenger', 'Charger',
       'Chevy Van', 'Ciera', 'Cirrus', 'City Express', 'Civic CRX',
       'Civic del Sol', 'Civic', 'C/K 1500 Series', 'C/K 2500 Series',
       'CL-Class', 'CLA-Class', 'CL', 'Classic', 'CLK-Class', 'CLS-Class',
       'Cobalt', 'Colorado', 'Colt', 'Concorde',
       'Continental Flying Spur Speed', 'Continental Flying Spur',
       'Continental GT Speed Convertible', 'Continental GT Speed',
       'Continental GT3-R', 'Continental GT', 'Continental GTC Speed',
       'Continental GTC', 'Continental Supersports Convertible',
       'Continental Supersports', 'Continental', 'Contour SVT', 'Contour',
       'Corniche', 'Corolla iM', 'Corolla', 'Corrado', 'Corsica',
       'Corvette Stingray', 'Corvette', 'Coupe', 'CR-V', 'CR-Z',
       'Cressida', 'Crossfire', 'Crosstour', 'Crosstrek',
       'Crown Victoria', 'Cruze Limited', 'Cruze', 'CT 200h', 'CT6',
       'CTS Coupe', 'CTS-V Coupe', 'CTS-V Wagon', 'CTS-V', 'CTS Wagon',
       'CTS', 'Cube', 'Custom Cruiser', 'Cutlass Calais', 'Cutlass Ciera',
       'Cutlass Supreme', 'Cutlass', 'CX-3', 'CX-5', 'CX-7', 'CX-9',
       'Dakota', 'Dart', 'Dawn', 'Daytona', 'DB7', 'DB9 GT', 'DB9', 'DBS',
       'Defender', 'DeVille', 'Diablo', 'Diamante', 'Discovery Series II',
       'Discovery Sport', 'Discovery', 'DTS', 'Durango', 'Dynasty',
       'E-150', 'E-250', 'E-Class', 'e-Golf', 'E-Series Van',
       'E-Series Wagon', 'E55 AMG', 'ECHO', 'Eclipse Spyder', 'Eclipse',
       'Edge', 'Eighty-Eight Royale', 'Eighty-Eight', 'Elantra Coupe',
       'Elantra GT', 'Elantra Touring', 'Elantra', 'Eldorado', 'Electra',
       'Element', 'Elise', 'Enclave', 'Encore', 'Endeavor', 'Entourage',
       'Envision', 'Envoy XL', 'Envoy XUV', 'Envoy', 'Enzo', 'Eos',
       'Equator', 'Equinox', 'Equus', 'ES 250', 'ES 300h', 'ES 300',
       'ES 330', 'ES 350', 'Escalade ESV', 'Escalade EXT',
       'Escalade Hybrid', 'Escalade', 'Escape Hybrid', 'Escape', 'Escort',
       'Esprit', 'Estate Wagon', 'Esteem', 'EuroVan', 'Evora 400',
       'Evora', 'EX35', 'Excel', 'Exige', 'EX', 'Expedition',
       'Explorer Sport Trac', 'Explorer Sport', 'Explorer', 'Expo',
       'Express Cargo', 'Express', 'F-150 Heritage',
       'F-150 SVT Lightning', 'F-150', 'F-250', 'F12 Berlinetta', 'F430',
       'Festiva', 'FF', 'Fiesta', 'Firebird', 'Fit EV', 'Fit',
       'Five Hundred', 'FJ Cruiser', 'Fleetwood', 'Flex', 'Flying Spur',
       'Focus RS', 'Focus ST', 'Focus', 'Forenza', 'Forester', 'Forte',
       'Fox', 'FR-S', 'Freelander', 'Freestar', 'Freestyle', 'Frontier',
       'Fusion Hybrid', 'Fusion', 'FX35', 'FX45', 'FX50', 'FX', 'G-Class',
       'G Convertible', 'G Coupe', 'G Sedan', 'G20', 'G35',
       'G37 Convertible', 'G37 Coupe', 'G37 Sedan', 'G37', 'G3', 'G5',
       'G6', 'G80', 'G8', 'Galant', 'Gallardo', 'Genesis Coupe',
       'Genesis', 'Ghibli', 'Ghost Series II', 'Ghost', 'GL-Class',
       'GLA-Class', 'GLC-Class', 'GLE-Class Coupe', 'GLE-Class', 'GLI',
       'GLK-Class', 'GLS-Class', 'Golf Alltrack', 'Golf GTI', 'Golf R',
       'Golf SportWagen', 'Golf', 'Grand Am', 'Grand Caravan',
       'Grand Prix', 'Grand Vitara', 'Grand Voyager', 'GranSport',
       'GranTurismo Convertible', 'GranTurismo', 'GS 200t', 'GS 300',
       'GS 350', 'GS 400', 'GS 430', 'GS 450h', 'GS 460', 'GS F', 'GT-R',
       'GT', 'GTI', 'GTO', 'GX 460', 'GX 470', 'H3', 'H3T', 'HHR',
       'Highlander Hybrid', 'Highlander', 'Horizon', 'HR-V', 'HS 250h',
       'Huracan', 'i-MiEV', 'I30', 'I35', 'i3', 'iA', 'ILX Hybrid', 'ILX',
       'Impala Limited', 'Impala', 'Imperial', 'Impreza WRX', 'Impreza',
       'iM', 'Insight', 'Integra', 'Intrepid', 'Intrigue', 'iQ',
       'IS 200t', 'IS 250 C', 'IS 250', 'IS 300', 'IS 350 C', 'IS 350',
       'IS F', 'J30', 'Jetta GLI', 'Jetta Hybrid', 'Jetta SportWagen',
       'Jetta', 'Jimmy', 'Journey', 'Juke', 'Justy', 'JX', 'K900',
       'Kizashi', 'LaCrosse', 'Lancer Evolution', 'Lancer Sportback',
       'Lancer', 'Land Cruiser', 'Landaulet', 'Laser', 'Le Baron',
       'Le Mans', 'Leaf', 'Legacy', 'Legend', 'LeSabre', 'Levante', 'LFA',
       'LHS', 'Loyale', 'LR2', 'LR3', 'LR4', 'LS 400', 'LS 430', 'LS 460',
       'LS 600h L', 'LS', 'LSS', 'LTD Crown Victoria', 'Lucerne',
       'Lumina Minivan', 'Lumina', 'LX 450', 'LX 470', 'LX 570',
       'M-Class', 'M2', 'M30', 'M35', 'M37', 'M3', 'M4 GTS', 'M45', 'M4',
       'M56', 'M5', 'M6 Gran Coupe', 'M6', 'Macan', 'Magnum',
       'Malibu Classic', 'Malibu Hybrid', 'Malibu Limited', 'Malibu Maxx',
       'Malibu', 'Mark LT', 'Mark VIII', 'Mark VII', 'Matrix', 'Maxima',
       'Maybach', 'Mazdaspeed 3', 'Mazdaspeed 6', 'Mazdaspeed MX-5 Miata',
       'Mazdaspeed Protege', 'M', 'MDX', 'Metris', 'Metro',
       'Mighty Max Pickup', 'Millenia', 'Mirage G4', 'Mirage', 'MKC',
       'MKS', 'MKT', 'MKX', 'MKZ Hybrid', 'MKZ', 'ML55 AMG', 'Model S',
       'Monaco', 'Montana SV6', 'Montana', 'Monte Carlo', 'Montero Sport',
       'Montero', 'MP4-12C', 'MPV', 'MR2 Spyder', 'MR2', 'Mulsanne',
       'Murano CrossCabriolet', 'Murano', 'Murcielago',
       'Mustang SVT Cobra', 'Mustang', 'MX-3', 'MX-5 Miata', 'MX-6',
       'Navajo', 'Navigator', 'Neon', 'New Beetle', 'New Yorker',
       'Ninety-Eight', 'Nitro', 'NSX', 'NV200', 'NX 200t', 'NX 300h',
       'NX', 'Odyssey', 'Omni', 'Optima Hybrid', 'Optima', 'Outback',
       'Outlander Sport', 'Outlander', 'Pacifica', 'Panamera',
       'Park Avenue', 'Park Ward', 'Paseo', 'Passat', 'Passport',
       'Pathfinder', 'Phaeton', 'Phantom Coupe', 'Phantom Drophead Coupe',
       'Phantom', 'Pickup', 'Pilot', 'Precis', 'Prelude', 'Previa',
       'Prius c', 'Prius Prime', 'Prius v', 'Prius', 'Prizm', 'Probe',
       'Protege5', 'Protege', 'Prowler', 'PT Cruiser', 'Pulsar', 'Q3',
       'Q40', 'Q45', 'Q50', 'Q5', 'Q60 Convertible', 'Q60 Coupe', 'Q70',
       'Q7', 'Quattroporte', 'Quest', 'QX4', 'QX50', 'QX56', 'QX60',
       'QX70', 'QX80', 'QX', 'R-Class', 'R32', 'R8', 'Rabbit', 'Raider',
       'Rainier', 'Rally Wagon', 'RAM 150', 'RAM 250', 'Ram 50 Pickup',
       'Ram Cargo', 'Ram Pickup 1500', 'Ram Van', 'Ram Wagon',
       'Ramcharger', 'Range Rover Evoque', 'Range Rover Sport',
       'Range Rover', 'Ranger', 'Rapide S', 'Rapide', 'RAV4 EV',
       'RAV4 Hybrid', 'RAV4', 'RC 200t', 'RC 300', 'RC 350', 'RC F',
       'RDX', 'Reatta', 'Regal', 'Regency', 'Rendezvous', 'Reno',
       'Reventon', 'Ridgeline', 'Rio', 'Riviera', 'RL', 'RLX',
       'Roadmaster', 'Rogue Select', 'Rogue', 'Rondo', 'Routan', 'RS 4',
       'RS 5', 'RS 6', 'RS 7', 'RSX', 'RX 300', 'RX 330', 'RX 350',
       'RX 400h', 'RX 450h', 'RX-7', 'RX-8', 'S-10 Blazer', 'S-10',
       'S-15 Jimmy', 'S-15', 'S-Class', 'S2000', 'S3', 'S40', 'S4', 'S5',
       'S60 Cross Country', 'S60', 'S6', 'S70', 'S7', 'S80', 'S8', 'S90',
       'Safari Cargo', 'Safari', 'Samurai', 'Santa Fe Sport', 'Santa Fe',
       'Savana Cargo', 'Savana', 'SC 300', 'SC 400', 'SC 430', 'Scoupe',
       'Sebring', 'Sedona', 'Sentra', 'Sephia', 'Sequoia', 'Seville',
       'Shadow', 'Shelby GT350', 'Shelby GT500', 'Sidekick', 'Sienna',
       'Sierra 1500 Classic', 'Sierra 1500 Hybrid', 'Sierra 1500',
       'Sierra 1500HD', 'Sierra C3', 'Sierra Classic 1500', 'Sigma',
       'Silhouette', 'Silver Seraph', 'Silverado 1500 Classic',
       'Silverado 1500 Hybrid', 'Silverado 1500', 'Sixty Special',
       'Skylark', 'SL-Class', 'SLC-Class', 'SLK-Class', 'SLR McLaren',
       'SLS AMG GT Final Edition', 'SLS AMG GT', 'SLS AMG', 'SLX',
       'Solstice', 'Sonata Hybrid', 'Sonata', 'Sonic', 'Sonoma',
       'Sorento', 'Soul EV', 'Soul', 'Spark EV', 'Spark', 'Spectra',
       'Spirit', 'Sportage', 'Sportvan', 'Spyder', 'SQ5', 'SRT Viper',
       'SRX', 'SS', 'SSR', 'Stanza', 'Stealth', 'Stratus', 'STS-V', 'STS',
       'Suburban', 'Sunbird', 'Sundance', 'Sunfire', 'Superamerica',
       'Supersports Convertible ISR', 'Supra', 'SVX', 'Swift', 'SX4',
       'Syclone', 'T100', 'Tacoma', 'Tahoe Hybrid', 'Tahoe Limited/Z71',
       'Tahoe', 'Taurus X', 'Taurus', 'TC', 'tC', 'Tempo', 'Tercel',
       'Terrain', 'Terraza', 'Thunderbird', 'Tiburon', 'Tiguan', 'Titan',
       'TL', 'TLX', 'Toronado', 'Torrent', 'Touareg 2', 'Touareg',
       'Town and Country', 'Town Car', 'Tracker', 'TrailBlazer EXT',
       'TrailBlazer', 'Trans Sport', 'Transit Connect', 'Transit Wagon',
       'Traverse', 'Trax', 'Tribeca', 'Tribute Hybrid', 'Tribute',
       'Truck', 'TSX Sport Wagon', 'TSX', 'TT RS', 'TT', 'TTS', 'Tucson',
       'Tundra', 'Typhoon', 'Uplander', 'V12 Vanquish', 'V12 Vantage S',
       'V12 Vantage', 'V40', 'V50', 'V60 Cross Country', 'V60', 'V70',
       'V8 Vantage', 'V8', 'V90', 'Vanagon', 'Vandura', 'Van', 'Vanquish',
       'Vanwagon', 'Veloster', 'Venture', 'Venza', 'Veracruz', 'Verano',
       'Verona', 'Versa Note', 'Versa', 'Veyron 16.4', 'Vibe', 'Vigor',
       'Viper', 'Virage', 'Vitara', 'Voyager', 'Windstar Cargo',
       'Windstar', 'Wraith', 'WRX', 'X-90', 'X1', 'X3', 'X4', 'X5 M',
       'X5', 'X6 M', 'X6', 'xA', 'xB', 'XC60', 'XC70', 'XC90', 'XC', 'xD',
       'XG300', 'XG350', 'XL-7', 'XL7', 'XLR-V', 'XLR', 'XT5', 'Xterra',
       'XTS', 'XT', 'XV Crosstrek', 'Yaris iA', 'Yaris', 'Yukon Denali',
       'Yukon Hybrid', 'Yukon XL', 'Yukon', 'Z3', 'Z4 M', 'Z4', 'Z8',
       'ZDX', 'Zephyr']
    fueltype_arr =['premium unleaded (required)', 'regular unleaded',
       'premium unleaded (recommended)', 'flex-fuel (unleaded/E85)',
       'diesel', 'electric',
       'flex-fuel (premium unleaded recommended/E85)', 'natural gas',
       'flex-fuel (premium unleaded required/E85)',
       'flex-fuel (unleaded/natural gas)']
    Transmission_Type_array= ['MANUAL', 'AUTOMATIC', 'AUTOMATED_MANUAL', 'DIRECT_DRIVE']
    driven_wheel_aryy =['rear wheel drive', 'front wheel drive', 'all wheel drive','four wheel drive']
    vehicle_size_array=['Compact', 'Midsize', 'Large']
    vehicle_style_array=['Coupe', 'Convertible', 'Sedan', 'Wagon', '4dr Hatchback',
       '2dr Hatchback', '4dr SUV', 'Passenger Minivan', 'Cargo Minivan',
       'Crew Cab Pickup', 'Regular Cab Pickup', 'Extended Cab Pickup',
       '2dr SUV', 'Cargo Van', 'Convertible SUV', 'Passenger Van']
    # location_array_encoded = [5, 6, 7, 9, 0, 1, 2, 3, 4, 8]
    make = st.selectbox("select ",make_array)
    car_model = st.selectbox('select model',model_array)
    fuel_type =st.selectbox('select fuel_type',fueltype_arr)
    engine_hp =st.number_input('engine hp')
    engine_cylinder=st.number_input('engine cylinder')
    tranmission_type =st.selectbox("select the tranmission type",Transmission_Type_array)
    driven_wheel=st.selectbox("select the driven wheel",driven_wheel_aryy)
    # market =st.selectbox("select the market",market_category_arr)
    vehicle_size =st.selectbox("select vehicle size",vehicle_size_array)
    vechicle_style=st.selectbox('select vehicle style',vehicle_style_array)
    highway_MPG =st.number_input("enter highway_mpg")
    city_mpg =st.number_input('enter city_mpg')
    year_array = []
    year_start= 2000
    year_end = 2100
   
    for i in range(year_start, year_end):
        year_array.append(i)
    year = st.selectbox("select year",year_array)

    predict = st.button('Predict')

    if predict:
        input_data = pd.DataFrame(data=[[make,car_model,year,fuel_type,engine_hp,engine_cylinder,tranmission_type,driven_wheel,vehicle_size,vechicle_style,highway_MPG,city_mpg]], columns=['Make', 'Model', 'Year', 'Engine Fuel Type', 'Engine HP',
       'Engine Cylinders', 'Transmission Type', 'Driven_Wheels',
       'Vehicle Size', 'Vehicle Style', 'highway MPG', 'city mpg'])
        result = model.predict(input_data)
        nu =result*81.23
        st.write('Price', nu[0].round(2),'nu')
    

def explore():
    st.title('Data Exploration & Data Visualization')
    exp = st.expander('Dataset')
    with exp:
        st.write('For the datasets we are using kaggle dataset https://www.kaggle.com/CooperUnion/cardataset The collected dataset has 11914 data and  15 columns with columns [Make, Model, Year, Engine Fuel Type, Engine HP,Engine Cylinders, Transmission Type, Driven_Wheels, Number of Doors, Vehicle Size, Vehicle Style, highway MPG, city mpg, Popularity, MSRP]')
        show_data_frame()

    exp = st.expander('Heatmap')
    with exp:
        image = Image.open('assets/1.png')
        st.image(image, 'Heatmap')
    
    exp = st.expander('data visualization')
    with exp:
        image = Image.open('assets/graph.png')
        st.image(image, 'PairPlot')
    


def team():
    st.title('Team Members')

    col1, col2, col3, col4 = st.columns(4)        
    
    with col1:
        image = Image.open('assets/n.png')
        st.image(image, 'Namgyal Wanghchuk')
        # st.write("Team lead")
        
    with col2:
        image = Image.open('assets/c.png')
        st.image(image, 'Chencho Tshering ')

    with col3:
        image = Image.open('assets/p.png')
        st.image(image, 'Phurba Thinley')
        

    with col4:
        image = Image.open('assets/k.png')
        st.image(image, 'Kesang Choden')

