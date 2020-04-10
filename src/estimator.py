

def estimator(data):

    _data = data

    return {
        'data': _data,

        'impact': {
            'currentlyInfected': _data['reportedCases'] * 10,
            'infectionsByRequestedTime': (_data['reportedCases'] * 10) * (2 ** 19)
        },

        'severeImpact': {
            'currentlyInfected': _data['reportedCases'] * 50,
            'infectionsByRequestedTime': (_data['reportedCases'] * 10) * (2 ** 19)
        }

    }


'''
cc = {'sa': 4}
print(cc['sa'])
'''
