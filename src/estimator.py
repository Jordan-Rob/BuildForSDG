def estimator(data):
    return data


def covid19ImpactEstimator(reportedCases):
    output = {
        'impact': {
            'currentlyInfected': reportedCases * 10,
            'infectionsByRequestedTime': (reportedCases * 10) * (2 ** 19)
        },

        'severeImpact': {
            'currentlyInfected': reportedCases * 50,
            'infectionsByRequestedTime': (reportedCases * 10) * (2 ** 19)
        }

    }

    return output
