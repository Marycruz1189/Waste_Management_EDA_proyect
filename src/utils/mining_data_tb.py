#that contains the generic 
# functionality related to open, create, read and 
# write ﬁles.

import pandas as pd 
import os 


def read_databases():
    
    """ Function to read the 5 databases """
    import os
    SEP = os.sep
    dir = os.path.dirname
    #global csv_fullpath_gdp
    csv_fullpath_gdp = dir(os.getcwd()) + SEP + "data" + SEP + "PIBcorriente_milesdeeuros.xlsx"
    #global csv_fullpath_d
    csv_fullpath_d = dir(os.getcwd()) + SEP + "data" + SEP + "residuos_gestionados_nuevo.xlsx"
    #global csv_fullpath_popu
    csv_fullpath_popu = dir(os.getcwd()) + SEP + "data" + SEP + "poblacion.xls"
    #global csv_fullpath_c
    csv_fullpath_c = dir(os.getcwd()) + SEP + "data" + SEP + "recogida_residuos.xlsx"
    return csv_fullpath_gdp, csv_fullpath_d, csv_fullpath_popu, csv_fullpath_c
    
if __name__ == '__main__':
    read_databases()



def clean_years(gdp, population):
    to_drop = gdp.iloc[:, 1:11]
    gdp.drop(to_drop, inplace = True , axis= 1 )
    to_drop_1  = ['2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001', '2000', '1999', '1998', '1997', '1996']
    population.drop(to_drop_1, inplace = True , axis= 1 )
    gdp['Comunidad Autónoma'] = gdp['Comunidad Autónoma'].str.upper()
    round(gdp.iloc[:, 2],2)
    population['Comunidad Autónoma'] = population['Comunidad Autónoma'].str.upper()
    return gdp, population


def melt_data(gdp, population):
    import pandas as pd 
    clean_gdp = pd.melt(gdp, id_vars=['Comunidad Autónoma'], 
    value_vars=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018],
    var_name='Año', value_name='PIB').sort_values('Comunidad Autónoma')
    clean_population = pd.melt(population, id_vars=['Comunidad Autónoma'], value_vars=['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', 2018],var_name='Año', value_name='Poblacion').sort_values('Comunidad Autónoma')
    
    
    return clean_gdp, clean_population



def clean_collection(waste_collection):
    import pandas as pd 
    waste_collection = waste_collection.T
    waste_collection.columns = waste_collection.iloc[0]
    waste_collection = waste_collection[1:]
    waste_collection['Año'] = waste_collection.index
    waste_collection['Año_1'] = waste_collection['Año'].str.extract(r'(\d{4})')
    waste_collection = waste_collection.drop(columns=['Año'], axis=1)
    waste_collection.rename(columns={'Año_1':'Año'}, inplace=True)
    cols = waste_collection.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    waste_collection = waste_collection[cols]
    waste_collection = waste_collection.reset_index(drop=True)
    new_names = {' ': 'Comunidad Autónoma', '10.1.1 Residuos domésticos y similares (domésticos y vías públicas)': 'Recoleccion-domésticos y vias', '10.1.2 Residuos domésticos voluminosos mezclados (enseres domésticos)': 'Recoleccion-voluminosos', '06 Residuos metálicos': 'Recoleccion-metálicos', '07.1 Residuos de vidrio': 'Recoleccion-vidrio', '07.2 Residuos de papel y cartón': 'Recoleccion-papel y carton', '07.4 Residuos de plásticos': 'Recoleccion-plasticos', '07.5 Residuos de Madera': 'Recoleccion-madera', '07.6 Residuos textiles': 'Recoleccion-textiles', '08.2 y 08.43 Equipos eléctricos desechados y Componentes de equipos eléctrónicos desechados': 'Recoleccion-eq. electricos', '08.41 Residuos de pilas y acumuladores': 'Recoleccion-pilas', '09. Residuos animales y vegetales': 'Recoleccion-animales', '10.21 Envases mixtos y embalajes mezclados': 'Recoleccion-Envases mixtos', '11 Lodos comunes (secos)': 'lodos', '12 Residuos minerales (incluye residuos de construcción y demolición)': 'Recoleccion-construccion', '18 Otros': 'Recoleccion-otros'}
    waste_collection.rename(columns=new_names, inplace=True)
    waste_collection['Comunidad Autónoma'] = waste_collection['Comunidad Autónoma'].str.upper()
    waste_collection [['Recoleccion-domésticos y vias',
       'Recoleccion-voluminosos', 'Recoleccion-metálicos',
       'Recoleccion-vidrio', 'Recoleccion-papel y carton',
       'Recoleccion-plasticos', 'Recoleccion-madera', 'Recoleccion-textiles',
       'Recoleccion-eq. electricos', 'Recoleccion-pilas',
       'Recoleccion-animales', 'Recoleccion-Envases mixtos', 'lodos',
       'Recoleccion-construccion', 'Recoleccion-otros',
       'TOTAL RESIDUOS MEZCLADOS', 'TOTAL RESIDUOS DE RECOGIDA SEPARADA',
       'TOTAL RESIDUOS']] = waste_collection [['Recoleccion-domésticos y vias',
       'Recoleccion-voluminosos', 'Recoleccion-metálicos',
       'Recoleccion-vidrio', 'Recoleccion-papel y carton',
       'Recoleccion-plasticos', 'Recoleccion-madera', 'Recoleccion-textiles',
       'Recoleccion-eq. electricos', 'Recoleccion-pilas',
       'Recoleccion-animales', 'Recoleccion-Envases mixtos', 'lodos',
       'Recoleccion-construccion', 'Recoleccion-otros',
       'TOTAL RESIDUOS MEZCLADOS', 'TOTAL RESIDUOS DE RECOGIDA SEPARADA',
       'TOTAL RESIDUOS']].astype(int)
  
    return waste_collection


