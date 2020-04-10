

def estimator(data):

    return {
        'data': data,

        'impact': {
            'currentlyInfected': data['reportedCases'] * 10,
            'infectionsByRequestedTime': (data['reportedCases'] * 10) * (2 ** 19)
        },

        'severeImpact': {
            'currentlyInfected': data['reportedCases'] * 50,
            'infectionsByRequestedTime': (data['reportedCases'] * 10) * (2 ** 19)
        }

    }


'''
cc = {'sa': 4}
print(cc['sa'])
'''
