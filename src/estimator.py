



def estimator(data):
    input_data = {
        'region': {
            'name': "Africa",
            'avgAge': 19.7,
            'avgDailyIncomeInUSD': 5,
            'avgDailyIncomePopulation': 0.71
        },
        'periodType': "days",
        'timeToElapse': 58,
        'reportedCases': 674,
        'population': 66622705,
        'totalHospitalBeds': 1380614
}

    def convert_2_days():
        if input_data['periodType'] == 'days':
            converted_days = input_data['timeToElapse']

        elif input_data['periodType'] == 'weeks':
            converted_days = input_data['timeToElapse'] * 7

        elif input_data['periodType'] == 'weeks':
            converted_days = input_data['timeToElapse'] * 30

        return converted_days    


    return {
        'data': input_data,

        'impact': {
            'currentlyInfected': input_data['reportedCases'] * 10,
            'infectionsByRequestedTime': (input_data['reportedCases'] * 10) * (2 ** ( convert_2_days() / 3 ))
        },

        'severeImpact': {
            'currentlyInfected': input_data['reportedCases'] * 50,
            'infectionsByRequestedTime': (input_data['reportedCases'] * 10) * (2 ** ( convert_2_days() / 3))
        }

    }


'''

a = 34
b = 34 % 3
print(b)
'''