def clean_disposal(waste_disposal):   
    round(waste_disposal.iloc[:, 2:11],2)
    waste_disposal.drop(columns='Unnamed: 10', inplace = True , axis= 1)
    waste_disposal.rename(columns={'Comunidades Autónomas': 'Comunidad Autónoma'}, inplace=True)
    waste_disposal['Comunidad Autónoma'] = waste_disposal['Comunidad Autónoma'].str.upper()
    return waste_disposal

# def save_clean_files():
#     """Function that returns all clean files """

def merge(gdp, population, waste_collection, waste_disposal):
    import pandas as pd 
    population["Año"] = population["Año"].astype(str).astype(int)
    gdp["Año"] = gdp["Año"].astype(str).astype(int)
    waste_collection["Año"] = waste_collection["Año"].astype(str).astype(int)
    #waste_collection["Comunidad Autónoma"] = waste_collection["Comunidad Autónoma"].astype(float).astype(str)
    data_merged_gdp_pop =  pd.merge(left=gdp, right=population, how="outer", on=["Año", 'Comunidad Autónoma'])
    data_merged_gdp_pop['GDP per capita'] = round((data_merged_gdp_pop['PIB']/data_merged_gdp_pop['Poblacion']*1000),2)
    data_merged_2 =  pd.merge(left=data_merged_gdp_pop, right=waste_collection, how="outer", on=["Año", 'Comunidad Autónoma'])
    waste_management =  pd.merge(left=data_merged_2, right=waste_disposal, how="outer", on=["Año","Comunidad Autónoma"])
    #waste_management =  pd.merge(left=data_merged_3, right=waste_emissions, how="outer", on=["Año"])
    

    return waste_management

def rename_db(waste_management):
    new_names = {'Comunidad Autónoma': 'Autonomous communities', 'Año': 'Year', 'PIB':'GDP', 'Poblacion': 'Population', 'PIB per capita': 'GDP per capita', 'Recoleccion-domésticos y vias': 'Domestic Waste and Wheelie Bins -C', 'Recoleccion-voluminosos': 'Bulk -C',
       'Recoleccion-metálicos': 'Metallics waste-C', 'Recoleccion-vidrio': 'Waste Glass-C',
       'Recoleccion-papel y carton':'Waste Paper and Cardboard-C', 'Recoleccion-plasticos': 'Plastics-C',
       'Recoleccion-madera':'Waste Wood-C', 'Recoleccion-textiles':'Textile waste-C' ,
       'Recoleccion-eq. electricos': 'Electrical waste-C', 'Recoleccion-pilas': 'Battery-C',
       'Recoleccion-animales': 'Animal-C', 'Recoleccion-Envases mixtos': 'Mixed packaging-C', 'lodos': 'Sludge-C',
       'Recoleccion-construccion': 'Construction-C', 'Recoleccion-otros': 'Others-C',
       'TOTAL RESIDUOS MEZCLADOS': 'Total mixed waste-C', 'TOTAL RESIDUOS DE RECOGIDA SEPARADA': 'Total separately waste-C (tn)',
       'TOTAL RESIDUOS': 'Total Waste-C', 'Reciclado procedente de recogida separada': 'Recycling collection-D', 'Materiales recuperados-TMB mezclados': 'Mixed Recovered Mater-D', 
       'Compostado/Digestion anaerobia de FORS': 'Composting/anaerobic digestion FORS-D', 'Compostado/Digestión anaerobia': 'Composting/anaerobic digestion-D', 'Incinerado':'Incinerated-D',
       'Gestion: Incineracion (tn)': 'Incineration (tn)-D', 'Vertido de rechazos':'Landfill of rejects', 
       'Vertido sin tratamiento previo': 'Landfill without pre-treatment-D', 'Total': 'Total Waste disposal (tn)-D'}
    waste_management.rename(columns=new_names, inplace=True)
    return waste_management
    
def missing_or_null(waste_management):

    print(waste_management.isnull().sum())

def outliers_quantile(waste_management):
    Q1 = waste_management.quantile(0.25)
    Q3 = waste_management.quantile(0.75)
    IQR = Q3 - Q1
    print(IQR)

# def outliers_analysis(waste_management):
#     waste_management = waste_management[~((waste_management < (Q1 - 1.5 * IQR)) |(waste_management > (Q3 + 1.5 * IQR))).any(axis=1)]
#     print(waste_management.shape)

def analysis_tonsday(waste_management):
    waste_management['Total(tons/day)'] = round((waste_management['Total Waste-C']/365),2)
    return waste_management

def analysis_kg_percapita(waste_management):
    waste_management['Per Capita(kg/capita/day)'] = round((waste_management['Total Waste-C']/waste_management['Population']),2)
    return waste_management       
       
def analysis_processed_waste(waste_management):
    waste_management['Processed_waste'] = round((waste_management['Total Waste disposal (tn)-D']-waste_management['Landfill of rejects'] - waste_management['Landfill without pre-treatment-D']),2)
    return waste_management 

def analysis_not_processed_waste(waste_management):
    waste_management['Not Processed_waste'] = round((waste_management['Landfill of rejects']+waste_management['Landfill without pre-treatment-D']),2)
    return waste_management 

def save_csv(waste_management):   
       
    return waste_management.to_csv("../reports/waste_management_cleaned.csv", index = False)

def save_excel(waste_management):   
       
    return waste_management.to_excel("../reports/waste_management_cleaned.xlsx", index = False)  

def save_json(waste_management):   
       
    return waste_management.to_json("../reports/waste_management_cleaned.json")  