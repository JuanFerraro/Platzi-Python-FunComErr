import utils
import read_csv
import charts

def run():
    #Obtener data:
    data = read_csv.read_csv('./app/data.csv')
    country = input('Cual pais?: ')

    result = utils.population_by_country(data, country)
    if len(result) > 0:
        country = result[0]
        keys, values = utils.get_population(country)
        charts.generate_bar_chart(keys, values)

if __name__ == '__main__':
    run()